import re
from pathlib import Path
base=Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/week06/submissions')

def extract_text(s):
    s=re.sub(r'(?is)<script.*?</script>',' ',s)
    s=re.sub(r'(?is)<style.*?</style>',' ',s)
    imgs=len(re.findall(r'(?is)<img\b',s))
    s=re.sub(r'(?s)<[^>]+>',' ',s)
    s=s.replace('&nbsp;',' ')
    s=re.sub(r'\s+',' ',s)
    return s.lower(), imgs

for p in sorted(base.iterdir()):
    if not p.is_file():
        continue
    s=p.read_text(errors='ignore')
    t,imgs=extract_text(s)
    indicators={}
    indicators['accuracy_fix']=1 if (re.search(r'accuracy',t) and re.search(r'fix|correct|replace',t)) else 0
    indicators['missing_rule']=1 if re.search(r'20\s*%|<=\s*20%',t) else 0
    indicators['missing_action']=1 if re.search(r'imput|replace|mean|median|na\.omit|remove',t) else 0
    indicators['mahal']=1 if re.search(r'mahalanobis|mahal',t) else 0
    indicators['outlier_count']=1 if re.search(r'\b\d+\s+outlier|outlier\s*[:=]?\s*\d+',t) else 0
    indicators['df']=1 if re.search(r'\bdf\b|degrees of freedom',t) else 0
    indicators['cutoff']=1 if re.search(r'cut\s*off|cutoff|qchisq|chi',t) else 0
    indicators['delete_outliers']=1 if re.search(r'delet|remov',t) else 0
    indicators['additivity_output']=1 if re.search(r'symnum|correl|cor\(',t) else 0
    indicators['linearity_output']=1 if re.search(r'linearity',t) and (imgs>0 or re.search(r'scatter|pairs\(',t)) else 0
    indicators['normality_output']=1 if re.search(r'normality',t) and (imgs>0 or re.search(r'qq|hist|density',t)) else 0
    indicators['homog_output']=1 if re.search(r'homogene|homoscedastic',t) and (imgs>0 or re.search(r'boxplot|levene',t)) else 0
    indicators['interpretation']=len(re.findall(r'i\s+(?:do|did)\s*(?:not\s*)?think|assumption\s+(?:is\s+)?(?:met|not met)|we\s+(?:meet|do not meet)',t))

    score = 0
    score += 15 if indicators['accuracy_fix'] else 0
    score += 7 if indicators['missing_rule'] else 0
    score += 8 if indicators['missing_action'] else 0
    out = indicators['mahal'] + indicators['outlier_count'] + indicators['df'] + indicators['cutoff'] + indicators['delete_outliers']
    score += int(25*out/5)
    score += 10 if indicators['additivity_output'] else 0
    score += 10 if indicators['linearity_output'] else 0
    score += 10 if indicators['normality_output'] else 0
    score += 10 if indicators['homog_output'] else 0
    score += 5 if indicators['interpretation']>=3 else (3 if indicators['interpretation']>=1 else 0)
    score=min(100,score)

    print(p.name)
    print(f"  score={score} imgs={imgs} interp_hits={indicators['interpretation']} ind={indicators}")
