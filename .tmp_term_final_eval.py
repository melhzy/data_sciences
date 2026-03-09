import csv
import re
from pathlib import Path

base = Path(r"d:/Github/data_sciences/ANLY500-Analytics-I/archive/term_final")
subs = base / "submissions"
out_csv = base / "term-final-grade.csv"


def classify_files(files):
    proposal = []
    presentation = []
    report = []
    code_artifacts = []

    for f in files:
        name = f.name.lower()
        ext = f.suffix.lower()

        is_proposal = 'proposal' in name or 'part 1' in name or 'project perposal' in name
        is_presentation = ext in {'.ppt', '.pptx'} or 'presentation' in name or ext in {'.mp4', '.mov'} or 'recording' in name
        is_report = (
            ('report' in name or 'final project' in name or 'part 3' in name or 'ieee' in name or 'project_formatted' in name)
            and ext in {'.docx', '.pdf', '.html'}
        ) or ('final' in name and ext in {'.docx', '.pdf'} and 'proposal' not in name)

        if ext in {'.rmd', '.ipynb', '.html', '.csv'} or 'code' in name:
            code_artifacts.append(f)

        if is_proposal:
            proposal.append(f)
        if is_presentation:
            presentation.append(f)
        if is_report:
            report.append(f)

    return proposal, presentation, report, code_artifacts


def score_proposal(files):
    if not files:
        return 0, 'missing'
    score = 14
    names = ' '.join(f.name.lower() for f in files)
    exts = {f.suffix.lower() for f in files}
    if any(e in {'.docx', '.pdf'} for e in exts):
        score += 3
    if 'proposal' in names and len(files) >= 1:
        score += 2
    if any('apa' in f.name.lower() or 'ieee' in f.name.lower() for f in files):
        score += 1
    return min(20, score), 'present'


def score_presentation(files):
    if not files:
        return 0, 'missing'
    score = 26
    exts = {f.suffix.lower() for f in files}
    names = ' '.join(f.name.lower() for f in files)
    if any(e in {'.pptx', '.ppt'} for e in exts):
        score += 6
    if any(e in {'.mp4', '.mov'} for e in exts):
        score += 4
    if 'final' in names or 'project' in names:
        score += 2
    if len(files) >= 2:
        score += 2
    return min(40, score), 'present'


def score_report(files, code_files):
    if not files:
        return 0, 'missing'
    score = 27
    exts = {f.suffix.lower() for f in files}
    names = ' '.join(f.name.lower() for f in files)

    if any(e in {'.docx', '.pdf'} for e in exts):
        score += 5
    if any('report' in f.name.lower() or 'final project' in f.name.lower() for f in files):
        score += 3
    if any('ieee' in f.name.lower() or 'apa' in f.name.lower() for f in files):
        score += 2
    if code_files:
        score += 3

    # penalty for proposal-only style file used as report
    if 'proposal' in names and not any('report' in f.name.lower() for f in files):
        score -= 4

    return max(0, min(40, score)), 'present'


rows = []
for student_dir in sorted([d for d in subs.iterdir() if d.is_dir()]):
    files = [f for f in student_dir.iterdir() if f.is_file()]
    proposal_files, presentation_files, report_files, code_files = classify_files(files)

    proposal_score, proposal_status = score_proposal(proposal_files)
    presentation_score, presentation_status = score_presentation(presentation_files)
    report_score, report_status = score_report(report_files, code_files)

    total = proposal_score + presentation_score + report_score

    missing = []
    if proposal_status == 'missing':
        missing.append('proposal')
    if presentation_status == 'missing':
        missing.append('presentation')
    if report_status == 'missing':
        missing.append('final report')

    strengths = []
    if proposal_score >= 17:
        strengths.append('proposal deliverable is complete')
    if presentation_score >= 34:
        strengths.append('presentation package is strong')
    if report_score >= 34:
        strengths.append('final report submission is strong')
    if code_files:
        strengths.append('supplementary code/materials were included')

    notes = []
    if missing:
        notes.append('missing deliverable(s): ' + ', '.join(missing))
    if proposal_score < 17 and proposal_status == 'present':
        notes.append('proposal package appears limited against full requirement scope')
    if presentation_score < 32 and presentation_status == 'present':
        notes.append('presentation evidence is lighter than expected for final stage')
    if report_score < 32 and report_status == 'present':
        notes.append('final report evidence/format appears weaker than expected')

    comment = 'Strengths: ' + ('; '.join(strengths[:2]) if strengths else 'partial project submission detected')
    if notes:
        comment += '. Final notes: ' + '; '.join(notes[:2]) + '.'

    rows.append([
        student_dir.name,
        proposal_score,
        presentation_score,
        report_score,
        total,
        len(files),
        len(code_files),
        comment
    ])

with out_csv.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writerow([
        'Student',
        'Proposal_20',
        'Presentation_40',
        'FinalReport_40',
        'Total_100',
        'Files_Submitted',
        'Code_or_Data_Artifacts',
        'Comments'
    ])
    w.writerows(rows)

print(f"Wrote {out_csv} with {len(rows)} students")
