import re, zipfile
from pathlib import Path

root = Path(r"d:/Github/data_sciences/ANLY500-Analytics-I/archive/week10")
sub_dir = root / "submissions"

def strip_html(s):
    s = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s)

def read_docx(path):
    try:
        with zipfile.ZipFile(path, 'r') as zf:
            xml = zf.read('word/document.xml').decode('utf-8', errors='ignore')
        return re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", xml))
    except Exception:
        return ""

def read_text(path):
    if path.suffix.lower() in {'.html','.htm'}:
        return strip_html(path.read_text(encoding='utf-8', errors='ignore'))
    if path.suffix.lower()=='.docx':
        return read_docx(path)
    return path.read_text(encoding='utf-8', errors='ignore')

def has_any(t,p):
    return any(re.search(x,t) for x in p)

def cnt(t,p):
    return sum(1 for x in p if re.search(x,t))

for fp in sorted(sub_dir.iterdir()):
    if fp.is_dir():
        continue
    t=read_text(fp).lower()
    wc=len(re.findall(r"\b\w+\b",t))
    stu=fp.name.split('_')[0]
    interp=cnt(t,[r"this means",r"suggests",r"indicates",r"therefore",r"we conclude",r"compared to",r"higher than",r"lower than",r"because"])
    trend=has_any(t,[r"trend",r"polynomial",r"contrast",r"linear trend",r"quadratic"])
    graph=has_any(t,[r"ggplot",r"geom_bar",r"error bar",r"coord_cartesian",r"ylim"])
    table=has_any(t,[r"kable",r"tableprint",r"no correction p",r"bonferroni p",r"d value"])
    power=has_any(t,[r"power",r"sample size",r"pwr",r"uniroot",r"n\s*=\s*2"])
    fmt=fp.suffix.lower()
    print(f"{stu:24} fmt={fmt:5} wc={wc:4} interp={interp} trend={int(trend)} graph={int(graph)} table={int(table)} power={int(power)}")
