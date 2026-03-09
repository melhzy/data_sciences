import csv
from pathlib import Path
p = Path(r'd:/Github/data_sciences/ANLY699-Applied-Project/archive/final_PPT/final-ppt-grade.csv')
rows=[]
with p.open('r', encoding='utf-8-sig', newline='') as f:
    r=csv.DictReader(f)
    fns=r.fieldnames
    for row in r:
        if row['Name'].strip().lower() == 'final project presentation':
            row['Name'] = 'chungminung'
            row['Comments'] = row['Comments'].replace('Final Project Presentation:', 'chungminung:')
        rows.append(row)
with p.open('w', encoding='utf-8-sig', newline='') as f:
    w=csv.DictWriter(f, fieldnames=fns, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writeheader(); w.writerows(rows)
print('Patched name mapping for Minung Chung')
