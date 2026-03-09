import re, zipfile
from pathlib import Path

week = Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/week07')
subs = week / 'submissions'
book = Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/Knowledge/Field_ea_2012_Discovering_Statistics_using_R_normalized.txt')

# quick reference extraction from textbook
book_text = book.read_text(errors='ignore').lower()
ref_hits = {
    'correlation': len(re.findall(r'\bcorrelation\b', book_text)),
    'pearson': len(re.findall(r'\bpearson\b', book_text)),
    'spearman': len(re.findall(r'\bspearman\b', book_text)),
    'kendall': len(re.findall(r'\bkendall\b', book_text)),
    'mahalanobis': len(re.findall(r'\bmahalanobis\b', book_text)),
    'partial': len(re.findall(r'\bpartial\b', book_text)),
}
print('TEXTBOOK_REFERENCE_HITS', ref_hits)


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
        xml = re.sub(r'<w:tab\s*/>', ' ', xml)
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


def b(pat, txt):
    return bool(re.search(pat, txt))

weights = {
    'data_import': 6,
    'accuracy': 8,
    'missing_pairwise': 6,
    'outliers': 12,
    'assumptions': 12,
    'plots': 12,
    'cor_types': 12,
    'strongest_biserial': 8,
    'ci_corr': 6,
    'diff_corr': 8,
    'gender_diff': 5,
    'partials': 5,
    'theory': 10,
}

rows = []
for p in sorted(subs.iterdir()):
    if not p.is_file():
        continue
    txt = file_text(p)
    if not txt:
        rows.append((p.name, 0, 'unreadable'))
        continue

    score = 0
    hits = {}

    hits['data_import'] = b(r'07_data\\.csv|read\\.csv\\(|rio::import|import\\("07_data|import\\(\'07_data', txt)
    hits['accuracy'] = b(r'accuracy|inaccurate|out[- ]of[- ]range|delete', txt)
    hits['missing_pairwise'] = b(r'pairwise|pairwise\\.complete\\.obs|exclude all data pairwise', txt)
    hits['outliers'] = all([
        b(r'mahalanobis|mahal', txt),
        b(r'cut\s*off|qchisq|chi-?square', txt),
        b(r'\bdf\b|degrees of freedom', txt),
        b(r'how many outliers|sum\(.*>.*cutoff|outliers?', txt)
    ])
    hits['assumptions'] = all([
        b(r'linearity', txt), b(r'normality', txt), b(r'homogeneity|homoscedasticity', txt)
    ])
    hits['plots'] = all([
        b(r'temporality', txt) and b(r'relativity', txt),
        b(r'expectability', txt) and b(r'positive', txt),
        b(r'gender', txt),
        b(r'geom_smooth|abline\(lm|lm\(', txt)
    ])
    hits['cor_types'] = all([b(r'pearson', txt), b(r'spearman', txt), b(r'kendall', txt)])
    hits['strongest_biserial'] = b(r'strongest|point\s*biserial|biserial', txt)
    hits['ci_corr'] = b(r'confidence interval|ci|cicor|fisher', txt)
    hits['diff_corr'] = b(r'difference in correlations|cocor|significant difference', txt)
    hits['gender_diff'] = b(r'gender.*difference in correlations|group.*difference', txt)
    hits['partials'] = b(r'partial|semi.?partial', txt)
    theory_q = sum(1 for pat in [r'model for understanding', r'model fit', r'correlation and covariance', r'difference between r and r\b|difference between r and r\^2|difference between r and r\s', r'nonparametric', r'semi.?partial and partial'] if b(pat, txt))
    hits['theory'] = theory_q >= 3

    for k,w in weights.items():
        if hits.get(k, False):
            score += w

    # format penalties/bonuses
    ext = p.suffix.lower()
    if ext == '.docx':
        score -= 4
    if ext == '.rmd':
        score -= 5
    if b(r'runif\(|sample\(|rnorm\(', txt):
        score -= 8
    score = max(0, min(100, score))

    student = p.name.split('_')[0].lower()
    rows.append((student, p.name, score, hits))

# keep best submission per student
best = {}
for student, fname, score, hits in rows:
    if student not in best or score > best[student][1]:
        best[student] = (fname, score, hits)

for s in sorted(best):
    fname, score, hits = best[s]
    print(f"{s}\t{score}\t{fname}\t{sum(1 for v in hits.values() if v)}/13")
