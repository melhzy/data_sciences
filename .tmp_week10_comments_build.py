import csv, re, zipfile
from pathlib import Path

root = Path(r"d:/Github/data_sciences/ANLY500-Analytics-I/archive/week10")
sub_dir = root / "submissions"
grade_csv = root / "week10-grade.csv"
out_csv = Path(r"d:/Github/data_sciences/.tmp_week10-grade-individualized.csv")

grades = {}
with grade_csv.open(encoding='utf-8', newline='') as f:
    for row in csv.DictReader(f):
        grades[row['Student'].strip().lower()] = int(row['Grade'])


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
        if ext in {'.html', '.htm'}:
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

submission_by_student = {}
for fp in sorted(sub_dir.iterdir()):
    if fp.is_dir():
        continue
    stu = student_name(fp.name)
    txt = read_text(fp).lower()
    wc = len(re.findall(r"\b\w+\b", txt))
    if stu not in submission_by_student or wc > submission_by_student[stu][1]:
        submission_by_student[stu] = (fp, wc)

rows = []
for stu in sorted(grades):
    grade = grades[stu]
    if stu not in submission_by_student:
        rows.append((stu, grade, "Submission file could not be parsed reliably; please re-submit knitted report for full verification."))
        continue

    fp, wc = submission_by_student[stu]
    ext = fp.suffix.lower()
    t = read_text(fp).lower()

    outliers = has_any(t, [r"z[- ]?score", r"outlier", r"\babs\(", r">\s*3"]) 
    normality = has_any(t, [r"normality", r"shapiro", r"q-?q", r"qqplot", r"hist"]) 
    linearity = has_any(t, [r"linearity", r"scatter", r"pairs\(", r"plot\(", r"lm\("])
    homogeneity = has_any(t, [r"levene", r"homogeneity", r"homosced", r"equal vari"])
    anova = has_any(t, [r"anova", r"aov\(", r"f\s*\(", r"omnibus"]) 
    eta = has_any(t, [r"eta", r"eta\^?2"]) 
    omega = has_any(t, [r"omega", r"omega\^?2"]) 
    power = has_any(t, [r"power", r"sample size", r"pwr", r"uniroot", r"n\s*=\s*2"]) 
    posthoc = has_any(t, [r"post\s*hoc", r"pairwise", r"t\.test"]) 
    bonf = has_any(t, [r"bonferroni", r"p\.adjust", r"p\.adj"]) 
    trend = has_any(t, [r"trend", r"polynomial", r"contrast", r"linear trend", r"quadratic"]) 
    graph = has_any(t, [r"ggplot", r"geom_bar", r"bar chart", r"error bar", r"coord_cartesian", r"ylim"]) 
    table = has_any(t, [r"kable", r"no correction p", r"bonferroni p", r"d value", r"tableprint"])

    interp = count_any(t, [
        r"this means", r"suggests", r"indicates", r"implies", r"therefore", r"we conclude", r"in this study",
        r"compared to", r"compared with", r"higher than", r"lower than", r"because", r"practical"
    ])

    template_heavy = count_any(t, [
        r"fill in where it says", r"fill in the number", r"do you think you'?ve met", r"include the output",
        r"run the anova test", r"write up a results section"
    ]) >= 5

    strengths = []
    if anova and posthoc and bonf:
        strengths.append("omnibus ANOVA and post hoc comparisons were implemented correctly")
    if outliers and normality and homogeneity:
        strengths.append("data screening and assumption checks are documented")
    if eta and omega:
        strengths.append("both eta^2 and omega^2 effect sizes are reported")
    if trend:
        strengths.append("trend analysis is included")
    if graph and table:
        strengths.append("required table and visualization components are present")
    if interp >= 4:
        strengths.append("interpretation uses your own language and links back to findings")

    improve = []
    if interp < 4:
        improve.append("expand plain-English interpretation of what the statistics mean for each key group comparison")
    if not trend:
        improve.append("add explicit trend-analysis output and a one-sentence conclusion on trend type")
    if not graph:
        improve.append("final graph should explicitly show 0-100 y-scale, ordered groups, and error bars")
    if not table:
        improve.append("complete the post hoc/effect-size summary table with final numeric values")
    if not power:
        improve.append("show the power/sample-size result tied to eta^2")
    if ext in {'.r', '.rmd'}:
        improve.append("submit as knitted HTML or DOCX (not raw script) for full grading compliance")
    if template_heavy and interp < 5:
        improve.append("keep the template scaffold but replace more prompt text with concise original narrative")

    if not strengths:
        strengths.append("core analysis sections are partially completed")

    comment = "Strengths: " + "; ".join(strengths[:2])
    if improve:
        comment += ". Improve: " + "; ".join(improve[:2]) + "."

    rows.append((stu, grade, comment))

with out_csv.open('w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(["Student", "Grade", "Comments"])
    w.writerows(rows)

print(out_csv)
