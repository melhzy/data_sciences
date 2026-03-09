import zipfile, re
p=r'd:/Github/data_sciences/ANLY500-Analytics-I/archive/term_final/requirements/final_project_guidelines.docx'
with zipfile.ZipFile(p,'r') as z:
    x=z.read('word/document.xml').decode('utf-8','ignore')
text=re.sub(r'(?s)<[^>]+>',' ',x)
text=re.sub(r'\s+',' ',text)
print(text[:12000])
