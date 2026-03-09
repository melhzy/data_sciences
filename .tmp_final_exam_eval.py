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
    # first segment before numeric id/question marker
    parts = base.split('_question_')[0].split('_')
    cleaned = [p for p in parts if p and not p.isdigit() and not re.fullmatch(r"\d+", p)]
    return ''.join(cleaned)


def extract_qnum(filename: str):
    m = re.search(r"question_(\d+)", filename.lower())
    if not m:
        return None
    code = m.group(1)
    mapping = {
        '1647348': 1,
        '1647349': 2,
        '1647350': 3,
        '1647351': 4,
    }
    return mapping.get(code)


def own_language_score(t: str):
    interp = count_any(t, [
        r"this means", r"suggests", r"indicates", r"implies", r"therefore", r"we conclude",
        r"in this study", r"compared to", r"higher than", r"lower than", r"because", r"shows that"
    ])
    generic = count_any(t, [
        r"provide an interpretation", r"capture a summary", r"rubric", r"for full credit",
        r"please submit", r"questions below concentrate"
    ])
    wc = len(re.findall(r"\b\w+\b", t))
    score = 0
    if wc >= 250:
        score += 2
    elif wc >= 150:
        score += 1
    score += min(3, interp)
    score -= min(2, generic)
    return max(0, min(5, score)), interp, wc


def score_q1(t: str):
    pts = 0
    attempt = has_any(t, [r"correlation", r"cor\(", r"corrplot", r"correlation matrix"])
    if attempt:
        pts += 12

    req = 0
    req += 1 if has_any(t, [r"accuracy", r"missing", r"na", r"outlier", r"z[- ]?score"]) else 0
    req += 1 if has_any(t, [r"linearity", r"normality", r"homogeneity", r"homoscedasticity", r"shapiro", r"levene"]) else 0
    req += 1 if has_any(t, [r"correlation matrix", r"cor\(", r"corrplot", r"pairs\(", r"heatmap"]) else 0
    req += 1 if has_any(t, [r"variance", r"var\("]) else 0
    req += 1 if has_any(t, [r"covariance", r"cov\("]) else 0
    pts += req * 1.6  # up to 8

    accuracy = 0
    accuracy += 1 if has_any(t, [r"r\s*=", r"pearson", r"spearman"]) else 0
    accuracy += 1 if has_any(t, [r"p\s*[<=>]", r"significant", r"not significant"]) else 0
    accuracy += 1 if has_any(t, [r"interpret", r"relationship", r"correlated effect"]) else 0
    pts += accuracy * 1.7  # up to ~5.1

    own, interp, wc = own_language_score(t)
    pts += own

    return max(0, min(25, round(pts))), {
        'attempt': attempt, 'req_count': req, 'accuracy': accuracy, 'own': own, 'interp': interp, 'wc': wc
    }


def score_q2(t: str):
    pts = 0
    attempt = has_any(t, [r"regression", r"lm\(", r"model summary", r"summary\("])
    if attempt:
        pts += 12

    req = 0
    req += 1 if has_any(t, [r"species", r"dependent variable"]) else 0
    req += 1 if has_any(t, [r"significant variable", r"p\s*[<=>]", r"pr\(>\|t\|\)"]) else 0
    req += 1 if has_any(t, [r"summary\(", r"r-squared", r"adjusted r-squared", r"f-statistic"]) else 0
    req += 1 if has_any(t, [r"plot\(", r"ggplot", r"residual", r"diagnostic", r"visual"]) else 0
    pts += req * 2.0  # 8

    accuracy = 0
    accuracy += 1 if has_any(t, [r"coefficient", r"estimate", r"intercept"]) else 0
    accuracy += 1 if has_any(t, [r"significant", r"not significant", r"p\s*[<=>]"]) else 0
    accuracy += 1 if has_any(t, [r"interpret", r"predict", r"relationship"]) else 0
    pts += accuracy * 1.7

    own, interp, wc = own_language_score(t)
    pts += own

    return max(0, min(25, round(pts))), {
        'attempt': attempt, 'req_count': req, 'accuracy': accuracy, 'own': own, 'interp': interp, 'wc': wc
    }


def score_q3(t: str):
    pts = 0
    attempt = has_any(t, [r"anova", r"aov\(", r"f\s*\("])
    if attempt:
        pts += 12

    req = 0
    req += 1 if has_any(t, [r"species", r"dependent variable"]) else 0
    req += 1 if has_any(t, [r"anova", r"aov\("]) else 0
    req += 1 if has_any(t, [r"summary\(", r"f\s*\(", r"p\s*[<=>]"]) else 0
    pts += req * 2.7  # up to 8.1

    accuracy = 0
    accuracy += 1 if has_any(t, [r"significant", r"not significant", r"p\s*[<=>]"]) else 0
    accuracy += 1 if has_any(t, [r"between groups", r"group difference", r"effect"]) else 0
    pts += accuracy * 2.0

    own, interp, wc = own_language_score(t)
    pts += own

    return max(0, min(25, round(pts))), {
        'attempt': attempt, 'req_count': req, 'accuracy': accuracy, 'own': own, 'interp': interp, 'wc': wc
    }


def score_q4(t: str):
    pts = 0
    attempt = has_any(t, [r"t-test", r"t test", r"t\.test\(", r"setosa", r"versicolor"])
    if attempt:
        pts += 12

    req = 0
    req += 1 if has_any(t, [r"h0", r"null hypothesis", r"ha", r"alternative"]) else 0
    req += 1 if has_any(t, [r"setosa", r"versicolor", r"sepal.length"]) else 0
    req += 1 if has_any(t, [r"t\.test\(", r"t-test", r"summary"]) else 0
    req += 1 if has_any(t, [r"p\s*[<=>]", r"confidence interval", r"mean"]) else 0
    pts += req * 2.0  # 8

    accuracy = 0
    accuracy += 1 if has_any(t, [r"reject", r"fail to reject", r"significant", r"not significant"]) else 0
    accuracy += 1 if has_any(t, [r"interpret", r"difference", r"effect", r"conclusion"]) else 0
    pts += accuracy * 1.8

    own, interp, wc = own_language_score(t)
    pts += own

    return max(0, min(25, round(pts))), {
        'attempt': attempt, 'req_count': req, 'accuracy': accuracy, 'own': own, 'interp': interp, 'wc': wc
    }


scorer = {1: score_q1, 2: score_q2, 3: score_q3, 4: score_q4}

by_student = defaultdict(dict)
for fp in sorted(sub_dir.iterdir()):
    if fp.is_dir():
        continue
    q = extract_qnum(fp.name)
    if q not in {1,2,3,4}:
        continue
    stu = extract_student(fp.name)
    txt = read_text(fp)
    score, meta = scorer[q](txt.lower())
    prev = by_student[stu].get(q)
    candidate = {'score': score, 'meta': meta, 'file': fp.name, 'ext': fp.suffix.lower()}
    if prev is None or score > prev['score']:
        by_student[stu][q] = candidate

rows = []
for stu in sorted(by_student):
    q_scores = []
    missing = []
    metas = []
    format_flags = []
    for q in [1,2,3,4]:
        if q in by_student[stu]:
            q_scores.append(by_student[stu][q]['score'])
            metas.append((q, by_student[stu][q]['meta']))
            if by_student[stu][q]['ext'] in {'.pages', '.r', '.rmd'}:
                format_flags.append(q)
        else:
            q_scores.append(0)
            missing.append(q)
    total = int(sum(q_scores))

    strengths = []
    if q_scores[0] >= 20:
        strengths.append("strong correlation/covariance/variance analysis")
    if q_scores[1] >= 20:
        strengths.append("solid regression modeling and summary")
    if q_scores[2] >= 20:
        strengths.append("good ANOVA execution and interpretation")
    if q_scores[3] >= 20:
        strengths.append("clear t-test setup and conclusion")

    own_total = sum(meta['own'] for _, meta in metas)
    if own_total >= 14:
        strengths.append("consistently uses own-language interpretation")

    improvements = []
    for q, meta in metas:
        if meta['own'] <= 2:
            improvements.append(f"Q{q}: deepen plain-English interpretation tied to output")
        if meta['req_count'] <= 2:
            improvements.append(f"Q{q}: cover more required rubric components")
    if missing:
        improvements.insert(0, f"missing submission(s): Q{','.join(map(str, missing))}")
    if format_flags:
        improvements.append(f"submit knitted Word/HTML format for Q{','.join(map(str, format_flags))}")

    if not strengths:
        strengths.append("partial attempt across exam components")

    comment = "Strengths: " + "; ".join(strengths[:2])
    if improvements:
        comment += ". Improve: " + "; ".join(dict.fromkeys(improvements))[:420]
        if not comment.endswith('.'):
            comment += '.'

    rows.append((stu, total, comment))

with out_csv.open('w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['Student', 'Grade', 'Comments'])
    w.writerows(rows)

print(f"Wrote {len(rows)} students to {out_csv}")
for stu, g, _ in rows:
    print(stu, g)
