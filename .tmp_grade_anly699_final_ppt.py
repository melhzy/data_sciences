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


def clean(t: str) -> str:
    return re.sub(r'\s+', ' ', (t or '')).strip().lower()


def extract_pdf(path: Path):
    try:
        reader = PdfReader(str(path))
        text = ' '.join((p.extract_text() or '') for p in reader.pages[:120])
        pages = len(reader.pages)
        return clean(text), pages, 0
    except Exception:
        return '', 0, 0


def extract_pptx(path: Path):
    text_parts = []
    slides = 0
    pic_count = 0
    try:
        with zipfile.ZipFile(path, 'r') as z:
            slide_files = sorted([n for n in z.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')])
            slides = len(slide_files)
            for sf in slide_files:
                xml = z.read(sf)
                root = ET.fromstring(xml)
                for el in root.iter():
                    tag = el.tag.lower()
                    if tag.endswith('}t') and el.text:
                        text_parts.append(el.text)
                    if tag.endswith('}pic'):
                        pic_count += 1
        return clean(' '.join(text_parts)), slides, pic_count
    except Exception:
        return '', 0, 0


def keyword_hits(text, words):
    return sum(1 for w in words if w in text)

rows = []
for f in files:
    ext = f.suffix.lower()
    if ext == '.pptx':
        txt, slide_count, visuals = extract_pptx(f)
    elif ext == '.pdf':
        txt, slide_count, visuals = extract_pdf(f)
    else:
        txt, slide_count, visuals = '', 0, 0

    # Presentation rubric scoring
    content_terms = [
        'problem', 'objective', 'motivation', 'dataset', 'data source', 'method', 'model',
        'result', 'finding', 'conclusion', 'implication', 'future work'
    ]
    content_hits = keyword_hits(txt, content_terms)
    if content_hits >= 10:
        content = 46
    elif content_hits >= 7:
        content = 40
    elif content_hits >= 4:
        content = 32
    elif content_hits >= 2:
        content = 24
    else:
        content = 16

    # Slides rubric
    if slide_count >= 12:
        slide_points = 19
    elif 9 <= slide_count <= 11:
        slide_points = 17
    elif 6 <= slide_count <= 8:
        slide_points = 14
    elif 1 <= slide_count <= 5:
        slide_points = 10
    else:
        slide_points = 8

    if visuals >= max(2, slide_count // 3):
        slide_points = min(20, slide_points + 1)

    # Style rubric
    style_terms = ['overview', 'agenda', 'summary', 'conclusion', 'because', 'therefore', 'insight', 'interpret']
    style_hits = keyword_hits(txt, style_terms)
    text_density = len(txt.split()) / max(slide_count, 1)
    if style_hits >= 6 and text_density <= 85:
        style = 18
    elif style_hits >= 4 and text_density <= 110:
        style = 16
    elif style_hits >= 2:
        style = 13
    else:
        style = 10

    # Timing rubric (10 min target approximated by slide count and density)
    if 9 <= slide_count <= 13:
        timing = 9
    elif 7 <= slide_count <= 15:
        timing = 7
    elif slide_count > 0:
        timing = 5
    else:
        timing = 3

    # Learning Outcome rubric calibration
    civc = 4 if keyword_hits(txt, ['community', 'public', 'societal', 'stakeholder', 'impact']) >= 4 else (3 if keyword_hits(txt, ['community', 'public', 'societal', 'stakeholder', 'impact']) >= 2 else (2 if keyword_hits(txt, ['community', 'public', 'societal', 'stakeholder', 'impact']) >= 1 else 1))
    entr = 4 if keyword_hits(txt, ['action plan', 'roadmap', 'implementation plan', 'next steps']) >= 3 else (3 if keyword_hits(txt, ['action plan', 'roadmap', 'implementation plan', 'next steps']) >= 2 else (2 if keyword_hits(txt, ['action plan', 'roadmap', 'implementation plan', 'next steps']) >= 1 else 1))
    anms_data = 4 if keyword_hits(txt, ['ethical', 'privacy', 'bias', 'data quality', 'data collection']) >= 3 else (3 if keyword_hits(txt, ['ethical', 'privacy', 'bias', 'data quality', 'data collection']) >= 2 else (2 if keyword_hits(txt, ['ethical', 'privacy', 'bias', 'data quality', 'data collection']) >= 1 else 1))
    anms_pres = 4 if style_hits >= 6 else (3 if style_hits >= 4 else (2 if style_hits >= 2 else 1))
    loa_avg = (civc + entr + anms_data + anms_pres) / 4.0

    loa_adj = 2 if loa_avg >= 3.5 else (1 if loa_avg >= 3.0 else (-2 if loa_avg < 2.0 else 0))

    subtotal = content + slide_points + style + timing
    grade = max(0, min(100, subtotal + loa_adj))

    # individualized comments
    strengths = []
    if content >= 40:
        strengths.append('content coverage explains the project problem-method-results flow clearly')
    if slide_points >= 17:
        strengths.append(f'slide structure is generally well organized for presentation ({slide_count} slides)')
    if style >= 16:
        strengths.append('delivery style appears accessible and not overly technical')
    if timing >= 9:
        strengths.append('estimated timing aligns well with a 10-minute target')

    weaknesses = []
    if content < 36:
        weaknesses.append('strengthen the narrative on project implications and conclusion takeaways')
    if slide_count < 9:
        weaknesses.append(f'increase deck length/coverage (currently {slide_count} slides) for full 10-minute depth')
    if style < 15:
        weaknesses.append('improve terminology precision and transition flow between sections')
    if timing < 7:
        weaknesses.append('rebalance section pacing to fit the expected presentation timing')

    if not strengths:
        strengths.append('submission shows partial alignment with presentation rubric elements')
    if not weaknesses:
        weaknesses.append('add one slide on limitations and next-step action plan for stronger closure')

    name = f.name.split('_')[0] if '_' in f.name else f.stem
    comment = (
        f"{name}: strengths - {strengths[0]}"
        + (f"; {strengths[1]}" if len(strengths) > 1 else '')
        + f". improvement priorities - {weaknesses[0]}"
        + (f"; {weaknesses[1]}" if len(weaknesses) > 1 else '')
        + f". (Content={content}/50, Slides={slide_points}/20, Style={style}/20, Timing={timing}/10, LOA avg={loa_avg:.2f}/4, adj={loa_adj:+d})"
    )

    rows.append([name, grade, comment])

with out_csv.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writerow(['Name', 'Grade', 'Comments'])
    w.writerows(rows)

print(f'Wrote {out_csv} with {len(rows)} records')
