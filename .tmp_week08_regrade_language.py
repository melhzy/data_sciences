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

def txt(path):
    e=path.suffix.lower()
    if e in ['.html','.htm']: return read_html(path)
    if e=='.docx': return read_docx(path)
    if e=='.rmd': return path.read_text(errors='ignore')
    return ''

def hr(t,p): return bool(re.search(p,t,re.I))
def cr(t,p): return len(re.findall(p,t,re.I))

records=[]
for p in sorted(subs.iterdir()):
    if not p.is_file():
        continue
    t=txt(p)
    if not t:
        continue
    student=p.name.split('_')[0].lower()

    tech=0
    for pat in [r'leverage|hatvalues',r"cook'?s|cooks\.distance",r'mahalanobis|mahal',r'hierarchical|model 1|step 1',r'mediation|path a|path b|indirect',r'anova\(']:
        if hr(t,pat): tech += 1

    fp=cr(t,r'\b(i|we|my|our)\b')
    interp=cr(t,r'interpret|suggest|indicat|therefore|because|implies|this means|results show|we found|i found')
    template=cr(t,r'what are we using as our model|include the output|calculate the difference in correlations|do you think you\'ve met')
    generic=cr(t,r'to assess|follow these steps|you can use the following code|for demonstration|assuming you have')

    # grading emphasizing own language
    tech_score = 58 + tech*6          # 58-94
    language_score = min(18, interp*1.2 + fp*0.15)
    originality_penalty = min(18, template*2 + generic*2)
    format_penalty = 3 if p.suffix.lower()=='.docx' else 0

    grade = round(max(0, min(100, tech_score + language_score - originality_penalty - format_penalty)))

    records.append((student,p.name,grade,tech,interp,fp,template,generic))

# choose best per student
best={}
for rec in records:
    s=rec[0]
    if s not in best or rec[2] > best[s][2]:
        best[s]=rec

for s in sorted(best):
    r=best[s]
    print(f"{s}\t{r[2]}\t{r[1]}\ttech={r[3]} interp={r[4]} fp={r[5]} template={r[6]} generic={r[7]}")
