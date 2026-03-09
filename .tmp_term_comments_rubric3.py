import csv
from pathlib import Path

path = Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/term_final/term-final-grade.csv')

with path.open('r', encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
    fieldnames = rows[0].keys() if rows else []

for r in rows:
    name = r['Student']
    p20 = int(r['Proposal_20'])
    pr40 = int(r['Presentation_40'])
    fr40 = int(r['FinalReport_40'])
    total = int(r['Total_100'])
    pp = int(r['Proposal_Pct'])
    prp = int(r['Presentation_Pct'])
    frp = int(r['FinalReport_Pct'])
    slides = int(r['Presentation_Slides'])

    comp_scores = {'proposal': p20/20, 'presentation': pr40/40, 'report': fr40/40}
    weakest = min(comp_scores, key=comp_scores.get)

    # tone
    if total >= 95:
        tone = 'Excellent overall performance'
    elif total >= 85:
        tone = 'Strong overall performance'
    elif total >= 70:
        tone = 'Satisfactory overall performance'
    else:
        tone = 'Performance is below expected graduate standard'

    # personalized strengths
    strengths = []
    if pp >= 90:
        strengths.append('proposal scope and planning are clearly articulated')
    elif pp >= 70:
        strengths.append('proposal shows a workable direction for the study')

    if prp >= 90:
        strengths.append('presentation communicates methods and progress with solid structure')
    elif prp >= 70:
        strengths.append('presentation captures key milestones and project flow')

    if frp >= 90:
        strengths.append('final report demonstrates strong technical depth and evaluation framing')
    elif frp >= 70:
        strengths.append('final report covers major sections with acceptable completeness')

    if slides >= 10:
        strengths.append(f'presentation length meets requirement ({slides} slides)')

    # personalized focus
    focus = []
    if weakest == 'proposal':
        focus.append('tighten problem framing, proposed methods, and evaluation metrics in the proposal')
    elif weakest == 'presentation':
        focus.append('improve presentation coherence by linking business problem, data, method, and findings on each section')
    else:
        focus.append('strengthen final report rigor with deeper validation, assumptions, and limitations discussion')

    if slides > 0 and slides < 10:
        focus.append(f'increase slide deck from {slides} to at least 10 slides')

    if fr40 == 0:
        focus.append('submit a clear final report artifact to enable full rubric evaluation')
    if pr40 == 0:
        focus.append('submit a gradable presentation artifact aligned with project requirements')
    if p20 == 0:
        focus.append('submit a complete proposal artifact with required planning elements')

    if frp < 70 and fr40 > 0:
        focus.append('add explicit sections for business value, tool rationale, and additional data-source strategy')

    if not strengths:
        strengths.append('available artifacts show partial rubric coverage')

    r['Comments'] = (
        f"{name}: {tone}. "
        f"Strengths: {strengths[0]}"
        + (f"; {strengths[1]}" if len(strengths) > 1 else '')
        + ". "
        f"Priority next steps: {focus[0]}"
        + (f"; {focus[1]}" if len(focus) > 1 else '')
        + "."
    )

with path.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writeheader()
    w.writerows(rows)

print(f'Updated individualized comments for {len(rows)} students in {path}')
