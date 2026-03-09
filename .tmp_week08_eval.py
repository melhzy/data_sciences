import re, zipfile
from pathlib import Path

base = Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/week08')
subs = base / 'submissions'
book = Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/Knowledge/Field_ea_2012_Discovering_Statistics_using_R_normalized.txt')

book_text = book.read_text(errors='ignore').lower()
book_ref = {
    'regression': len(re.findall(r'\bregression\b', book_text)),
    'mediation': len(re.findall(r'\bmediat', book_text)),
    'moderation': len(re.findall(r'\bmoderat', book_text)),
    'leverage': len(re.findall(r'\bleverage\b', book_text)),
    'cook': len(re.findall(r"cook'?s", book_text)),
    'multicollinearity': len(re.findall(r'\bmulticollinearity\b', book_text)),
}
print('BOOK_REF', book_ref)

def read_docx(path: Path) -> str:
    try:
        with zipfile.ZipFile(path, 'r') as z:
            xml = z.read('word/document.xml').decode('utf-8', errors='ignore')
        xml = re.sub(r'</w:p>', '\n', xml)
        xml = re.sub(r'<[^>]+>', ' ', xml)
        return re.sub(r'\s+', ' ', xml).lower()
    except Exception:
        return ''

def read_html(path: Path) -> str:
    s = path.read_text(errors='ignore')
    s = re.sub(r'(?is)<script.*?</script>', ' ', s)
    s = re.sub(r'(?is)<style.*?</style>', ' ', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', s).lower()

def get_text(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in ['.html', '.htm']:
        return read_html(path)
    if ext == '.docx':
        return read_docx(path)
    if ext == '.rmd':
        return path.read_text(errors='ignore').lower()
    return ''

def has_any(t, arr):
    return any(a in t for a in arr)

def has_re(t, pat):
    return bool(re.search(pat, t))

weights = {
    'data_import': 5,
    'factor_type_work': 5,
    'leverage': 8,
    'cooks': 8,
    'mahal': 8,
    'overall_outliers': 8,
    'additivity': 8,
    'linearity': 6,
    'normality': 6,
    'homog': 6,
    'hierarchical_steps': 14,
    'anova_change': 6,
    'mediation_paths': 6,
    'sobel': 3,
    'boot_indirect': 3,
    'writeup': 10,
}
max_raw = sum(weights.values())

records = []
for p in sorted(subs.iterdir()):
    if not p.is_file():
        continue
    t = get_text(p)
    if not t:
        # image-only/unsupported files
        student = p.name.split('_')[0].lower()
        records.append((student, p.name, 0, {'readable': False}, 0, 'unsupported'))
        continue

    hits = {}
    hits['data_import'] = has_any(t, ['08_data.sav','08_data.csv','read.spss','read_sav','rio::import','import("08_data','import(\'08_data'])
    hits['factor_type_work'] = has_re(t, r'factor\s*\(\s*.*type[_ ]?work|as\.factor\s*\(\s*.*type[_ ]?work|type[_ ]?work\s*<-\s*factor')

    hits['leverage'] = all([
        has_re(t, r'leverage|hatvalues|hat values'),
        has_re(t, r'cut\s*off|cutoff|2\*\(k\+1\)/n|3\*\(k\+1\)/n'),
        has_re(t, r'how many|count|sum\(')
    ])
    hits['cooks'] = all([
        has_re(t, r"cook'?s|cooks\.distance"),
        has_re(t, r'cut\s*off|cutoff|4/n|1'),
        has_re(t, r'how many|count|sum\(')
    ])
    hits['mahal'] = all([
        has_re(t, r'mahalanobis|mahal'),
        has_re(t, r'\bdf\b|degrees of freedom'),
        has_re(t, r'cut\s*off|cutoff|qchisq|chi-?square'),
        has_re(t, r'outlier|how many|count|sum\(')
    ])
    hits['overall_outliers'] = has_re(t, r'overall.*outlier|total outlier|delete them|remove outlier|filtered data|noout|clean')

    hits['additivity'] = has_re(t, r'cor\(|correlation table|multicollinearity|vif')
    hits['linearity'] = has_re(t, r'linearity|residuals|fitted|plot')
    hits['normality'] = has_re(t, r'normality|qq|q-q|shapiro|hist')
    hits['homog'] = has_re(t, r'homoscedastic|homogeneity|residuals.*fitted|plot')

    # hierarchical regression requirements
    has_step1 = has_re(t, r'years')
    has_step2 = has_re(t, r'type[_ ]?work')
    has_step3 = has_re(t, r'affective') and has_re(t, r'cognitive')
    has_hier = has_re(t, r'hierarchical|step 1|step 2|step 3|model 1|model 2|model 3|lm\(')
    hits['hierarchical_steps'] = has_hier and has_step1 and has_step2 and has_step3
    hits['anova_change'] = has_re(t, r'anova\(|change between each step|delta r|r\^2 change|f[- ]change')

    hits['mediation_paths'] = has_re(t, r'mediation|path a|path b|path c|indirect') and has_re(t, r'years') and has_re(t, r'affective') and has_re(t, r'ocb')
    hits['sobel'] = has_re(t, r'sobel')
    hits['boot_indirect'] = has_re(t, r'boot|bootstrap|bootstrapped indirect')

    # write-up checks
    write_q = 0
    for pat in [r'brief description|experiment|variables', r'data screening|assumption', r'f-?value', r'\bbeta\b|\bb\b', r'interpretation|dummy coding|study results']:
        if has_re(t, pat):
            write_q += 1
    hits['writeup'] = write_q >= 3

    raw = sum(weights[k] for k,v in hits.items() if v)
    grade = round(raw / max_raw * 100)

    ext = p.suffix.lower()
    if ext == '.docx':
        grade -= 3
    if ext == '.rmd':
        grade -= 5
    if has_re(t, r'runif\(|sample\(|rnorm\('):
        grade -= 8

    # wrong artifacts penalty
    if ext in ['.png', '.jpg', '.jpeg']:
        grade = 0

    grade = max(0, min(100, grade))
    student = p.name.split('_')[0].lower()
    records.append((student, p.name, grade, hits, raw, 'ok'))

# keep best file per student
best = {}
for student, fname, grade, hits, raw, status in records:
    if student not in best or grade > best[student][1]:
        best[student] = (fname, grade, hits, raw, status)

for s in sorted(best):
    f,g,h,raw,status = best[s]
    print(f"{s}\t{g}\t{f}\t{sum(1 for v in h.values() if v) if isinstance(h, dict) else 0}/16\traw={raw}\t{status}")
