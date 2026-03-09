import csv, re, zipfile
from pathlib import Path
from collections import defaultdict

root = Path(r"d:/Github/data_sciences/ANLY500-Analytics-I/archive/anly500_final")
sub_dir = root / "submissions"
out_csv = root / "final_exam_grade.csv"


def strip_html(s: str) -> str:
    s = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = s.replace('&nbsp;', ' ').replace('&amp;', ' and ')
    return re.sub(r"\s+", " ", s)


def read_docx(path: Path) -> str:
    try:
        with zipfile.ZipFile(path, 'r') as zf:
            xml = zf.read('word/document.xml').decode('utf-8', errors='ignore')
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
            return read_docx(path)
        return path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return ""


def has_any(t, pats):
    return any(re.search(p, t) for p in pats)


def count_any(t, pats):
    return sum(1 for p in pats if re.search(p, t))


def extract_student(filename: str) -> str:
    base = Path(filename).name.lower()
    prefix = base.split('_question_')[0]
    prefix = re.sub(r"\d+$", "", prefix)
    return prefix.replace("_", "")


def extract_qnum(filename: str):
    m = re.search(r"question_(\d+)", filename.lower())
    if not m:
        return None
    return {'1647348': 1, '1647349': 2, '1647350': 3, '1647351': 4}.get(m.group(1))


def own_lang(t):
    interp = count_any(t, [
        r"this means", r"suggests", r"indicates", r"implies", r"therefore", r"we conclude",
        r"in this study", r"compared to", r"higher than", r"lower than", r"because", r"shows that"
    ])
    generic = count_any(t, [
        r"provide an interpretation", r"capture a summary", r"rubric", r"for full credit", r"please submit"
    ])
    wc = len(re.findall(r"\b\w+\b", t))
    score = 0
    if interp >= 3:
        score += 2
    elif interp >= 1:
        score += 1
    if wc < 120:
        score -= 1
    if generic >= 3 and interp <= 1:
        score -= 1
    return max(0, min(2, score)), interp, wc


def q_score(t: str, q: int):
    if q == 1:
        attempt = has_any(t, [r"correlation", r"cor\(", r"correlation matrix", r"corrplot"])
        req_flags = [
            has_any(t, [r"accuracy", r"missing", r"na", r"outlier", r"z[- ]?score"]),
            has_any(t, [r"linearity", r"normality", r"homogeneity", r"homoscedasticity", r"shapiro", r"levene"]),
            has_any(t, [r"correlation matrix", r"cor\(", r"corrplot", r"pairs\(", r"heatmap"]),
            has_any(t, [r"variance", r"var\("]),
            has_any(t, [r"covariance", r"cov\("]),
        ]
        acc_flags = [
            has_any(t, [r"r\s*=", r"pearson", r"spearman"]),
            has_any(t, [r"p\s*[<=>]", r"significant", r"not significant"]),
            has_any(t, [r"relationship", r"correlated effect", r"interpret"]),
            has_any(t, [r"matrix", r"visual", r"plot"]),
            has_any(t, [r"what does it tell", r"indicate", r"means"]),
        ]
    elif q == 2:
        attempt = has_any(t, [r"regression", r"lm\(", r"model summary"])
        req_flags = [
            has_any(t, [r"species", r"dependent variable"]),
            has_any(t, [r"significant", r"pr\(>\|t\|\)", r"p\s*[<=>]"]),
            has_any(t, [r"summary\(", r"r-squared", r"adjusted r-squared", r"f-statistic"]),
            has_any(t, [r"plot\(", r"ggplot", r"residual", r"diagnostic", r"visual"]),
            has_any(t, [r"final model", r"model with only significant"]),
        ]
        acc_flags = [
            has_any(t, [r"coefficient", r"estimate", r"intercept"]),
            has_any(t, [r"p\s*[<=>]", r"significant", r"not significant"]),
            has_any(t, [r"predictor", r"variable"]),
            has_any(t, [r"interpret", r"means", r"indicates"]),
            has_any(t, [r"support", r"based on results", r"model summary"]),
        ]
    elif q == 3:
        attempt = has_any(t, [r"anova", r"aov\(", r"f\s*\("])
        req_flags = [
            has_any(t, [r"species", r"dependent variable"]),
            has_any(t, [r"anova", r"aov\("]),
            has_any(t, [r"summary\(", r"f\s*\(", r"p\s*[<=>]"]),
            has_any(t, [r"interpret", r"difference", r"group", r"effect"]),
        ]
        acc_flags = [
            has_any(t, [r"p\s*[<=>]", r"significant", r"not significant"]),
            has_any(t, [r"f\s*\(", r"df", r"statistic"]),
            has_any(t, [r"between", r"across species", r"group difference"]),
            has_any(t, [r"support", r"based on", r"results"]),
            has_any(t, [r"conclusion", r"therefore", r"suggests"]),
        ]
    else:
        attempt = has_any(t, [r"t-test", r"t test", r"t\.test\(", r"setosa", r"versicolor"])
        req_flags = [
            has_any(t, [r"h0", r"null hypothesis"]),
            has_any(t, [r"ha", r"alternative"]),
            has_any(t, [r"setosa", r"versicolor", r"sepal.length"]),
            has_any(t, [r"t\.test\(", r"t-test", r"summary"]),
            has_any(t, [r"p\s*[<=>]", r"confidence interval", r"mean"]),
        ]
        acc_flags = [
            has_any(t, [r"reject", r"fail to reject", r"significant", r"not significant"]),
            has_any(t, [r"difference", r"effect", r"conclusion"]),
            has_any(t, [r"setosa", r"versicolor"]),
            has_any(t, [r"support", r"based on results", r"output"]),
            has_any(t, [r"interpret", r"means", r"indicates"]),
        ]

    attempt_pts = 10 if attempt else 0
    req_pts = 8 * (sum(req_flags) / len(req_flags))
    acc_pts = 5 * (sum(acc_flags) / len(acc_flags))
    own_pts, interp, wc = own_lang(t)

    score = attempt_pts + req_pts + acc_pts + own_pts
    if wc < 90:
        score -= 2

    score = int(round(max(0, min(25, score))))
    meta = {
        'req': sum(req_flags), 'req_total': len(req_flags),
        'own': own_pts, 'interp': interp, 'wc': wc
    }
    return score, meta


by_student = defaultdict(dict)
for fp in sorted(sub_dir.iterdir()):
    if fp.is_dir():
        continue
    q = extract_qnum(fp.name)
    if q not in {1, 2, 3, 4}:
        continue
    stu = extract_student(fp.name)
    score, meta = q_score(read_text(fp).lower(), q)
    cand = {'score': score, 'meta': meta, 'ext': fp.suffix.lower()}
    prev = by_student[stu].get(q)
    if prev is None or score > prev['score']:
        by_student[stu][q] = cand

rows = []
for stu in sorted(by_student):
    q1 = by_student[stu].get(1, {}).get('score', 0)
    q2 = by_student[stu].get(2, {}).get('score', 0)
    q3 = by_student[stu].get(3, {}).get('score', 0)
    q4 = by_student[stu].get(4, {}).get('score', 0)
    total = q1 + q2 + q3 + q4

    missing = [q for q in [1,2,3,4] if q not in by_student[stu]]
    format_penalty_q = [q for q in [1,2,3,4] if q in by_student[stu] and by_student[stu][q]['ext'] in {'.pages', '.r', '.rmd'}]
    total -= 3 * len(format_penalty_q)
    total = int(max(0, min(100, total)))

    strengths = []
    if q1 >= 22: strengths.append("Q1 correlation analysis is strong")
    if q2 >= 22: strengths.append("Q2 regression modeling is well executed")
    if q3 >= 22: strengths.append("Q3 ANOVA section is technically solid")
    if q4 >= 22: strengths.append("Q4 t-test setup and reporting are clear")
    if not strengths: strengths.append("partial but substantive exam attempt")

    own_weak_q = [q for q in [1,2,3,4] if q in by_student[stu] and by_student[stu][q]['meta']['own'] == 0]
    req_weak_q = [q for q in [1,2,3,4] if q in by_student[stu] and by_student[stu][q]['meta']['req'] < (by_student[stu][q]['meta']['req_total'] - 1)]

    improvements = []
    if missing:
        improvements.append(f"submit missing question(s): Q{','.join(map(str, missing))}")
    if own_weak_q:
        improvements.append(f"use more original interpretation language in Q{','.join(map(str, own_weak_q))}")
    if req_weak_q:
        improvements.append(f"cover all rubric elements more explicitly in Q{','.join(map(str, req_weak_q))}")
    if format_penalty_q:
        improvements.append(f"submit knitted Word/HTML format for Q{','.join(map(str, format_penalty_q))}")

    comment = "Strengths: " + "; ".join(strengths[:2])
    if improvements:
        comment += ". Improve: " + "; ".join(improvements[:2]) + "."

    rows.append((stu, total, q1, q2, q3, q4, comment))

with out_csv.open('w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['Student', 'Grade', 'Q1', 'Q2', 'Q3', 'Q4', 'Comments'])
    w.writerows(rows)

print(f"Updated {out_csv} with sub-scores + individualized comments for {len(rows)} students")
