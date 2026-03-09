import csv
from pathlib import Path

file_path = Path(r"d:/Github/data_sciences/ANLY500-Analytics-I/archive/anly500_final/final_exam_grade.csv")

rows = []
with file_path.open('r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        c = (row.get('Comments') or '').strip()
        if 'Improve:' in c:
            left, right = c.split('Improve:', 1)
            left = left.strip().rstrip('.')
            right = right.strip().rstrip('.')
            if left.startswith('Strengths:'):
                c = f"{left}. Final evaluation notes: {right}."
            else:
                c = f"Final evaluation notes: {c.rstrip('.')}.'"
        # soften imperative phrasing for final exam context
        c = c.replace('submit missing question(s):', 'missing question(s):')
        c = c.replace('submit knitted Word/HTML format for', 'submitted format issue in')
        c = c.replace('use more original interpretation language in', 'interpretation depth was lighter in')
        c = c.replace('cover all rubric elements more explicitly in', 'rubric coverage was lighter in')
        row['Comments'] = c
        rows.append(row)

with file_path.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(
        f,
        fieldnames=fieldnames,
        quoting=csv.QUOTE_ALL,
        lineterminator='\r\n'
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"Reformatted {file_path} for Excel with UTF-8 BOM + quoted fields ({len(rows)} rows)")
