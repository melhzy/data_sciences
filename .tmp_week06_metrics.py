import re
from pathlib import Path
base=Path(r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/week06/submissions')
for p in sorted(base.iterdir()):
    if not p.is_file():
        continue
    s=p.read_text(errors='ignore')
    html_tags=len(re.findall(r'<[^>]+>',s))
    pre_blocks=len(re.findall(r'<pre',s,re.I))
    r_outputs=len(re.findall(r'##\s',s))
    code_fences=len(re.findall(r'```',s))
    sourcecode=len(re.findall(r'sourceCode|class="r"|class=\"r\"',s,re.I))
    print(f"{p.name}\thtml_tags={html_tags}\tpre={pre_blocks}\tr_out={r_outputs}\tfences={code_fences}\tsource={sourcecode}")
