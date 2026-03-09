import csv
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from html import unescape

try:
    from pypdf import PdfReader
except Exception:
    PdfReader = None

BASE = Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/term_final')
SUBS = BASE / 'submissions'
OUT = BASE / 'term-final-grade.csv'


def clean_text(text: str) -> str:
    text = unescape(text or '')
    text = re.sub(r'\s+', ' ', text)
    return text.strip().lower()


def norm_name(path: Path) -> str:
    return clean_text(path.name.replace('_', ' ').replace('-', ' '))


def extract_docx_text(path: Path) -> str:
    try:
        with zipfile.ZipFile(path, 'r') as z:
            xml = z.read('word/document.xml')
        root = ET.fromstring(xml)
        texts = [el.text for el in root.iter() if el.tag.endswith('}t') and el.text]
        return clean_text(' '.join(texts))
    except Exception:
        return ''


def extract_pptx_text_and_slides(path: Path):
    try:
        with zipfile.ZipFile(path, 'r') as z:
            slide_files = sorted([n for n in z.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')])
            texts = []
            for sf in slide_files:
                root = ET.fromstring(z.read(sf))
                chunks = [el.text for el in root.iter() if el.tag.endswith('}t') and el.text]
                texts.append(' '.join(chunks))
        return clean_text(' '.join(texts)), len(slide_files)
    except Exception:
        return '', 0


def extract_pdf_text(path: Path) -> str:
    if PdfReader is None:
        return ''
    try:
        reader = PdfReader(str(path))
        chunks = []
        for page in reader.pages[:40]:
            chunks.append(page.extract_text() or '')
        return clean_text(' '.join(chunks))
    except Exception:
        return ''


def extract_html_text(path: Path) -> str:
    try:
        txt = path.read_text(encoding='utf-8', errors='ignore')
        txt = re.sub(r'<script.*?>.*?</script>', ' ', txt, flags=re.S|re.I)
        txt = re.sub(r'<style.*?>.*?</style>', ' ', txt, flags=re.S|re.I)
        txt = re.sub(r'<[^>]+>', ' ', txt)
        return clean_text(txt)
    except Exception:
        return ''


def extract_ipynb_text(path: Path) -> str:
    try:
        nb = json.loads(path.read_text(encoding='utf-8', errors='ignore'))
        chunks = []
        for c in nb.get('cells', []):
            src = c.get('source', [])
            chunks.append(' '.join(src) if isinstance(src, list) else str(src))
        return clean_text(' '.join(chunks))
    except Exception:
        return ''


def extract_plain_text(path: Path) -> str:
    try:
        return clean_text(path.read_text(encoding='utf-8', errors='ignore'))
    except Exception:
        return ''


def extract_content(path: Path):
    ext = path.suffix.lower()
    if ext == '.docx':
        return extract_docx_text(path)
    if ext == '.pptx':
        return extract_pptx_text_and_slides(path)
    if ext == '.pdf':
        return extract_pdf_text(path)
    if ext == '.html':
        return extract_html_text(path)
    if ext == '.ipynb':
        return extract_ipynb_text(path)
    if ext in {'.rmd', '.r', '.txt', '.md', '.csv'}:
        return extract_plain_text(path)
    return ''


def keyword_hits(text: str, words):
    return sum(1 for w in words if w in text)


def level_from_hits(hits, hi=4, mid=2, low=1):
    if hits >= hi:
        return 100
    if hits >= mid:
        return 90
    if hits >= low:
        return 70
    return 0


def pct_to_component(pct, weight):
    return round((pct / 100.0) * weight)

# Rubric 2 critical elements (weights 25/25/25/15/10)
critical_elements = [
    ("DataSourceBusinessValue", 25, ['data source', 'dataset', 'business value', 'organization', 'stakeholder', 'impact']),
    ("Application", 25, ['methodology', 'process', 'execution', 'pipeline', 'workflow', 'implementation']),
    ("AnalyticStructureSelection", 25, ['model selection', 'analytic structure', 'algorithm', 'approach', 'justif', 'defend']),
    ("ToolSelection", 15, ['tool', 'python', 'r ', 'power bi', 'tableau', 'sql', 'comparison', 'why this tool']),
    ("AdditionalDataSources", 10, ['additional data', 'external data', 'internal data', 'augment', 'supplementary source'])
]

# Rubric 3 competencies (mapped for comments + mild scoring modulation)
competencies = {
    'COMM_1_2': ['audience', 'clear', 'communication', 'presentation', 'language', 'storytelling'],
    'ANMS_2_4': ['validate', 'validation', 'assumption', 'limitation', 'robust', 'sensitivity'],
    'ANMS_3_2': ['missing', 'outlier', 'assumption', 'data quality', 'accuracy', 'screening'],
    'ANMS_6_3': ['grammar', 'conclusion', 'references', 'guideline', 'structure', 'introduction'],
    'GLOB_0_2a': ['consequence', 'impact', 'local', 'broader', 'societal', 'ethical'],
    'CIVC_0_1': ['civic', 'policy', 'government', 'public', 'community']
}

rows = []

for sd in sorted([d for d in SUBS.iterdir() if d.is_dir()], key=lambda p: p.name.lower()):
    files = [f for f in sd.rglob('*') if f.is_file()]
    artifacts = []
    slides = 0
    has_recording = False

    for f in files:
        ext = f.suffix.lower()
        extracted = extract_content(f)
        text = extracted[0] if isinstance(extracted, tuple) else extracted
        if isinstance(extracted, tuple):
            slides += extracted[1]
        if ext in {'.mp4', '.mov'}:
            has_recording = True
        artifacts.append({'path': f, 'name': norm_name(f), 'ext': ext, 'text': text, 'role': 'other'})

    # role assignment
    for a in artifacts:
        n = a['name']
        if a['ext'] in {'.ppt', '.pptx'} or 'presentation' in n or 'part 2' in n:
            a['role'] = 'presentation'
        elif a['ext'] in {'.mp4', '.mov'}:
            a['role'] = 'presentation'
        elif 'proposal' in n or 'part 1' in n or 'perposal' in n:
            a['role'] = 'proposal'
        elif 'final project' in n or 'final report' in n or 'part 3' in n or 'report' in n:
            a['role'] = 'report'

    unresolved = [a for a in artifacts if a['role'] == 'other' and a['ext'] in {'.docx', '.pdf', '.html'}]
    for a in unresolved:
        nm = a['name'] + ' ' + a['text']
        pscore = keyword_hits(nm, ['proposal', 'plan', 'objective', 'data needed'])
        rscore = keyword_hits(nm, ['introduction', 'related work', 'evaluation', 'conclusion', 'final'])
        if pscore >= rscore and pscore >= 2:
            a['role'] = 'proposal'
        elif rscore > pscore and rscore >= 2:
            a['role'] = 'report'

    roles = [a['role'] for a in artifacts]
    unresolved = [a for a in artifacts if a['role'] == 'other' and a['ext'] in {'.docx', '.pdf', '.html'}]
    if ('proposal' in roles) and ('presentation' in roles) and ('report' not in roles) and unresolved:
        sorted_by_len = sorted(unresolved, key=lambda x: len(x['text']), reverse=True)
        sorted_by_len[0]['role'] = 'report'

    grouped = {'proposal': [], 'presentation': [], 'report': [], 'other': []}
    for a in artifacts:
        grouped[a['role']].append(a)

    prop_text = clean_text(' '.join(a['text'] for a in grouped['proposal']))
    pres_text = clean_text(' '.join(a['text'] for a in grouped['presentation']))
    rep_text = clean_text(' '.join(a['text'] for a in grouped['report']))
    all_text = clean_text(prop_text + ' ' + pres_text + ' ' + rep_text)

    # Proposal percentage (0/70/90/100 style using evidence for required items)
    proposal_hits = keyword_hits(prop_text, [
        'problem statement', 'research question', 'data', 'dataset', 'plan', 'method',
        'algorithm', 'model', 'evaluate', 'metric', 'deliverable', 'timeline', 'apa', 'ieee'
    ])
    prop_pct = 0
    if grouped['proposal']:
        prop_pct = level_from_hits(proposal_hits, hi=7, mid=4, low=2)

    # Presentation percentage (0/70/90/100 style + slide requirement)
    pres_hits = keyword_hits(pres_text, [
        'problem', 'background', 'literature', 'process', 'workflow', 'data source', 'eda',
        'model', 'result', 'challenge', 'completed', 'remaining', 'next step'
    ])
    pres_pct = 0
    if grouped['presentation']:
        pres_pct = level_from_hits(pres_hits, hi=8, mid=5, low=2)
        if slides >= 10:
            pres_pct = min(100, pres_pct + 5)
        elif 1 <= slides < 10:
            pres_pct = max(70, pres_pct - 5)
        if has_recording:
            pres_pct = min(100, pres_pct + 3)

    # Final report percentage based on Rubric 2 critical elements
    report_pct = 0
    ce_levels = {}
    if grouped['report']:
        weighted_sum = 0
        for ce_name, weight, keys in critical_elements:
            hits = keyword_hits(rep_text, keys)
            lvl = level_from_hits(hits, hi=4, mid=2, low=1)
            ce_levels[ce_name] = lvl
            weighted_sum += (lvl / 100.0) * weight
        report_pct = round(weighted_sum)

    # Rubric 3 competency evidence (used for refinement + comments)
    comp_scores = {}
    for comp, keys in competencies.items():
        h = keyword_hits(all_text, keys)
        if h >= 4:
            comp_scores[comp] = 4
        elif h >= 2:
            comp_scores[comp] = 3
        elif h >= 1:
            comp_scores[comp] = 2
        else:
            comp_scores[comp] = 1

    avg_comp = sum(comp_scores.values()) / len(comp_scores)
    # gentle adjustment to keep rubric-1 weights primary
    adjust = 0
    if avg_comp >= 3.5:
        adjust = 2
    elif avg_comp < 2.0:
        adjust = -3

    # Convert to weighted component points (Rubric 1)
    proposal_20 = pct_to_component(prop_pct, 20)
    presentation_40 = pct_to_component(pres_pct, 40)
    finalreport_40 = pct_to_component(report_pct, 40)

    total = proposal_20 + presentation_40 + finalreport_40 + adjust
    total = max(0, min(100, total))

    missing = []
    if not grouped['proposal']:
        missing.append('proposal')
    if not grouped['presentation']:
        missing.append('presentation')
    if not grouped['report']:
        missing.append('final report')

    strengths = []
    if proposal_20 >= 18:
        strengths.append('proposal aligns well with planning requirements')
    if presentation_40 >= 34:
        strengths.append('presentation communicates methodology and project progress clearly')
    if finalreport_40 >= 34:
        strengths.append('final report covers key technical/reporting expectations')
    if ce_levels.get('ToolSelection', 0) >= 90:
        strengths.append('tool selection is justified with strong analytic relevance')

    improvements = []
    if missing:
        improvements.append('missing deliverable(s): ' + ', '.join(missing))
    if slides and slides < 10:
        improvements.append(f'presentation has {slides} slides (minimum is 10)')
    if ce_levels.get('AdditionalDataSources', 0) <= 70 and grouped['report']:
        improvements.append('expand discussion of additional internal/external data sources and their value')
    if comp_scores['ANMS_2_4'] <= 2:
        improvements.append('add clearer model validation, assumptions, and limitation analysis')
    if comp_scores['ANMS_6_3'] <= 2:
        improvements.append('improve report writing quality and section completeness for graduate-level standards')

    tone = 'Excellent' if total >= 95 else ('Strong' if total >= 85 else ('Satisfactory' if total >= 70 else 'Needs significant improvement'))
    c1 = strengths[0] if strengths else 'partial alignment with rubric criteria'
    c2 = strengths[1] if len(strengths) > 1 else 'core deliverables are present but uneven in depth'
    n1 = improvements[0] if improvements else 'tighten methodological justification and reproducibility details'
    n2 = improvements[1] if len(improvements) > 1 else 'increase explicit linkage between business value and analytic choices'

    comment = f"{sd.name}: {tone} performance under the ANLY500 final project rubric. Strengths: {c1}; {c2}. Next steps: {n1}; {n2}."

    rows.append([
        sd.name,
        proposal_20,
        presentation_40,
        finalreport_40,
        total,
        prop_pct,
        pres_pct,
        report_pct,
        round(avg_comp, 2),
        slides,
        comment
    ])

with OUT.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writerow([
        'Student','Proposal_20','Presentation_40','FinalReport_40','Total_100',
        'Proposal_Pct','Presentation_Pct','FinalReport_Pct','Competency_Avg_4pt',
        'Presentation_Slides','Comments'
    ])
    w.writerows(rows)

print(f'Re-evaluated and wrote {OUT} with {len(rows)} students')
