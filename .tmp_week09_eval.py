import re, zipfile
from pathlib import Path

base = Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/week09')
subs = base / 'submissions'

# ---------- readers ----------
def read_docx(path: Path) -> str:
    try:
        with zipfile.ZipFile(path, 'r') as z:
            xml = z.read('word/document.xml').decode('utf-8', errors='ignore')
        xml = re.sub(r'</w:p>', '\n', xml)
        xml = re.sub(r'<[^>]+>', ' ', xml)
        return re.sub(r'\s+', ' ', xml)
    except Exception:
        return ''

def read_html(path: Path) -> str:
    s = path.read_text(errors='ignore')
    s = re.sub(r'(?is)<script.*?</script>', ' ', s)
    s = re.sub(r'(?is)<style.*?</style>', ' ', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', s)

def get_text(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in ['.html', '.htm']:
        return read_html(path)
    if ext == '.docx':
        return read_docx(path)
    if ext == '.rmd':
        return path.read_text(errors='ignore')
    return ''

# ---------- helpers ----------
def has_re(t, p):
    return bool(re.search(p, t, flags=re.I))

def count_re(t, p):
    return len(re.findall(p, t, flags=re.I))

def has_any(t, arr):
    lt = t.lower()
    return any(a.lower() in lt for a in arr)

weights = {
    'data_import': 4,
    'accuracy': 5,
    'missing': 4,
    'outliers': 9,
    'assumptions': 8,
    'additivity_answer': 3,
    'ind_t': 10,
    'ind_effect': 4,
    'ind_power': 4,
    'ind_graph': 3,
    'ind_writeup': 8,
    'dep_t': 10,
    'dep_effect': 4,
    'dep_power': 4,
    'dep_graph': 3,
    'dep_writeup': 8,
    'theory_qs': 9,
    'apa_elements': 6,
}
max_raw = sum(weights.values())

results = []
for p in sorted(subs.iterdir()):
    if not p.is_file():
        continue
    t = get_text(p)
    if not t:
        continue

    h = {}
    h['data_import'] = has_any(t, ['09_data.csv', 'read.csv(', 'rio::import', 'import("09_data', "import('09_data"])

    h['accuracy'] = has_re(t, r'accuracy|inaccurate|out[- ]of[- ]range|fixed|correct')
    h['missing'] = has_re(t, r'missing data|is\.na|drop_na|na\.omit|imput')
    h['outliers'] = all([
        has_re(t, r'mahalanobis|mahal'),
        has_re(t, r'\bdf\b|degrees of freedom'),
        has_re(t, r'cut\s*off|cutoff|qchisq|chi-?square'),
        has_re(t, r'how many outlier|number of outlier|sum\(.*>.*cut')
    ]) and has_re(t, r'delete|remove|exclude')

    h['assumptions'] = all([
        has_re(t, r'linearity'),
        has_re(t, r'normality'),
        has_re(t, r'homogeneity|homoscedasticity')
    ])
    h['additivity_answer'] = has_re(t, r'additivity') and has_re(t, r'won\'t need|not need|not necessary|because')

    # independent t test block
    h['ind_t'] = all([
        has_re(t, r'independent t-?test|t\.test\(.*gender|pal_cell.*gender|gender.*pal_cell'),
        has_re(t, r'equal variances|var\.equal|welch|homogeneity'),
        has_re(t, r'mean|sd|standard deviation'),
        has_re(t, r'significant')
    ])
    h['ind_effect'] = has_re(t, r'effect size|cohen\'?s d|hedges')
    h['ind_power'] = has_re(t, r'power|pwr\.|sample size|participants should have used')
    h['ind_graph'] = has_re(t, r'bar graph|geom_bar|stat_summary|graph1')
    h['ind_writeup'] = has_re(t, r'apa') and has_re(t, r'independent') and has_re(t, r't\(')

    # dependent t test block
    h['dep_t'] = all([
        has_re(t, r'dependent t-?test|paired t-?test|t\.test\(.*paired\s*=\s*true|pal_cell.*pal_acc|pal_acc.*pal_cell'),
        has_re(t, r'mean|sd|standard deviation'),
        has_re(t, r'significant')
    ])
    h['dep_effect'] = has_re(t, r'effect size|cohen\'?s d|dz|hedges')
    h['dep_power'] = has_re(t, r'power|pwr\.|sample size|participants should have used')
    h['dep_graph'] = has_re(t, r'graph2|bar graph|geom_bar|stat_summary')
    h['dep_writeup'] = has_re(t, r'apa') and has_re(t, r'dependent|paired') and has_re(t, r't\(')

    # theory Q11-16 evidence
    theory_hits = 0
    for pat in [r'null hypothesis', r'research hypothesis|alternative hypothesis', r'mean difference score', r'systematic variance', r'unsystematic variance']:
        if has_re(t, pat):
            theory_hits += 1
    h['theory_qs'] = theory_hits >= 4

    # APA reporting elements
    apa_count = 0
    for pat in [r'\bmean\b|\bm\b', r'\bsd\b|standard deviation|standard error', r'\bt\b\s*\(|t-value|t value', r'\bp\b\s*[<=>]', r'effect size|cohen', r'plain english|in plain english|this means|indicates that']:
        if has_re(t, pat):
            apa_count += 1
    h['apa_elements'] = apa_count >= 5

    raw = sum(weights[k] for k,v in h.items() if v)

    # ---------- originality / own-language score ----------
    first_person = count_re(t, r'\b(i|we|my|our)\b')
    interpretive = count_re(t, r'interpret|suggest|indicat|therefore|because|implies|this means|results show|we found|i found')
    prompt_residue = count_re(t, r'include output|what is your|do you think you\'ve met|list the null hypothesis|list the research hypothesis')
    generic_ai = count_re(t, r'follow these steps|you can use the following code|for demonstration|assuming you have|to assess')

    language_bonus = min(12, interpretive*0.9 + first_person*0.1)
    language_penalty = min(18, prompt_residue*1.5 + generic_ai*2)

    grade = round((raw / max_raw) * 88 + language_bonus - language_penalty)

    # mild format adjustment
    ext = p.suffix.lower()
    if ext == '.docx':
        grade -= 2
    if ext == '.rmd':
        grade -= 3

    grade = max(0, min(100, grade))

    student = p.name.split('_')[0].lower()
    results.append({
        'student': student,
        'file': p.name,
        'grade': grade,
        'raw': raw,
        'criteria_hit': sum(1 for v in h.values() if v),
        'first_person': first_person,
        'interpretive': interpretive,
        'prompt_residue': prompt_residue,
        'generic_ai': generic_ai,
        'hits': h
    })

# pick best submission per student
best = {}
for r in results:
    s = r['student']
    if s not in best or r['grade'] > best[s]['grade']:
        best[s] = r

for s in sorted(best):
    r = best[s]
    print(f"{s}\t{r['grade']}\t{r['file']}\thits={r['criteria_hit']}/{len(weights)}\tinterp={r['interpretive']}\tprompt={r['prompt_residue']}\tgeneric={r['generic_ai']}")
