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


def keyword_count(text, words):
    return sum(1 for w in words if w in text)

proposal_terms = ['proposal', 'problem statement', 'research question', 'data needed', 'plan', 'timeline']
report_terms = ['introduction', 'related work', 'literature review', 'technical approach', 'evaluation', 'conclusion', 'future work']

proposal_criteria = [
    (2, ['problem statement', 'research question', 'objective']),
    (2, ['data source', 'dataset', 'data collection', 'data needed']),
    (2, ['algorithm', 'model', 'technique', 'methodology']),
    (2, ['evaluate', 'evaluation', 'metric', 'accuracy', 'f1', 'rmse']),
    (2, ['deliverable', 'expected', 'timeline', 'future work']),
    (1, ['apa', 'ieee', 'references'])
]
presentation_criteria = [
    (1.5, ['problem statement', 'research question', 'challenge']),
    (1.5, ['background', 'literature', 'related work']),
    (1.5, ['process', 'methodology', 'workflow']),
    (1.5, ['data source', 'dataset', 'data description']),
    (1.5, ['exploratory', 'eda', 'visualization']),
    (1.5, ['algorithm', 'model', 'technique', 'tool']),
    (1.5, ['result', 'test', 'validation', 'performance']),
    (1.5, ['challenge', 'limitation']),
    (1.5, ['completed', 'progress', 'done']),
    (1.5, ['remaining', 'next step', 'future work'])
]
report_criteria = [
    (2.5, ['introduction', 'motivation', 'problem statement']),
    (2.5, ['related work', 'literature review', 'background']),
    (2.5, ['data source', 'dataset', 'data description']),
    (2.5, ['technical approach', 'method', 'algorithm', 'model']),
    (2.5, ['test', 'evaluation', 'metric', 'performance']),
    (2.5, ['baseline', 'comparison', 'benchmark']),
    (2.5, ['conclusion', 'future work', 'limitation']),
    (2.5, ['reproduc', 'replicat', 'implementation details'])
]


def score_by_keywords(text: str, groups):
    pts = 0
    hits = 0
    for weight, words in groups:
        if any(w in text for w in words):
            pts += weight
            hits += 1
    return pts, hits


rows = []
for sd in sorted([d for d in SUBS.iterdir() if d.is_dir()], key=lambda p: p.name.lower()):
    files = [f for f in sd.rglob('*') if f.is_file()]

    artifacts = []
    ppt_slides = 0
    has_recording = False

    for f in files:
        ext = f.suffix.lower()
        extracted = extract_content(f)
        text = extracted[0] if isinstance(extracted, tuple) else extracted
        if isinstance(extracted, tuple):
            ppt_slides += extracted[1]
        if ext in {'.mp4', '.mov'}:
            has_recording = True
        artifacts.append({'path': f, 'name': norm_name(f), 'ext': ext, 'text': text, 'role': 'other'})

    # Pass 1 explicit role assignment
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

    # Pass 2 infer doc/pdf/html roles if unresolved
    unresolved = [a for a in artifacts if a['role'] == 'other' and a['ext'] in {'.docx', '.pdf', '.html'}]
    for a in unresolved:
        p_score = keyword_count(a['name'] + ' ' + a['text'], proposal_terms)
        r_score = keyword_count(a['name'] + ' ' + a['text'], report_terms)
        if p_score >= r_score and p_score >= 2:
            a['role'] = 'proposal'
        elif r_score > p_score and r_score >= 2:
            a['role'] = 'report'

    # Pass 3 fallback: if proposal/presentation exist and no report, assign longest unresolved doc/pdf/html as report
    roles = [a['role'] for a in artifacts]
    unresolved = [a for a in artifacts if a['role'] == 'other' and a['ext'] in {'.docx', '.pdf', '.html'}]
    if ('proposal' in roles) and ('presentation' in roles) and ('report' not in roles) and unresolved:
        cand = sorted(unresolved, key=lambda x: len(x['text']), reverse=True)[0]
        cand['role'] = 'report'

    # If no proposal and unresolved exists, assign most proposal-like one
    roles = [a['role'] for a in artifacts]
    unresolved = [a for a in artifacts if a['role'] == 'other' and a['ext'] in {'.docx', '.pdf', '.html'}]
    if ('proposal' not in roles) and unresolved:
        cand = sorted(unresolved, key=lambda x: keyword_count(x['name'] + ' ' + x['text'], proposal_terms), reverse=True)[0]
        cand['role'] = 'proposal'

    grouped = {'proposal': [], 'presentation': [], 'report': [], 'other': []}
    for a in artifacts:
        grouped[a['role']].append(a)

    prop_text = clean_text(' '.join(a['text'] for a in grouped['proposal']))
    pres_text = clean_text(' '.join(a['text'] for a in grouped['presentation']))
    rep_text = clean_text(' '.join(a['text'] for a in grouped['report']))

    if grouped['proposal']:
        prop_score = 9
        p_pts, p_hits = score_by_keywords(prop_text, proposal_criteria)
        prop_score += p_pts
        w = len(prop_text.split())
        prop_score += 2 if w >= 350 else (1 if w >= 200 else 0)
        prop_score = min(20, round(prop_score))
    else:
        p_hits = 0
        prop_score = 0

    if grouped['presentation']:
        pres_score = 15
        exts = {a['ext'] for a in grouped['presentation']}
        if '.pptx' in exts or '.ppt' in exts:
            pres_score += 5
        if has_recording:
            pres_score += 3
        pres_score += 4 if ppt_slides >= 10 else (2 if 6 <= ppt_slides < 10 else 0)
        prs_pts, prs_hits = score_by_keywords(pres_text, presentation_criteria)
        pres_score += prs_pts
        pres_score = min(40, round(pres_score))
    else:
        prs_hits = 0
        pres_score = 0

    if grouped['report']:
        rep_score = 14
        exts = {a['ext'] for a in grouped['report']}
        if '.pdf' in exts or '.docx' in exts:
            rep_score += 4
        r_pts, r_hits = score_by_keywords(rep_text, report_criteria)
        rep_score += r_pts
        if any(k in rep_text for k in ['reference', 'references', 'citation', 'bibliography']):
            rep_score += 2
        if any(k in rep_text for k in ['regression', 'classification', 'clustering', 'xgboost', 'random forest', 'neural network', 'anomaly']):
            rep_score += 2
        words = len(rep_text.split())
        rep_score += 2 if words >= 1800 else (-3 if words < 500 else 0)
        rep_score = max(0, min(40, round(rep_score)))
    else:
        r_hits = 0
        rep_score = 0

    total = prop_score + pres_score + rep_score

    missing = []
    if not grouped['proposal']:
        missing.append('proposal')
    if not grouped['presentation']:
        missing.append('presentation')
    if not grouped['report']:
        missing.append('final report')

    strengths = []
    if p_hits >= 4:
        strengths.append('proposal addresses core planning elements')
    if prs_hits >= 6:
        strengths.append('presentation covers most required project-status content')
    if r_hits >= 6:
        strengths.append('final report addresses major technical/reporting sections')
    if ppt_slides >= 10:
        strengths.append('presentation meets 10-slide minimum')

    issues = []
    if missing:
        issues.append('missing deliverable(s): ' + ', '.join(missing))
    if grouped['presentation'] and ppt_slides and ppt_slides < 10:
        issues.append(f'presentation has {ppt_slides} slides (below 10 minimum)')
    if grouped['report'] and r_hits < 5:
        issues.append('final report has limited evidence for required section coverage')
    if grouped['proposal'] and p_hits < 3:
        issues.append('proposal is missing several required planning details')

    comment = 'Strengths: ' + ('; '.join(strengths[:2]) if strengths else 'partial alignment with rubric requirements')
    if issues:
        comment += '. Priority improvements: ' + '; '.join(issues[:2]) + '.'

    rows.append([
        sd.name, prop_score, pres_score, rep_score, total, len(files), ppt_slides,
        p_hits, prs_hits, r_hits, comment
    ])

with OUT.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writerow([
        'Student','Proposal_20','Presentation_40','FinalReport_40','Total_100',
        'Files_Submitted','Presentation_Slides','Proposal_Criteria_Hits',
        'Presentation_Criteria_Hits','Report_Criteria_Hits','Comments'
    ])
    w.writerows(rows)

print(f'Wrote {OUT} with {len(rows)} students')
