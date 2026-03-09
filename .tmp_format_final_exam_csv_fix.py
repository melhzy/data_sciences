import csv
from pathlib import Path

file_path = Path(r"d:/Github/data_sciences/ANLY500-Analytics-I/archive/anly500_final/final_exam_grade.csv")

with file_path.open('r', encoding='utf-8', newline='') as f:
    raw = list(csv.reader(f))

if not raw:
    raise SystemExit('CSV is empty')

header = raw[0]
expected = ["Student","Grade","Q1","Q2","Q3","Q4","Comments"]

rows = []
for r in raw[1:]:
    if not r or all(not x.strip() for x in r):
        continue
    if len(r) < 7:
        r = r + [''] * (7 - len(r))
    elif len(r) > 7:
        r = r[:6] + [','.join(r[6:])]

    student, grade, q1, q2, q3, q4, comments = r
    c = comments.strip()
    if 'Improve:' in c:
        left, right = c.split('Improve:', 1)
        left = left.strip().rstrip('.')
        right = right.strip().rstrip('.')
        if left.startswith('Strengths:'):
            c = f"{left}. Final evaluation notes: {right}."
        else:
            c = f"Final evaluation notes: {c.rstrip('.')}.'"

    c = c.replace('submit missing question(s):', 'missing question(s):')
    c = c.replace('submit knitted Word/HTML format for', 'submitted format issue in')
    c = c.replace('use more original interpretation language in', 'interpretation depth was lighter in')
    c = c.replace('cover all rubric elements more explicitly in', 'rubric coverage was lighter in')

    rows.append([student, grade, q1, q2, q3, q4, c])

with file_path.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    writer.writerow(expected)
    writer.writerows(rows)

print(f"Reformatted for Excel: {file_path} ({len(rows)} rows)")
