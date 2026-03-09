import re, csv, zipfile
from pathlib import Path

root = Path(r"d:/Github/data_sciences/ANLY500-Analytics-I/archive/week10")
sub_dir = root / "submissions"
out_csv = root / "week10-grade.csv"


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
    try:
        if ext in {'.html','.htm'}:
            return strip_html(path.read_text(encoding='utf-8', errors='ignore'))
        if ext == '.docx':
            return read_docx(path)
        return path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return ""

def has_any(t, pats):
    return any(re.search(p, t) for p in pats)

def count_any(t, pats):
    return sum(1 for p in pats if re.search(p, t))

def student_name(filename):
    return Path(filename).name.split('_')[0].lower()

rows = []
for fp in sorted(sub_dir.iterdir()):
    if fp.is_dir():
        continue
    ext = fp.suffix.lower()
    t = read_text(fp).lower()
    wc = len(re.findall(r"\b\w+\b", t))

    # core required elements
    outliers = has_any(t, [r"z[- ]?score", r"outlier", r"\babs\(", r">\s*3"])
    normality = has_any(t, [r"normality", r"shapiro", r"q-?q", r"qqplot", r"hist"])
    linearity = has_any(t, [r"linearity", r"scatter", r"pairs\(", r"plot\(", r"lm\("])
    homogeneity = has_any(t, [r"levene", r"homogeneity", r"homosced", r"equal vari"])
    anova = has_any(t, [r"anova", r"aov\(", r"f\s*\(", r"omnibus"])
    eta = has_any(t, [r"eta", r"eta\^?2"])
    omega = has_any(t, [r"omega", r"omega\^?2"])
    power = has_any(t, [r"power", r"sample size", r"pwr", r"uniroot", r"n\s*=\s*2\s*\*?\s*per group"])
    posthoc = has_any(t, [r"post\s*hoc", r"pairwise", r"t\.test"])
    bonf = has_any(t, [r"bonferroni", r"p\.adjust", r"p\.adj"])
    trend = has_any(t, [r"trend", r"polynomial", r"contrast", r"linear trend", r"quadratic"])
    graph = has_any(t, [r"ggplot", r"geom_bar", r"bar chart", r"error bar", r"coord_cartesian", r"ylim"])
    writeup = has_any(t, [r"in this study", r"we found", r"results", r"figure", r"significant", r"not significant"])

    outputs = count_any(t, [
        r"\[1\]", r"f\s*\([^\)]*\)\s*=", r"p\s*[<=>]\s*\.?\d", r"levene", r"bonferroni",
        r"eta", r"omega", r"cohen", r"trend", r"ggplot", r"error bar"
    ])

    interp = count_any(t, [
        r"this means", r"suggests", r"indicates", r"implies", r"therefore", r"we conclude", r"in this study",
        r"compared to", r"compared with", r"higher than", r"lower than", r"because", r"practical"
    ])
    template = count_any(t, [
        r"fill in", r"don'?t change this", r"include the output", r"do you think you'?ve met",
        r"run the anova test", r"write up a results section", r"a\.\s*include", r"b\.\s*was the omnibus"
    ])
    placeholders = count_any(t, [r"eta\s*=\s*12", r"\benter your name\b", r"\bna\b"])

    core = sum([outliers, normality, linearity, homogeneity, anova, eta, omega, power, posthoc, bonf, trend, graph, writeup])

    grade = 52 + core * 2.2 + outputs * 1.8
    grade += min(8, interp * 1.4)

    # rigor penalties
    grade -= template * 1.7
    grade -= placeholders * 2.5
    if ext in {'.r', '.rmd'}:
        grade -= 10
    if wc < 2200:
        grade -= 4
    if wc < 1800:
        grade -= 4

    grade = int(round(max(62, min(99, grade))))

    strengths = []
    if core >= 11:
        strengths.append("comprehensive ANOVA pipeline coverage")
    elif core >= 9:
        strengths.append("good technical coverage of required ANOVA steps")
    if interp >= 4:
        strengths.append("clear interpretation in own language")

    improves = []
    if interp < 4:
        improves.append("deeper own-language interpretation of findings")
    if template >= 5:
        improves.append("reduce copied prompt text and keep concise original write-up")
    if not trend:
        improves.append("explicit trend analysis output and interpretation")
    if not graph:
        improves.append("final bar chart details (error bars, ordered groups, 0-100 scale)")
    if ext in {'.r', '.rmd'}:
        improves.append("submit knitted report format (HTML/DOCX) with clean narrative")

    comment = "Strengths: " + ("; ".join(strengths) if strengths else "partially complete analysis")
    if improves:
        comment += ". Improve: " + "; ".join(improves[:3]) + "."

    rows.append((student_name(fp.name), grade, comment))

rows.sort(key=lambda x: x[0])

with out_csv.open('w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(["Student", "Grade", "Comments"])
    w.writerows(rows)

print(f"Wrote {len(rows)} rows -> {out_csv}")
for r in rows:
    print(r[0], r[1])
