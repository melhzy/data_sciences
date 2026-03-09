import csv
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from pypdf import PdfReader

base = Path(r'd:/Github/data_sciences/ANLY699-Applied-Project/archive/final_PPT')
subs = base / 'Submissions'
out_csv = base / 'final-ppt-grade.csv'
files = sorted([p for p in subs.iterdir() if p.is_file()])

def clean(t): return re.sub(r'\s+', ' ', (t or '')).strip().lower()

def extract_pdf(path):
    r = PdfReader(str(path)); return clean(' '.join((p.extract_text() or '') for p in r.pages[:120])), len(r.pages), 0

def extract_pptx(path):
    texts=[]; slides=0; pics=0
    with zipfile.ZipFile(path,'r') as z:
        sfs=sorted([n for n in z.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')]); slides=len(sfs)
        for sf in sfs:
            root=ET.fromstring(z.read(sf))
            for el in root.iter():
                tag=el.tag.lower()
                if tag.endswith('}t') and el.text: texts.append(el.text)
                if tag.endswith('}pic'): pics+=1
    return clean(' '.join(texts)), slides, pics

def hits(text, words): return sum(1 for w in words if w in text)

def infer_name(path: Path):
    n = path.stem
    if '_' in n:
        return n.split('_')[0]
    low = n.lower()
    if 'minung' in low and 'chung' in low:
        return 'chungminung'
    return n.replace('-', ' ').strip()

rows=[]
for f in files:
    ext=f.suffix.lower()
    txt, slides, pics = extract_pptx(f) if ext=='.pptx' else extract_pdf(f)

    content_hits = hits(txt,['problem','objective','motivation','dataset','data source','method','model','result','finding','conclusion','implication','future work'])
    content = 46 if content_hits>=10 else (40 if content_hits>=7 else (32 if content_hits>=4 else (24 if content_hits>=2 else 16)))

    sp = 19 if slides>=12 else (17 if 9<=slides<=11 else (14 if 6<=slides<=8 else (10 if 1<=slides<=5 else 8)))
    if pics >= max(2, slides//3): sp=min(20, sp+1)

    style_hits = hits(txt,['overview','agenda','summary','conclusion','because','therefore','insight','interpret'])
    density = len(txt.split())/max(slides,1)
    style = 18 if style_hits>=6 and density<=85 else (16 if style_hits>=4 and density<=110 else (13 if style_hits>=2 else 10))

    timing = 9 if 9<=slides<=13 else (7 if 7<=slides<=15 else (5 if slides>0 else 3))

    civc = 4 if hits(txt,['community','public','societal','stakeholder','impact'])>=4 else (3 if hits(txt,['community','public','societal','stakeholder','impact'])>=2 else (2 if hits(txt,['community','public','societal','stakeholder','impact'])>=1 else 1))
    entr = 4 if hits(txt,['action plan','roadmap','implementation plan','next steps'])>=3 else (3 if hits(txt,['action plan','roadmap','implementation plan','next steps'])>=2 else (2 if hits(txt,['action plan','roadmap','implementation plan','next steps'])>=1 else 1))
    anms_data = 4 if hits(txt,['ethical','privacy','bias','data quality','data collection'])>=3 else (3 if hits(txt,['ethical','privacy','bias','data quality','data collection'])>=2 else (2 if hits(txt,['ethical','privacy','bias','data quality','data collection'])>=1 else 1))
    anms_pres = 4 if style_hits>=6 else (3 if style_hits>=4 else (2 if style_hits>=2 else 1))
    loa_avg=(civc+entr+anms_data+anms_pres)/4
    loa_adj = 2 if loa_avg>=3.5 else (1 if loa_avg>=3.0 else (-2 if loa_avg<2.0 else 0))

    subtotal=content+sp+style+timing
    grade=max(0,min(100,subtotal+loa_adj))

    strengths=[]; weak=[]
    if content>=40: strengths.append('content coverage explains the project problem-method-results flow clearly')
    if sp>=17: strengths.append(f'slide structure is generally well organized for presentation ({slides} slides)')
    if style>=16: strengths.append('delivery style appears accessible and not overly technical')
    if timing>=9: strengths.append('estimated timing aligns well with a 10-minute target')

    if content<36: weak.append('strengthen the narrative on project implications and conclusion takeaways')
    if slides<9: weak.append(f'increase deck length/coverage (currently {slides} slides) for full 10-minute depth')
    if style<15: weak.append('improve terminology precision and transition flow between sections')
    if timing<7: weak.append('rebalance section pacing to fit the expected presentation timing')
    if not strengths: strengths=['submission shows partial alignment with presentation rubric elements']
    if not weak: weak=['add one slide on limitations and next-step action plan for stronger closure']

    name=infer_name(f)
    comment=(f"{name}: strengths - {strengths[0]}" + (f"; {strengths[1]}" if len(strengths)>1 else '') +
             f". improvement priorities - {weak[0]}" + (f"; {weak[1]}" if len(weak)>1 else '') +
             f". (Content={content}/50, Slides={sp}/20, Style={style}/20, Timing={timing}/10, LOA avg={loa_avg:.2f}/4, adj={loa_adj:+d})")

    rows.append([name,grade,comment])

with out_csv.open('w', encoding='utf-8-sig', newline='') as f:
    w=csv.writer(f,quoting=csv.QUOTE_ALL,lineterminator='\r\n'); w.writerow(['Name','Grade','Comments']); w.writerows(rows)

print(f'Updated {out_csv} with {len(rows)} records')
