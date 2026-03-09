import re
from pathlib import Path
base=Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/week06/submissions')
keys={
 'accuracy': [r'accuracy', r'not accurate|inaccurate|error', r'fix|correct|replace'],
 'missing':[r'missing data|missing', r'<=\s*20%|20\s*%', r'imput|replace|mean|median|mice|na\.omit'],
 'outliers':[r'mahalanobis|mahal', r'cut\s*off|cutoff|qchisq|chi', r'outlier'],
 'additivity':[r'additivity', r'symnum|correl|cor\('],
 'linearity':[r'linearity', r'scatter|pairs|plot'],
 'normality':[r'normality', r'qq|hist|density|plot'],
 'homog':[r'homogeneity|homoscedasticity|homog', r'levene|boxplot|plot']
}

def txt(html):
    t=html
    t=re.sub(r'(?is)<script.*?</script>',' ',t)
    t=re.sub(r'(?is)<style.*?</style>',' ',t)
    t=re.sub(r'(?s)<[^>]+>',' ',t)
    t=t.replace('&nbsp;',' ')
    t=re.sub(r'\s+',' ',t)
    return t.lower()

rows=[]
for p in sorted(base.iterdir()):
    if not p.is_file():
        continue
    s=p.read_text(errors='ignore')
    t=txt(s)
    sec_score=0
    det={}
    for sec,pats in keys.items():
        matches=sum(1 for pat in pats if re.search(pat,t))
        if matches>=2:
            sec_score += 1
        det[sec]=matches
    code_hits=len(re.findall(r'ggplot|mahalanobis|qchisq|symnum|pairs\(|cor\(|lm\(|plot\(',t))
    rows.append((p.name, sec_score, code_hits, len(t), det))

for name,score,code_hits,l,det in rows:
    print(f"{name}\tsec={score}/7\tcode={code_hits}\tlen={l}\tdet={det}")
