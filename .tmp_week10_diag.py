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
    ext = path.suffix.lower()
    if ext in {'.html','.htm'}:
        return strip_html(path.read_text(encoding='utf-8', errors='ignore'))
    if ext == '.docx':
        return read_docx(path)
    return path.read_text(encoding='utf-8', errors='ignore')

for fp in sorted(sub_dir.iterdir()):
    if fp.is_dir():
        continue
    t = read_text(fp).lower()
    wc = len(re.findall(r"\b\w+\b", t))
    template = sum(1 for p in [r"fill in", r"don't change this", r"include the output", r"do you think you've met", r"run the anova", r"write up a results section"] if re.search(p,t))
    placeholders = sum(1 for p in [r"eta\s*=\s*12", r"\bna\b", r"\bna,\s*na\b", r"enter your name"] if re.search(p,t))
    interp = sum(1 for p in [r"this means",r"suggests",r"indicates",r"therefore",r"we conclude",r"in this study",r"higher than",r"lower than",r"because"] if re.search(p,t))
    outputs = sum(1 for p in [r"\[1\]", r"f\s*\([^\)]*\)\s*=", r"p\s*[<=>]\s*\.?\d", r"levene", r"bonferroni", r"eta", r"omega", r"cohen", r"trend", r"ggplot", r"error bar"] if re.search(p,t))
    print(f"{fp.name[:45]:45} wc={wc:5d} template={template} ph={placeholders} interp={interp} output={outputs}")
