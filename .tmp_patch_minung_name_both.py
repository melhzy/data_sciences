import csv
from pathlib import Path

paths = [
    Path(r'd:/Github/data_sciences/ANLY699-Applied-Project/archive/final_PPT/final-ppt-grade.csv'),
    Path(r'd:/Github/data_sciences/ANLY699-Applied-Project/archive/final_PPT/final-ppt-grade-detailed.csv'),
]

for p in paths:
    with p.open('r', encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
        fields = rows[0].keys() if rows else []

    for r in rows:
        if r.get('Name', '').strip().lower() == 'final project presentation':
            r['Name'] = 'chungminung'
            if 'Comments' in r and isinstance(r['Comments'], str):
                r['Comments'] = r['Comments'].replace('Final Project Presentation:', 'chungminung:')

    with p.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
        w.writeheader()
        w.writerows(rows)

print('Patched Name field in summary and detailed PPT grade files')
