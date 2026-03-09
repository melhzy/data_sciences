import csv
from pathlib import Path

file_path = Path(r"d:/Github/data_sciences/ANLY500-Analytics-I/archive/anly500_final/final_exam_grade.csv")

rows = [
    ["ahmedassad",93,22,22,25,24,"Strong ANOVA and t-test performance with consistent statistical workflow across all sections; final note is to better integrate covariance and variance explanation within the Q1 interpretation."],
    ["bhandaretanmaydwarkanath",96,25,23,24,24,"Very balanced and high-quality submission with excellent Q1 and solid inference across Q3 and Q4; Q2 interpretation is present but could be more explicit in practical meaning."],
    ["fuyunlong",91,23,23,22,23,"Technically consistent work across all four questions with no major rubric omissions; interpretation depth was lighter in Q2-Q4 relative to the statistical output quality."],
    ["gaikwadravinaprakash",92,25,21,22,24,"Excellent correlation section and strong testing structure, especially in Q4; explanatory depth in Q2-Q3 is comparatively lighter than technical execution."],
    ["hexun",92,24,24,20,24,"Strong Q1, Q2, and Q4 sections with clear method usage and reporting flow; Q3 ANOVA interpretation is shorter and less developed than other sections."],
    ["imtiazahmed",100,25,25,25,25,"Outstanding exam performance with full rubric coverage and strong interpretation quality across all questions."],
    ["jainraunaq",96,24,25,23,24,"Very strong regression and overall analytical control with good consistency across sections; Q3 discussion is correct but comparatively brief."],
    ["katragaddamanish",91,23,24,21,23,"Good command of methods and clear completion across all questions; interpretation strength is uneven in Q3 and Q4 compared with technical setup."],
    ["krishnamurthysmruthi",92,24,24,20,24,"Well-structured exam with clear strengths in Q1, Q2, and Q4; Q3 narrative interpretation is present but relatively limited."],
    ["lakkadakshitachetan",95,23,25,23,24,"Excellent Q2 regression quality and strong overall technical consistency; Q1 and Q3 would benefit from more explicit explanatory linkage to outputs."],
    ["mahajanaashna",92,25,24,23,23,"Strong analytical coverage with high-quality Q1 and Q2 sections; Q4 was submitted in non-standard format which affects submission compliance."],
    ["manachokarimajane",88,25,21,20,22,"Excellent Q1 foundation and competent Q4 execution; Q3-Q4 interpretation depth is lower than the technical work shown."],
    ["natasanjeyashree",89,24,21,20,24,"Good t-test section and complete methodological coverage overall; interpretation quality is lighter in Q2 and Q3 compared with Q1 and Q4."],
    ["shindesiddheshudesh",91,23,22,22,24,"Consistent completion across all questions with solid inferential structure; explanatory narrative in Q1-Q3 is less developed than the statistical reporting."],
    ["sunfeiyi",95,25,24,23,23,"Very good overall exam quality with a strong Q1 and stable scoring profile; Q3 and Q4 interpretation detail is comparatively brief."],
    ["suumemmanuelndone",28,5,23,0,0,"Meaningful work is present in Q2, but total score is substantially reduced by missing Q3 and Q4 and limited Q1 completion."],
    ["usadadiyaparas",93,22,24,23,24,"Strong and consistent execution across all sections with good inferential flow; Q1 interpretation could be more tightly anchored to reported statistics."],
    ["xiekaiyu",96,25,23,24,24,"Excellent Q1 and strong overall technical quality across the exam; Q2 predictor interpretation is correct but relatively concise."],
    ["yixiaowen",92,24,24,21,23,"Good balance across questions with clear handling of correlation and regression; Q4 conclusion is valid but less fully explained than earlier sections."],
    ["zaverirohanpurvin",95,24,24,24,23,"Strong and consistent submission with good rubric coverage and statistical structure throughout; Q4 interpretation depth is slightly lighter than Q1-Q3."]
]

with file_path.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
    w.writerow(["Student","Grade","Q1","Q2","Q3","Q4","Comments"])
    w.writerows(rows)

print(f"Restored and formatted {file_path} with {len(rows)} rows")
