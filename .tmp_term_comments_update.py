import csv
from pathlib import Path

path = Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/term_final/term-final-grade.csv')

with path.open('r', encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
    fieldnames = rows[0].keys() if rows else []

for r in rows:
    name = r['Student']
    p = int(r['Proposal_20'])
    pr = int(r['Presentation_40'])
    fr = int(r['FinalReport_40'])
    total = int(r['Total_100'])
    slides = int(r['Presentation_Slides'])
    ph = int(r['Proposal_Criteria_Hits'])
    psh = int(r['Presentation_Criteria_Hits'])
    rh = int(r['Report_Criteria_Hits'])

    strong = []
    improve = []

    if p >= 18 and ph >= 5:
        strong.append('proposal clearly defines the project question, data need, and planned method')
    elif p >= 15:
        strong.append('proposal establishes a workable project direction')
    else:
        improve.append('proposal section needs clearer scope, methods, and evaluation details')

    if pr >= 34 and psh >= 7:
        strong.append('presentation communicates project workflow and progress effectively')
    elif pr >= 26:
        strong.append('presentation covers key progress points with acceptable structure')
    else:
        improve.append('presentation coverage is thin for a final-stage project update')

    if slides > 0 and slides < 10:
        improve.append(f'slide deck has {slides} slides and is below the 10-slide requirement')
    elif slides >= 10:
        strong.append(f'slide deck meets the 10-slide expectation ({slides} slides)')

    if fr >= 36 and rh >= 6:
        strong.append('final report includes strong technical structure and evaluation discussion')
    elif fr >= 30:
        strong.append('final report demonstrates core analysis and reporting elements')
    else:
        improve.append('final report needs stronger technical/evaluation depth and section completeness')

    if fr == 0:
        improve.append('final report deliverable appears missing or not gradable from submitted files')
    if pr == 0:
        improve.append('presentation deliverable appears missing or not gradable from submitted files')
    if p == 0:
        improve.append('proposal deliverable appears missing or not gradable from submitted files')

    tone = 'Very strong overall submission' if total >= 95 else ('Solid submission with good progress' if total >= 85 else ('Developing submission with mixed quality' if total >= 70 else 'Limited submission against course expectations'))

    # make comments individualized with name + mixed evidence
    strong_part = '; '.join(strong[:3]) if strong else 'limited evidence of complete rubric coverage'
    improve_part = '; '.join(improve[:3]) if improve else 'continue improving writing precision and reproducibility detail for graduate-level polish'

    r['Comments'] = f"{name}: {tone}. Strengths: {strong_part}. Next focus: {improve_part}."

with path.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writeheader()
    w.writerows(rows)

print(f'Updated individualized comments for {len(rows)} students in {path}')
