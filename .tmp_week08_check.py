import re, zipfile
from pathlib import Path
base = Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/week08')
subs = base / 'submissions'

def read_docx(path):
    try:
        with zipfile.ZipFile(path,'r') as z:
            xml=z.read('word/document.xml').decode('utf-8',errors='ignore')
        xml=re.sub(r'</w:p>','\n',xml)
        xml=re.sub(r'<[^>]+>',' ',xml)
        return re.sub(r'\s+',' ',xml).lower()
    except Exception:
        return ''

def read_html(path):
    s=path.read_text(errors='ignore')
    s=re.sub(r'(?is)<script.*?</script>',' ',s)
    s=re.sub(r'(?is)<style.*?</style>',' ',s)
    s=re.sub(r'(?s)<[^>]+>',' ',s)
    return re.sub(r'\s+',' ',s).lower()

def txt(path):
    e=path.suffix.lower()
    if e in ['.html','.htm']: return read_html(path)
    if e=='.docx': return read_docx(path)
    if e=='.rmd': return path.read_text(errors='ignore').lower()
    return ''

def hr(t,p): return bool(re.search(p,t))
def ha(t,a): return any(x in t for x in a)

def hits(t):
    h={}
    h['data_import']=ha(t,['08_data.sav','read_sav','read.spss','rio::import','read.csv('])
    h['factor_type_work']=hr(t,r'factor\s*\(\s*.*type[_ ]?work|type[_ ]?work\s*<-\s*factor')
    h['leverage']=hr(t,r'leverage|hatvalues') and hr(t,r'cut\s*off|cutoff')
    h['cooks']=hr(t,r"cook'?s|cooks\.distance") and hr(t,r'cut\s*off|cutoff|4/n')
    h['mahal']=hr(t,r'mahalanobis|mahal') and hr(t,r'\bdf\b|degrees of freedom') and hr(t,r'qchisq|chi-?square|cut\s*off')
    h['overall_outliers']=hr(t,r'overall.*outlier|total outlier|delete them|remove outlier|filtered data|noout|clean')
    h['additivity']=hr(t,r'cor\(|correlation table|multicollinearity|vif')
    h['linearity']=hr(t,r'linearity|residuals|fitted|plot')
    h['normality']=hr(t,r'normality|qq|q-q|shapiro|hist')
    h['homog']=hr(t,r'homoscedastic|homogeneity|residuals.*fitted|plot')
    h['hierarchical_steps']=hr(t,r'hierarchical|step 1|model 1') and hr(t,r'years') and hr(t,r'type[_ ]?work') and hr(t,r'affective') and hr(t,r'cognitive')
    h['anova_change']=hr(t,r'anova\(|change between each step|r\^2 change|f[- ]change')
    h['mediation_paths']=hr(t,r'mediation|path a|path b|path c|indirect') and hr(t,r'years') and hr(t,r'affective') and hr(t,r'ocb')
    h['sobel']=hr(t,r'sobel')
    h['boot_indirect']=hr(t,r'boot|bootstrap|bootstrapped indirect')
    h['writeup']=sum(1 for p in [r'brief description|experiment|variables',r'data screening|assumption',r'f-?value',r'\bbeta\b|\bb\b',r'interpretation|dummy coding|study results'] if hr(t,p))>=3
    return h

for fn in [
    'suumemmanuelndone_38655_5166630_08 - Lab Regression_files.htlm.htm',
    'fuyunlong_30011_5139191_08_lab.html'
]:
    p=subs/fn
    t=txt(p)
    h=hits(t)
    missing=[k for k,v in h.items() if not v]
    print(fn)
    print('missing=',missing)
    print('len=',len(t))
    print('has_data=',ha(t,['08_data.sav','read_sav','read.spss','rio::import','read.csv(']))
