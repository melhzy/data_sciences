import csv
from pathlib import Path

base = Path(r'd:/Github/data_sciences/ANLY699-Applied-Project/archive')
thesis = base / 'final_Thesis' / 'final_thesis_grade_updated.csv'
if not thesis.exists():
    thesis = base / 'final_Thesis' / 'Submissions' / 'final_thesis_grade.csv'
ppt = base / 'final_PPT' / 'final-ppt-grade.csv'
out = base / 'ANLY699_consolidated_gradebook.csv'

thesis_rows = {}
ppt_rows = {}

if thesis.exists():
    with thesis.open('r', encoding='utf-8-sig', newline='') as f:
        for r in csv.DictReader(f):
            thesis_rows[r['Name'].strip().lower()] = r

if ppt.exists():
    with ppt.open('r', encoding='utf-8-sig', newline='') as f:
        for r in csv.DictReader(f):
            ppt_rows[r['Name'].strip().lower()] = r

names = sorted(set(thesis_rows.keys()) | set(ppt_rows.keys()))

rows = []
for n in names:
    tr = thesis_rows.get(n)
    pr = ppt_rows.get(n)
    t = int(tr['Grade']) if tr and str(tr.get('Grade','')).strip().isdigit() else None
    p = int(pr['Grade']) if pr and str(pr.get('Grade','')).strip().isdigit() else None

    if t is not None and p is not None:
        avg = round((t + p) / 2, 1)
    elif t is not None:
        avg = float(t)
    elif p is not None:
        avg = float(p)
    else:
        avg = ''

    rows.append([
        n,
        '' if t is None else t,
        '' if p is None else p,
        avg,
        '' if not tr else tr.get('Comments',''),
        '' if not pr else pr.get('Comments','')
    ])

with out.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writerow(['Name','Thesis_Grade','PPT_Grade','Avg_Grade','Thesis_Comments','PPT_Comments'])
    w.writerows(rows)

print(f'Wrote {out} with {len(rows)} students')
