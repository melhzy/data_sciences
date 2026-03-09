import re, zipfile
from pathlib import Path

week = Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/week07')
subs = week / 'submissions'

def strip_html(s:str)->str:
    s = re.sub(r'(?is)<script.*?</script>', ' ', s)
    s = re.sub(r'(?is)<style.*?</style>', ' ', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s.lower()

def read_docx_text(path: Path) -> str:
    try:
        with zipfile.ZipFile(path, 'r') as z:
            xml = z.read('word/document.xml').decode('utf-8', errors='ignore')
        xml = re.sub(r'</w:p>', '\n', xml)
        xml = re.sub(r'<[^>]+>', ' ', xml)
        xml = re.sub(r'\s+', ' ', xml)
        return xml.lower()
    except Exception:
        return ''

def file_text(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in ['.html', '.htm']:
        return strip_html(path.read_text(errors='ignore'))
    if ext == '.docx':
        return read_docx_text(path)
    if ext == '.rmd':
        return path.read_text(errors='ignore').lower()
    return ''

def has_any(txt, arr):
    return any(a in txt for a in arr)

def has_re(txt, pat):
    return bool(re.search(pat, txt))

weights = {
    'data_import': 6,'accuracy': 8,'missing_pairwise': 6,'outliers': 12,
    'assumptions': 12,'plots': 12,'cor_types': 12,'strongest_biserial': 8,
    'ci_corr': 6,'diff_corr': 8,'gender_diff': 5,'partials': 5,'theory': 10,
}

rows = []
for p in sorted(subs.iterdir()):
    if not p.is_file():
        continue
    txt = file_text(p)
    if not txt:
        continue

    hits = {}
    hits['data_import'] = has_any(txt, ['07_data.csv','read.csv(','read_csv(','rio::import','import("07_data','import(\'07_data'])
    hits['accuracy'] = has_re(txt, r'accuracy|inaccurate|out[- ]of[- ]range|delete')
    hits['missing_pairwise'] = has_any(txt, ['pairwise','pairwise.complete.obs','exclude all data pairwise'])
    hits['outliers'] = all([
        has_re(txt, r'mahalanobis|mahal'),
        has_re(txt, r'cut\s*off|qchisq|chi-?square'),
        has_re(txt, r'\bdf\b|degrees of freedom'),
        has_re(txt, r'outlier|how many outliers|sum\(.*>.*cutoff')
    ])
    hits['assumptions'] = all([has_any(txt,['linearity']), has_any(txt,['normality']), has_re(txt,r'homogeneity|homoscedasticity')])
    hits['plots'] = all([
        has_any(txt,['temporality']) and has_any(txt,['relativity']),
        has_any(txt,['expectability']) and has_any(txt,['positive']),
        has_any(txt,['gender']),
        has_re(txt, r'geom_smooth|abline\(lm|lm\(')
    ])
    hits['cor_types'] = all([has_any(txt,['pearson']), has_any(txt,['spearman']), has_any(txt,['kendall'])])
    hits['strongest_biserial'] = has_re(txt, r'strongest|point\s*biserial|biserial')
    hits['ci_corr'] = has_re(txt, r'confidence interval|\bci\b|cicor|fisher')
    hits['diff_corr'] = has_re(txt, r'difference in correlations|cocor|significant difference')
    hits['gender_diff'] = has_re(txt, r'gender.*difference in correlations|group.*difference')
    hits['partials'] = has_re(txt, r'partial|semi.?partial')

    theory_count = 0
    for pat in [r'model for understanding', r'model fit', r'correlation and covariance', r'nonparametric', r'semi.?partial and partial', r'difference between r and r']:
        if has_re(txt, pat):
            theory_count += 1
    hits['theory'] = theory_count >= 3

    score = sum(weights[k] for k,v in hits.items() if v)

    ext = p.suffix.lower()
    if ext == '.docx':
        score -= 4
    if ext == '.rmd':
        score -= 5
    if has_re(txt, r'runif\(|sample\(|rnorm\('):
        score -= 8

    score = max(0, min(100, score))
    student = p.name.split('_')[0].lower()
    rows.append((student, p.name, score, hits))

best = {}
for student, fname, score, hits in rows:
    if student not in best or score > best[student][1]:
        best[student] = (fname, score, hits)

for s in sorted(best):
    fname, score, hits = best[s]
    print(f"{s}\t{score}\t{fname}\t{sum(1 for v in hits.values() if v)}/13")
