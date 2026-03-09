import re, zipfile
from pathlib import Path

subs = Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/week08/submissions')

def read_docx(path):
    try:
        with zipfile.ZipFile(path,'r') as z:
            xml=z.read('word/document.xml').decode('utf-8',errors='ignore')
        xml=re.sub(r'</w:p>','\n',xml)
        xml=re.sub(r'<[^>]+>',' ',xml)
        return re.sub(r'\s+',' ',xml)
    except Exception:
        return ''

def read_html(path):
    s=path.read_text(errors='ignore')
    s=re.sub(r'(?is)<script.*?</script>',' ',s)
    s=re.sub(r'(?is)<style.*?</style>',' ',s)
    s=re.sub(r'(?s)<[^>]+>',' ',s)
    return re.sub(r'\s+',' ',s)

def get_text(path):
    e=path.suffix.lower()
    if e in ['.html','.htm']: return read_html(path)
    if e=='.docx': return read_docx(path)
    if e=='.rmd': return path.read_text(errors='ignore')
    return ''

def has_re(t,p): return bool(re.search(p,t,re.I))
def count_re(t,p): return len(re.findall(p,t,re.I))

for p in sorted(subs.iterdir()):
    if not p.is_file():
        continue
    t=get_text(p)
    if not t:
        continue
    student=p.name.split('_')[0].lower()

    # Explanatory language indicators
    first_person = count_re(t, r'\b(i|we|my|our)\b')
    interpretive_terms = count_re(t, r'interpret|suggest|indicat|therefore|because|implies|in this|this means|we found|i found|results show')
    requirement_q = count_re(t, r'do you think|what type of relationship|is there a significant difference|include')
    # likely copied prompt/template residue (penalty)
    template_residue = count_re(t, r'what are we using as our model|calculate the difference in correlations|include the output|do you think you\'ve met')
    # AI-style generic instruction text in result sections (penalty)
    generic_instr = count_re(t, r'to assess|follow these steps|you can use the following code|for demonstration|assuming you have')

    # quick technical completeness proxy
    technical = 0
    for pat in [r'leverage|hatvalues', r'cook', r'mahalanobis|mahal', r'hierarchical|model 1|step 1', r'mediation|sobel|bootstrap', r'anova\(']:
        if has_re(t, pat): technical += 1

    print(f"{student}\t{p.name}\ttech={technical}\tfp={first_person}\tinterp={interpretive_terms}\treqQ={requirement_q}\ttemplate={template_residue}\tgeneric={generic_instr}")
