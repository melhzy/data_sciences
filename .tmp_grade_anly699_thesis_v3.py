import csv
import re
from pathlib import Path
from pypdf import PdfReader

files = [
    Path(r'd:/Github/data_sciences/ANLY699-Applied-Project/archive/final_Thesis/Submissions/altaherabdullahahmadadel_31728_5139942_699 Manuscript.pdf'),
    Path(r'd:/Github/data_sciences/ANLY699-Applied-Project/archive/final_Thesis/Submissions/caothaiduong_30462_5168394_ANLY 699 Final Manuscript.pdf'),
    Path(r'd:/Github/data_sciences/ANLY699-Applied-Project/archive/final_Thesis/Submissions/chungminung_33092_5168039_Final Project Presentation_Minung Chung-1.pdf'),
    Path(r'd:/Github/data_sciences/ANLY699-Applied-Project/archive/final_Thesis/Submissions/kashyapsatwik_31318_5140320_Proposal - satwik kashyap - current - preprint-1.pdf'),
    Path(r'd:/Github/data_sciences/ANLY699-Applied-Project/archive/final_Thesis/Submissions/ravalhiraldevdutt_31485_5171121_Interpretable Depression Detection Manuscript.pdf'),
    Path(r'd:/Github/data_sciences/ANLY699-Applied-Project/archive/final_Thesis/Submissions/selvarajvikasini_30961_5166744_ANLY_699 Final Paper Pdf.pdf'),
]
out_csv = Path(r'd:/Github/data_sciences/ANLY699-Applied-Project/archive/final_Thesis/Submissions/final_thesis_grade.csv')


def extract(path):
    r = PdfReader(str(path))
    txt = ' '.join((p.extract_text() or '') for p in r.pages[:120])
    txt = re.sub(r'\s+', ' ', txt).strip().lower()
    return txt, len(r.pages)


def group_score(text, groups, pages):
    h = sum(1 for g in groups if any(k in text for k in g))
    ratio = h / len(groups)
    s = 18 if ratio >= .85 else (15 if ratio >= .60 else (12 if ratio >= .40 else (8 if ratio >= .20 else 4)))
    if pages >= 15: s += 2
    elif pages <= 4: s -= 3
    return max(0,min(20,s)), h


def level(text, keys):
    h = sum(1 for k in keys if k in text)
    return 4 if h >=5 else (3 if h >=3 else (2 if h>=1 else 1))

rows=[]
for f in files:
    text,pages = extract(f)
    stem = f.stem.lower()
    stu = f.name.split('_')[0]

    intro = [['introduction'],['literature review','related work','background'],['problem statement','research gap','motivation'],['objective','aim']]
    methods = [['hypothesis','research question','h0','h1'],['method','methodology','approach'],['dataset','data source','sample'],['model','algorithm','analysis'],['validation','evaluation']]
    results = [['result','findings'],['table','figure'],['accuracy','auc','precision','recall','f1','rmse','mae'],['comparison','baseline']]
    discuss = [['discussion','interpretation'],['limitation','limitations'],['implication'],['future work','conclusion']]
    formatg = [['abstract'],['reference','references','bibliography'],['apa','ieee'],['format','readability']]

    s1,h1 = group_score(text,intro,pages)
    s2,h2 = group_score(text,methods,pages)
    s3,h3 = group_score(text,results,pages)
    s4,h4 = group_score(text,discuss,pages)
    s5,h5 = group_score(text,formatg,pages)
    thesis = s1+s2+s3+s4+s5

    type_adj = 0
    if 'presentation' in stem: type_adj -= 18
    if 'proposal' in stem and 'final' not in stem: type_adj -= 14
    if ('manuscript' in stem) or ('final paper' in stem): type_adj += 2

    loa = {
        'COMM 1.1 Organization': level(text,['introduction','conclusion','transition','discussion','results']),
        'GLOB 0.1 Self-Identity': level(text,['global','societal','community','bias','belief','values']),
        'ANMS 2.1 Hypothesis': level(text,['hypothesis','research question','null hypothesis','testable']),
        'ANMS 6.3 Report Writing': level(text,['abstract','introduction','method','results','discussion','reference'])
    }
    loa_avg = sum(loa.values())/4
    loa_adj = 2 if loa_avg>=3.5 else (1 if loa_avg>=3.0 else (-2 if loa_avg<2.0 else 0))

    grade = max(0,min(100,thesis+type_adj+loa_adj))

    weakest_component = min([
        ('Introduction/Lit',s1),('Hypotheses/Methods',s2),('Results',s3),('Discussion',s4),('Abstract/Refs/Format',s5)
    ], key=lambda x:x[1])
    strongest_component = max([
        ('Introduction/Lit',s1),('Hypotheses/Methods',s2),('Results',s3),('Discussion',s4),('Abstract/Refs/Format',s5)
    ], key=lambda x:x[1])

    weakest_loa = min(loa.items(), key=lambda x:x[1])

    action = 'expand full manuscript sections beyond proposal scope' if 'proposal' in stem else (
        'submit final manuscript format instead of presentation-only file' if 'presentation' in stem else (
            'tighten literature gap and improve depth of supporting scholarship' if weakest_component[0]=='Introduction/Lit' else (
            'clarify methods-to-results linkage and statistical reporting' if weakest_component[0] in ['Hypotheses/Methods','Results'] else
            'improve discussion depth with limitations and implications')))

    comment = (
        f"{stu}: component profile [Intro={s1}, Methods={s2}, Results={s3}, Discussion={s4}, Format={s5}] out of 20 each. "
        f"Strongest area: {strongest_component[0]} ({strongest_component[1]}/20). "
        f"Primary gap: {weakest_component[0]} ({weakest_component[1]}/20) and lowest learning-outcome signal in {weakest_loa[0]} (level {weakest_loa[1]}/4). "
        f"Priority revision: {action}."
    )

    rows.append([stu,grade,comment])

with out_csv.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f,quoting=csv.QUOTE_ALL,lineterminator='\r\n')
    w.writerow(['Name','Grade','Comments'])
    w.writerows(rows)

print(f'Updated {out_csv} with {len(rows)} individualized records')
