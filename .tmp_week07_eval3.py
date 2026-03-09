import re, zipfile
from pathlib import Path
week = Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/week07')
subs = week / 'submissions'

def strip_html(s):
    s = re.sub(r'(?is)<script.*?</script>', ' ', s)
    s = re.sub(r'(?is)<style.*?</style>', ' ', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', s).lower()

def read_docx(path):
    try:
        with zipfile.ZipFile(path, 'r') as z:
            xml = z.read('word/document.xml').decode('utf-8', errors='ignore')
        xml = re.sub(r'</w:p>', '\n', xml)
        xml = re.sub(r'<[^>]+>', ' ', xml)
        return re.sub(r'\s+', ' ', xml).lower()
    except Exception:
        return ''

def text_of(path):
    e = path.suffix.lower()
    if e in ['.html', '.htm']:
        return strip_html(path.read_text(errors='ignore'))
    if e == '.docx':
        return read_docx(path)
    if e == '.rmd':
        return path.read_text(errors='ignore').lower()
    return ''

def has_re(t,p): return bool(re.search(p,t))
def has_any(t,arr): return any(a in t for a in arr)

weights = {'data_import':6,'accuracy':8,'missing_pairwise':6,'outliers':12,'assumptions':12,'plots':12,'cor_types':12,'strongest_biserial':8,'ci_corr':6,'diff_corr':8,'gender_diff':5,'partials':5,'theory':10}
max_raw = sum(weights.values())

best={}
for p in sorted(subs.iterdir()):
    if not p.is_file():
        continue
    t=text_of(p)
    if not t:
        continue
    h={}
    h['data_import']=has_any(t,['07_data.csv','read.csv(','read_csv(','rio::import','import("07_data','import(\'07_data'])
    h['accuracy']=has_re(t,r'accuracy|inaccurate|out[- ]of[- ]range|delete')
    h['missing_pairwise']=has_any(t,['pairwise','pairwise.complete.obs','exclude all data pairwise'])
    h['outliers']=all([has_re(t,r'mahalanobis|mahal'),has_re(t,r'cut\s*off|qchisq|chi-?square'),has_re(t,r'\bdf\b|degrees of freedom'),has_re(t,r'outlier|how many outliers|sum\(.*>.*cutoff')])
    h['assumptions']=all([has_any(t,['linearity']),has_any(t,['normality']),has_re(t,r'homogeneity|homoscedasticity')])
    h['plots']=all([has_any(t,['temporality']) and has_any(t,['relativity']),has_any(t,['expectability']) and has_any(t,['positive']),has_any(t,['gender']),has_re(t,r'geom_smooth|abline\(lm|lm\(')])
    h['cor_types']=all([has_any(t,['pearson']),has_any(t,['spearman']),has_any(t,['kendall'])])
    h['strongest_biserial']=has_re(t,r'strongest|point\s*biserial|biserial')
    h['ci_corr']=has_re(t,r'confidence interval|\bci\b|cicor|fisher')
    h['diff_corr']=has_re(t,r'difference in correlations|cocor|significant difference')
    h['gender_diff']=has_re(t,r'gender.*difference in correlations|group.*difference')
    h['partials']=has_re(t,r'partial|semi.?partial')
    theory_count=sum(1 for pat in [r'model for understanding',r'model fit',r'correlation and covariance',r'nonparametric',r'semi.?partial and partial',r'difference between r and r'] if has_re(t,pat))
    h['theory']=theory_count>=3

    raw = sum(weights[k] for k,v in h.items() if v)
    grade = round(raw / max_raw * 100)
    ext=p.suffix.lower()
    if ext=='.docx': grade -= 4
    if ext=='.rmd': grade -= 5
    if has_re(t,r'runif\(|sample\(|rnorm\('): grade -= 8
    grade=max(0,min(100,grade))

    student=p.name.split('_')[0].lower()
    rec=(p.name,grade,h,raw)
    if student not in best or grade>best[student][1]:
        best[student]=rec

for s in sorted(best):
    f,g,h,raw=best[s]
    print(f"{s}\t{g}\t{f}\t{sum(1 for v in h.values() if v)}/13\traw={raw}")
