import re, csv, zipfile
from pathlib import Path

root = Path(r"d:/Github/data_sciences/ANLY500-Analytics-I/archive/week10")
sub_dir = root / "submissions"
out_csv = root / "week10-grade.csv"


def strip_html(s: str) -> str:
    s = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = re.sub(r"&nbsp;", " ", s)
    s = re.sub(r"&amp;", " and ", s)
    return re.sub(r"\s+", " ", s)


def read_docx_text(path: Path) -> str:
    try:
        with zipfile.ZipFile(path, 'r') as zf:
            with zf.open('word/document.xml') as f:
                xml = f.read().decode('utf-8', errors='ignore')
        txt = re.sub(r"(?s)<[^>]+>", " ", xml)
        return re.sub(r"\s+", " ", txt)
    except Exception:
        return ""


def read_text(path: Path) -> str:
    ext = path.suffix.lower()
    try:
        if ext in {'.html', '.htm'}:
            return strip_html(path.read_text(encoding='utf-8', errors='ignore'))
        if ext == '.docx':
            return read_docx_text(path)
        return path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return ""


def has_any(t, pats):
    return any(re.search(p, t) for p in pats)


def count_any(t, pats):
    return sum(1 for p in pats if re.search(p, t))


def score_submission(text: str):
    t = text.lower()
    wc = len(re.findall(r"\b\w+\b", t))

    data_use = has_any(t, [r"10_data\.csv", r"import\(", r"read\.csv", r"read_csv", r"rio", r"data\s*<-", r"competence", r"participant"])
    outliers = has_any(t, [r"z[- ]?score", r"scale\(", r"\|?z\|?", r"outlier", r">\s*3", r"3\.0"]) 
    normality = has_any(t, [r"normality", r"shapiro", r"q-?q", r"qqplot", r"hist", r"distribution"])
    linearity = has_any(t, [r"linearity", r"scatter", r"pairs\(", r"plot\(", r"lm\("])
    homogeneity = has_any(t, [r"homogeneity", r"homosced", r"levene", r"equal vari", r"variance"])
    anova = has_any(t, [r"anova", r"aov\(", r"f\s*\(", r"omnibus"]) 
    sig = has_any(t, [r"p\s*[<=>]", r"significant", r"not significant"])
    eta = has_any(t, [r"eta", r"eta\^?2", r"eta squared"])
    omega = has_any(t, [r"omega", r"omega\^?2", r"omega squared"])
    power = has_any(t, [r"power", r"pwr", r"sample size", r"participants would you have needed", r"uniroot"])
    posthoc = has_any(t, [r"post\s*hoc", r"pairwise", r"t\.test", r"no correction", r"bonferroni"]) 
    bonf = has_any(t, [r"bonferroni", r"p\.adj", r"adjust"])
    effect_d = has_any(t, [r"cohen", r"hedges", r"\bd\b", r"effect size"]) 
    trend = has_any(t, [r"trend", r"polynomial", r"contrast", r"linear trend", r"quadratic"])
    graph = has_any(t, [r"ggplot", r"geom_bar", r"bar chart", r"error bar", r"coord_cartesian", r"ylim", r"figure"])
    table = has_any(t, [r"kable", r"table", r"no correction p", r"bonferroni p", r"d value"]) 
    writeup = has_any(t, [r"results", r"in this study", r"we found", r"figure", r"omnibus", r"post hoc"])

    interp_markers = [
        r"this means", r"suggests", r"indicates", r"implies", r"therefore", r"we conclude", r"in this study",
        r"compared to", r"compared with", r"higher than", r"lower than", r"practical", r"interpre", r"because"
    ]
    interp_hits = count_any(t, interp_markers)

    template_markers = [
        r"fill in the number", r"fill in where it says", r"don'?t change this", r"include the output",
        r"do you think you'?ve met", r"run the anova test", r"write up a results section", r"a\.\s*include",
        r"b\.\s*was the omnibus", r"c\.\s*the omnibus"
    ]
    template_hits = count_any(t, template_markers)

    tech_points = 0
    tech_points += 4 if data_use else 0
    tech_points += 6 if outliers else 0
    tech_points += 5 if normality else 0
    tech_points += 4 if linearity else 0
    tech_points += 8 if homogeneity else 0
    tech_points += 10 if anova else 0
    tech_points += 4 if sig else 0
    tech_points += 7 if eta else 0
    tech_points += 7 if omega else 0
    tech_points += 5 if power else 0
    tech_points += 8 if posthoc else 0
    tech_points += 3 if bonf else 0
    tech_points += 6 if effect_d else 0
    tech_points += 5 if trend else 0
    tech_points += 5 if graph else 0
    tech_points += 3 if table else 0
    tech_points += 5 if writeup else 0
    tech_points = min(85, tech_points)

    own_lang_points = 0
    if wc >= 800:
        own_lang_points += 5
    elif wc >= 450:
        own_lang_points += 4
    elif wc >= 250:
        own_lang_points += 2

    own_lang_points += min(8, interp_hits)
    own_lang_points -= min(6, template_hits)
    own_lang_points = max(0, min(15, own_lang_points))

    reporting_points = 0
    reporting_points += 5 if has_any(t, [r"mean", r"sd", r"standard deviation", r"error bar"]) else 0
    reporting_points += 5 if has_any(t, [r"f\s*\(", r"t\s*\(", r"p\s*[<=>]", r"eta", r"omega", r"d\s*="]) else 0

    total = int(round(tech_points + own_lang_points + reporting_points))
    total = max(45, min(100, total))

    deficits = []
    if not outliers: deficits.append("outlier z-score step")
    if not homogeneity: deficits.append("Levene/homogeneity evidence")
    if not anova: deficits.append("omnibus ANOVA output")
    if not eta or not omega: deficits.append("both eta^2 and omega^2 effect sizes")
    if not posthoc or not bonf: deficits.append("post hoc with Bonferroni comparison")
    if not trend: deficits.append("trend analysis")
    if not graph: deficits.append("final bar chart with error bars")
    if own_lang_points < 7: deficits.append("own-language interpretation depth")
    if wc < 220: deficits.append("submission completeness/length")

    strengths = []
    if anova and posthoc: strengths.append("solid ANOVA and post hoc workflow")
    if eta and omega: strengths.append("reported core ANOVA effect sizes")
    if graph and writeup: strengths.append("included figure and narrative results")
    if own_lang_points >= 10: strengths.append("clear original interpretation in own words")
    if homogeneity and normality: strengths.append("assumption checks were documented")

    return {"grade": total, "wc": wc, "deficits": deficits[:3], "strengths": strengths[:2]}


def student_from_name(filename: str):
    return Path(filename).name.split('_')[0].lower()

records = {}
for fp in sorted(sub_dir.iterdir()):
    if fp.is_dir():
        continue
    text = read_text(fp)
    sc = score_submission(text)
    stu = student_from_name(fp.name)
    row = {"student": stu, "file": fp.name, **sc}
    if (stu not in records) or (row["grade"] > records[stu]["grade"]):
        records[stu] = row

rows = []
for stu in sorted(records):
    r = records[stu]
    comment = ("Strengths: " + "; ".join(r["strengths"])) if r["strengths"] else "Partial completion detected"
    if r["deficits"]:
        comment += ". Improve: " + "; ".join(r["deficits"]) + "."
    rows.append((stu, r["grade"], comment))

with out_csv.open('w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(["Student", "Grade", "Comments"])
    w.writerows(rows)

print(f"Wrote {len(rows)} grades to {out_csv}")
for stu, g, _ in rows:
    print(stu, g)
