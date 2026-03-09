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


def extract(path: Path):
    try:
        r = PdfReader(str(path))
        pages = len(r.pages)
        text = ' '.join((p.extract_text() or '') for p in r.pages[:120])
        text = re.sub(r'\s+', ' ', text).lower().strip()
        return text, pages
    except Exception:
        return '', 0


def group_score(text, groups, pages):
    hits = sum(1 for g in groups if any(k in text for k in g))
    maxh = len(groups)
    ratio = hits / maxh if maxh else 0
    if ratio >= 0.85:
        s = 18
    elif ratio >= 0.60:
        s = 15
    elif ratio >= 0.40:
        s = 12
    elif ratio >= 0.20:
        s = 8
    else:
        s = 4
    if pages >= 15:
        s += 2
    elif pages <= 4:
        s -= 3
    return max(0, min(20, s)), hits, maxh


def loa_level(text, keys):
    h = sum(1 for k in keys if k in text)
    if h >= 5: return 4
    if h >= 3: return 3
    if h >= 1: return 2
    return 1

rows = []
for f in files:
    text, pages = extract(f)
    stem = f.stem.lower()
    name = f.name.split('_')[0]

    intro_keys = [
        ['introduction'], ['literature review', 'related work', 'background'],
        ['problem statement', 'research gap', 'motivation'], ['objective', 'aim']
    ]
    meth_keys = [
        ['hypothesis', 'research question', 'h0', 'h1'], ['method', 'methodology', 'approach'],
        ['dataset', 'data source', 'sample'], ['model', 'algorithm', 'analysis'], ['validation', 'evaluation']
    ]
    res_keys = [
        ['result', 'findings'], ['table', 'figure'], ['accuracy', 'auc', 'precision', 'recall', 'f1', 'rmse', 'mae'],
        ['comparison', 'baseline']
    ]
    dis_keys = [
        ['discussion', 'interpretation'], ['limitation', 'limitations'], ['implication'], ['future work', 'conclusion']
    ]
    fmt_keys = [
        ['abstract'], ['reference', 'references', 'bibliography'], ['apa', 'ieee'], ['grammar', 'format', 'readability']
    ]

    s_intro, h_intro, m_intro = group_score(text, intro_keys, pages)
    s_meth, h_meth, m_meth = group_score(text, meth_keys, pages)
    s_res, h_res, m_res = group_score(text, res_keys, pages)
    s_dis, h_dis, m_dis = group_score(text, dis_keys, pages)
    s_fmt, h_fmt, m_fmt = group_score(text, fmt_keys, pages)

    thesis_total = s_intro + s_meth + s_res + s_dis + s_fmt

    # submission type penalties/bonuses (master thesis expectation)
    type_adj = 0
    if 'presentation' in stem:
        type_adj -= 18
    if 'proposal' in stem and 'final' not in stem:
        type_adj -= 14
    if 'manuscript' in stem or 'final paper' in stem:
        type_adj += 2

    # LOA rubric integration
    comm = loa_level(text, ['introduction','conclusion','transition','discussion','results'])
    glob = loa_level(text, ['global','societal','community','bias','value','belief'])
    hyp = loa_level(text, ['hypothesis','research question','null hypothesis','testable'])
    write = loa_level(text, ['abstract','introduction','method','results','discussion','reference'])
    loa_avg = (comm + glob + hyp + write) / 4.0
    loa_adj = 2 if loa_avg >= 3.5 else (1 if loa_avg >= 3.0 else (-2 if loa_avg < 2.0 else 0))

    total = max(0, min(100, thesis_total + type_adj + loa_adj))

    components = [
        ('Introduction/Literature Review', s_intro),
        ('Hypotheses/Methods', s_meth),
        ('Results', s_res),
        ('Discussion', s_dis),
        ('Abstract/References/Formatting', s_fmt),
    ]
    best = max(components, key=lambda x: x[1])
    worst = min(components, key=lambda x: x[1])

    specific = []
    if worst[0] == 'Results':
        specific.append('report clearer quantitative outputs (metrics/tables/figures) and baseline comparisons')
    elif worst[0] == 'Discussion':
        specific.append('deepen interpretation of findings, practical implications, and study limitations')
    elif worst[0] == 'Hypotheses/Methods':
        specific.append('state testable hypotheses/research questions explicitly and tighten method-validation alignment')
    elif worst[0] == 'Introduction/Literature Review':
        specific.append('strengthen literature synthesis and articulate a sharper research gap')
    else:
        specific.append('improve abstract clarity, citation completeness, and formatting consistency')

    if 'presentation' in stem:
        specific.append('submit a full thesis manuscript (not slide deck only) for fair thesis-criteria scoring')
    if 'proposal' in stem and 'final' not in stem:
        specific.append('submit completed final thesis sections beyond proposal-stage scope')
    if pages and pages < 8:
        specific.append(f'expand manuscript depth; current length ({pages} pages) is limited for final thesis expectations')

    strength_msg = f"strongest area: {best[0]} ({best[1]}/20)"
    weak_msg = f"primary gap: {worst[0]} ({worst[1]}/20)"

    comment = (
        f"{name}: {strength_msg}; {weak_msg}. "
        f"Priority improvements: {specific[0]}"
        + (f"; {specific[1]}" if len(specific) > 1 else '')
        + f". (Thesis={thesis_total}/100, SubmissionTypeAdj={type_adj:+d}, LOA avg={loa_avg:.2f}/4, LOA adj={loa_adj:+d})"
    )

    rows.append([name, total, comment])

with out_csv.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writerow(['Name', 'Grade', 'Comments'])
    w.writerows(rows)

print(f'Wrote {out_csv} with {len(rows)} students')
