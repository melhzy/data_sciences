import re, zipfile
from pathlib import Path
base = Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/week09/submissions')

def rd_docx(p):
    try:
        with zipfile.ZipFile(p,'r') as z:
            x=z.read('word/document.xml').decode('utf-8',errors='ignore')
        x=re.sub(r'</w:p>','\n',x)
        x=re.sub(r'<[^>]+>',' ',x)
        return re.sub(r'\s+',' ',x)
    except Exception:
        return ''

def rd_html(p):
    s=p.read_text(errors='ignore')
    s=re.sub(r'(?is)<script.*?</script>',' ',s)
    s=re.sub(r'(?is)<style.*?</style>',' ',s)
    s=re.sub(r'(?s)<[^>]+>',' ',s)
    return re.sub(r'\s+',' ',s)

def txt(p):
    e=p.suffix.lower()
    if e in ['.html','.htm']: return rd_html(p)
    if e=='.docx': return rd_docx(p)
    if e=='.rmd': return p.read_text(errors='ignore')
    return ''

def hr(t,p): return bool(re.search(p,t,re.I))
def cr(t,p): return len(re.findall(p,t,re.I))
def ha(t,a):
    l=t.lower(); return any(x.lower() in l for x in a)

weights={'data_import':4,'accuracy':5,'missing':4,'outliers':9,'assumptions':8,'additivity_answer':3,'ind_t':10,'ind_effect':4,'ind_power':4,'ind_graph':3,'ind_writeup':8,'dep_t':10,'dep_effect':4,'dep_power':4,'dep_graph':3,'dep_writeup':8,'theory_qs':9,'apa_elements':6}
mx=sum(weights.values())
rows=[]
for p in sorted(base.iterdir()):
    if not p.is_file(): continue
    t=txt(p)
    if not t: continue
    h={}
    h['data_import']=ha(t,['09_data.csv','read.csv(','rio::import','import("09_data',"import('09_data"])
    h['accuracy']=hr(t,r'accuracy|inaccurate|out[- ]of[- ]range|fixed|correct')
    h['missing']=hr(t,r'missing data|is\.na|drop_na|na\.omit|imput')
    h['outliers']=all([hr(t,r'mahalanobis|mahal'),hr(t,r'\bdf\b|degrees of freedom'),hr(t,r'cut\s*off|cutoff|qchisq|chi-?square'),hr(t,r'outlier')]) and hr(t,r'delete|remove|exclude')
    h['assumptions']=all([hr(t,r'linearity'),hr(t,r'normality'),hr(t,r'homogeneity|homoscedasticity')])
    h['additivity_answer']=hr(t,r'additivity') and hr(t,r'won\'t need|not need|not necessary|because')
    h['ind_t']=all([hr(t,r'independent t-?test|t\.test\(.*gender|pal_cell.*gender|gender.*pal_cell'),hr(t,r'equal variances|var\.equal|welch|homogeneity'),hr(t,r'mean|sd|standard deviation'),hr(t,r'significant')])
    h['ind_effect']=hr(t,r'effect size|cohen\'?s d|hedges')
    h['ind_power']=hr(t,r'power|pwr\.|sample size|participants should have used')
    h['ind_graph']=hr(t,r'bar graph|geom_bar|stat_summary|graph1')
    h['ind_writeup']=hr(t,r'apa') and hr(t,r'independent') and hr(t,r't\(')
    h['dep_t']=all([hr(t,r'dependent t-?test|paired t-?test|t\.test\(.*paired\s*=\s*true|pal_cell.*pal_acc|pal_acc.*pal_cell'),hr(t,r'mean|sd|standard deviation'),hr(t,r'significant')])
    h['dep_effect']=hr(t,r'effect size|cohen\'?s d|dz|hedges')
    h['dep_power']=hr(t,r'power|pwr\.|sample size|participants should have used')
    h['dep_graph']=hr(t,r'graph2|bar graph|geom_bar|stat_summary')
    h['dep_writeup']=hr(t,r'apa') and hr(t,r'dependent|paired') and hr(t,r't\(')
    th=0
    for pat in [r'null hypothesis',r'research hypothesis|alternative hypothesis',r'mean difference score',r'systematic variance',r'unsystematic variance']:
        if hr(t,pat): th+=1
    h['theory_qs']=th>=4
    ap=0
    for pat in [r'\bmean\b|\bm\b',r'\bsd\b|standard deviation|standard error',r'\bt\b\s*\(|t-value|t value',r'\bp\b\s*[<=>]',r'effect size|cohen',r'plain english|in plain english|this means|indicates that']:
        if hr(t,pat): ap+=1
    h['apa_elements']=ap>=5

    raw=sum(weights[k] for k,v in h.items() if v)
    first=cr(t,r'\b(i|we|my|our)\b')
    interp=cr(t,r'interpret|suggest|indicat|therefore|because|implies|this means|results show|we found|i found')
    prompt=cr(t,r'include output|what is your|do you think you\'ve met|list the null hypothesis|list the research hypothesis')
    generic=cr(t,r'follow these steps|you can use the following code|for demonstration|assuming you have|to assess')

    bonus=min(12,interp*0.9 + first*0.08)
    penalty=min(10,prompt*0.5 + generic*1.2)
    if interp>=12:
        penalty=penalty*0.5

    grade=round((raw/mx)*88 + bonus - penalty)
    e=p.suffix.lower()
    if e=='.docx': grade-=2
    if e=='.rmd': grade-=3
    grade=max(0,min(100,grade))

    s=p.name.split('_')[0].lower()
    rows.append((s,p.name,grade,sum(1 for v in h.values() if v),interp,prompt,generic))

best={}
for r in rows:
    if r[0] not in best or r[2]>best[r[0]][2]: best[r[0]]=r
for s in sorted(best):
    r=best[s]
    print(f"{s}\t{r[2]}\t{r[1]}\thits={r[3]}/18\tinterp={r[4]}\tprompt={r[5]}\tgeneric={r[6]}")
