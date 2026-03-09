import csv
import re
from pathlib import Path
from pypdf import PdfReader

base = Path(r'd:/Github/data_sciences/ANLY699-Applied-Project/archive/final_Thesis')
subs = base / 'Submissions'
summary_out_subs = subs / 'final_thesis_grade.csv'
summary_out_root_fallback = base / 'final_thesis_grade_updated.csv'
detail_out = base / 'final_thesis_grade_detailed.csv'

files = [
    subs / 'altaherabdullahahmadadel_31728_5139942_699 Manuscript.pdf',
    subs / 'caothaiduong_30462_5168394_ANLY 699 Final Manuscript.pdf',
    subs / 'chungminung_33092_5168039_Final Project Presentation_Minung Chung-1.pdf',
    subs / 'kashyapsatwik_31318_5140320_Proposal - satwik kashyap - current - preprint-1.pdf',
    subs / 'ravalhiraldevdutt_31485_5171121_Interpretable Depression Detection Manuscript.pdf',
    subs / 'selvarajvikasini_30961_5166744_ANLY_699 Final Paper Pdf.pdf',
]

def extract(path):
    r = PdfReader(str(path))
    txt = ' '.join((p.extract_text() or '') for p in r.pages[:120])
    txt = re.sub(r'\s+', ' ', txt).strip().lower()
    return txt, len(r.pages)

def group_score(text, groups, pages):
    h = sum(1 for g in groups if any(k in text for k in g))
    ratio = h / len(groups)
    s = 18 if ratio >= .85 else (15 if ratio >= .60 else (12 if ratio >= .40 else (8 if ratio >= .20 else 4)))
    if pages >= 15:
        s += 2
    elif pages <= 4:
        s -= 3
    return max(0, min(20, s))

def level(text, keys):
    h = sum(1 for k in keys if k in text)
    return 4 if h >= 5 else (3 if h >= 3 else (2 if h >= 1 else 1))

summary_rows = []
detail_rows = []

for f in files:
    text, pages = extract(f)
    stem = f.stem.lower()
    stu = f.name.split('_')[0]

    s_intro = group_score(text, [['introduction'],['literature review','related work','background'],['problem statement','research gap','motivation'],['objective','aim']], pages)
    s_methods = group_score(text, [['hypothesis','research question','h0','h1'],['method','methodology','approach'],['dataset','data source','sample'],['model','algorithm','analysis'],['validation','evaluation']], pages)
    s_results = group_score(text, [['result','findings'],['table','figure'],['accuracy','auc','precision','recall','f1','rmse','mae'],['comparison','baseline']], pages)
    s_disc = group_score(text, [['discussion','interpretation'],['limitation','limitations'],['implication'],['future work','conclusion']], pages)
    s_format = group_score(text, [['abstract'],['reference','references','bibliography'],['apa','ieee'],['format','readability']], pages)

    thesis = s_intro + s_methods + s_results + s_disc + s_format

    type_adj = 0
    if 'presentation' in stem:
        type_adj -= 18
    if 'proposal' in stem and 'final' not in stem:
        type_adj -= 14
    if ('manuscript' in stem) or ('final paper' in stem):
        type_adj += 2

    loa_comm = level(text,['introduction','conclusion','transition','discussion','results'])
    loa_glob = level(text,['global','societal','community','bias','belief','values'])
    loa_hyp = level(text,['hypothesis','research question','null hypothesis','testable'])
    loa_write = level(text,['abstract','introduction','method','results','discussion','reference'])
    loa_avg = round((loa_comm + loa_glob + loa_hyp + loa_write) / 4, 2)
    loa_adj = 2 if loa_avg >= 3.5 else (1 if loa_avg >= 3.0 else (-2 if loa_avg < 2.0 else 0))

    grade = max(0, min(100, thesis + type_adj + loa_adj))

    weakest = min([
        ('Introduction/Lit', s_intro), ('Hypotheses/Methods', s_methods), ('Results', s_results),
        ('Discussion', s_disc), ('Abstract/Refs/Format', s_format)
    ], key=lambda x: x[1])
    strongest = max([
        ('Introduction/Lit', s_intro), ('Hypotheses/Methods', s_methods), ('Results', s_results),
        ('Discussion', s_disc), ('Abstract/Refs/Format', s_format)
    ], key=lambda x: x[1])

    action = 'expand full manuscript sections beyond proposal scope' if 'proposal' in stem else (
        'submit final manuscript format instead of presentation-only file' if 'presentation' in stem else (
            'tighten literature gap and improve depth of supporting scholarship' if weakest[0] == 'Introduction/Lit' else (
                'clarify methods-to-results linkage and statistical reporting' if weakest[0] in ['Hypotheses/Methods','Results'] else
                'improve discussion depth with limitations and implications')))

    comment = (
        f"{stu}: component profile [Intro={s_intro}, Methods={s_methods}, Results={s_results}, Discussion={s_disc}, Format={s_format}] out of 20 each. "
        f"Strongest area: {strongest[0]} ({strongest[1]}/20). Primary gap: {weakest[0]} ({weakest[1]}/20). "
        f"Priority revision: {action}."
    )

    summary_rows.append([stu, grade, comment])
    detail_rows.append([
        stu, pages, s_intro, s_methods, s_results, s_disc, s_format,
        thesis, loa_comm, loa_glob, loa_hyp, loa_write, loa_avg,
        type_adj, loa_adj, grade
    ])

for target in [summary_out_subs, summary_out_root_fallback]:
    with target.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
        w.writerow(['Name','Grade','Comments'])
        w.writerows(summary_rows)

with detail_out.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writerow([
        'Name','Pages','Intro_Lit_20','Hypotheses_Methods_20','Results_20','Discussion_20','Abstract_Ref_Format_20',
        'ThesisSubtotal_100','LOA_COMM_1_1_4','LOA_GLOB_0_1_4','LOA_ANMS_2_1_4','LOA_ANMS_6_3_4','LOA_Avg_4',
        'SubmissionTypeAdj','LOA_Adjustment','FinalGrade_100'
    ])
    w.writerows(detail_rows)

print(f'Wrote {summary_out_subs}')
print(f'Wrote {summary_out_root_fallback}')
print(f'Wrote {detail_out}')
