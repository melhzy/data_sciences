import re
from pathlib import Path
base=Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/week06/submissions')
patterns={
 'uses_06_data': r'06_data\\.csv|import\("06_data|read\\.csv\("06_data|read_csv\("06_data|rio::import',
 'uses_random': r'runif\(|sample\(|rnorm\(|set\.seed\(',
 'mentions_chickflick': r'chickflick|festival|exam anxiety|jiminy'
}
for p in sorted(base.iterdir()):
    if not p.is_file():
        continue
    s=p.read_text(errors='ignore').lower()
    vals={k: bool(re.search(v,s)) for k,v in patterns.items()}
    print(f"{p.name}\t{vals}")
