import re
from pathlib import Path
base=Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/week06/submissions')
for p in sorted(base.iterdir()):
    if not p.is_file():
        continue
    s=p.read_text(errors='ignore').lower()
    uses_data = bool(re.search(r'06_data\\.csv|read\\.csv\\(&quot;06_data|read\\.csv\\("06_data|import\\(&quot;06_data|import\\("06_data|rio::import', s))
    uses_random = bool(re.search(r'runif\\(|sample\\(|rnorm\\(', s))
    print(f"{p.name}\tuses_data={uses_data}\tuses_random={uses_random}")
