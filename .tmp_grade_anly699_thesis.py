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


def extract_text(path: Path) -> str:
    try:
        reader = PdfReader(str(path))
        chunks = []
        for p in reader.pages[:120]:
            chunks.append(p.extract_text() or '')
        txt = ' '.join(chunks)
        txt = re.sub(r'\s+', ' ', txt).strip().lower()
        return txt
    except Exception:
        return ''


def hits(text: str, keys):
    return sum(1 for k in keys if k in text)


def score_20_by_presence(text: str, key_groups, page_count):
    group_hits = sum(1 for grp in key_groups if any(k in text for k in grp))
    if group_hits >= max(4, len(key_groups)-1):
        base = 18
    elif group_hits >= max(3, len(key_groups)//2):
        base = 15
    elif group_hits >= 2:
        base = 11
    elif group_hits >= 1:
        base = 7
    else:
        base = 3

    if page_count >= 10:
        base += 2
    elif page_count <= 3:
        base -= 2

    return max(0, min(20, base)), group_hits


def loa_level_1_to_4(text, criterion):
    if criterion == 'COMM_1_1':
        keys = ['introduction', 'conclusion', 'transition', 'method', 'results', 'discussion']
        h = hits(text, keys)
    elif criterion == 'GLOB_0_1':
        keys = ['global', 'bias', 'belief', 'values', 'culture', 'ethic', 'societal', 'community']
        h = hits(text, keys)
    elif criterion == 'ANMS_2_1':
        keys = ['hypothesis', 'h0', 'h1', 'research question', 'testable', 'null hypothesis']
        h = hits(text, keys)
    else:  # ANMS_6_3
        keys = ['abstract', 'introduction', 'method', 'results', 'discussion', 'reference']
        h = hits(text, keys)

    if h >= 5:
        return 4
    if h >= 3:
        return 3
    if h >= 2:
        return 2
    return 1


rows = []
for f in files:
    if not f.exists():
        rows.append([f.stem, 0, f"File not found: {f.name}"])
        continue

    text = extract_text(f)
    try:
        n_pages = len(PdfReader(str(f)).pages)
    except Exception:
        n_pages = 0

    # Thesis rubric criteria (5 x 20)
    intro_lit_keys = [
        ['introduction'], ['literature review', 'related work', 'background'],
        ['problem statement', 'motivation', 'gap'], ['objective', 'aim']
    ]
    hyp_methods_keys = [
        ['hypothesis', 'research question'], ['method', 'methodology', 'approach'],
        ['data', 'dataset', 'sample'], ['analysis', 'model', 'algorithm']
    ]
    results_keys = [
        ['results', 'findings'], ['table', 'figure', 'chart'], ['accuracy', 'auc', 'rmse', 'f1', 'metric']
    ]
    discussion_keys = [
        ['discussion', 'interpretation'], ['limitation', 'limitations'], ['future work', 'implication', 'conclusion']
    ]
    abstract_ref_format_keys = [
        ['abstract'], ['reference', 'references', 'bibliography'], ['apa', 'ieee'], ['readability', 'format']
    ]

    s_intro, h_intro = score_20_by_presence(text, intro_lit_keys, n_pages)
    s_methods, h_methods = score_20_by_presence(text, hyp_methods_keys, n_pages)
    s_results, h_results = score_20_by_presence(text, results_keys, n_pages)
    s_disc, h_disc = score_20_by_presence(text, discussion_keys, n_pages)
    s_format, h_format = score_20_by_presence(text, abstract_ref_format_keys, n_pages)

    thesis_total = s_intro + s_methods + s_results + s_disc + s_format

    # Learning outcome rubric calibration (4 criteria, 1-4 scale)
    l_comm = loa_level_1_to_4(text, 'COMM_1_1')
    l_glob = loa_level_1_to_4(text, 'GLOB_0_1')
    l_hyp = loa_level_1_to_4(text, 'ANMS_2_1')
    l_write = loa_level_1_to_4(text, 'ANMS_6_3')
    loa_avg = (l_comm + l_glob + l_hyp + l_write) / 4.0

    # small bounded adjustment to ensure both rubrics are used
    if loa_avg >= 3.5:
        adj = 3
    elif loa_avg >= 3.0:
        adj = 1
    elif loa_avg < 2.0:
        adj = -4
    elif loa_avg < 2.5:
        adj = -2
    else:
        adj = 0

    total = max(0, min(100, thesis_total + adj))

    # individualized comments
    strengths = []
    if s_intro >= 16:
        strengths.append('strong framing of research context and literature')
    if s_methods >= 16:
        strengths.append('clear hypothesis/research-method alignment')
    if s_results >= 16:
        strengths.append('results are reported with visible analytic evidence')
    if s_disc >= 16:
        strengths.append('discussion links findings, limitations, and implications')
    if s_format >= 16:
        strengths.append('document structure and references are generally well-formed')

    weak_areas = [
        ('Introduction/Literature Review', s_intro),
        ('Hypotheses/Methods', s_methods),
        ('Results', s_results),
        ('Discussion', s_disc),
        ('Abstract/References/Formatting', s_format),
    ]
    weak_areas.sort(key=lambda x: x[1])

    improve_msgs = []
    for area, score in weak_areas[:2]:
        if score <= 12:
            if area == 'Introduction/Literature Review':
                improve_msgs.append('deepen the literature synthesis and sharpen the research gap statement')
            elif area == 'Hypotheses/Methods':
                improve_msgs.append('state testable hypotheses/research questions more explicitly and justify method choices')
            elif area == 'Results':
                improve_msgs.append('expand quantitative result reporting with clearer metrics, tables, or comparative outputs')
            elif area == 'Discussion':
                improve_msgs.append('strengthen interpretation, limitations, and practical implications of findings')
            else:
                improve_msgs.append('improve abstract clarity, reference quality, and formatting consistency')

    if n_pages <= 5:
        improve_msgs.append(f'submission length ({n_pages} pages) appears short for a full master-level thesis manuscript')

    if not strengths:
        strengths = ['partial alignment with thesis rubric elements']
    if not improve_msgs:
        improve_msgs = ['continue tightening academic writing precision and methodological transparency']

    student_name = f.name.split('_')[0]
    comment = (
        f"{student_name}: "
        f"Strengths - {strengths[0]}"
        + (f"; {strengths[1]}" if len(strengths) > 1 else '')
        + f". Improvement priorities - {improve_msgs[0]}"
        + (f"; {improve_msgs[1]}" if len(improve_msgs) > 1 else '')
        + f". (Thesis criteria total={thesis_total}/100, LOA avg={loa_avg:.2f}/4, adjustment={adj:+d})"
    )

    rows.append([student_name, total, comment])

with out_csv.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writerow(['Name', 'Grade', 'Comments'])
    w.writerows(rows)

print(f'Wrote {out_csv} with {len(rows)} records')
