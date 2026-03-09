from pathlib import Path
import shutil

base = Path(r"d:/Github/data_sciences/ANLY500-Analytics-I/archive/term_final/submissions")

moved = 0
skipped = 0

for item in list(base.iterdir()):
    if item.is_dir():
        continue
    name = item.name
    if '_' not in name:
        skipped += 1
        continue
    student = name.split('_')[0].strip().lower()
    if not student:
        skipped += 1
        continue
    dest_dir = base / student
    dest_dir.mkdir(exist_ok=True)
    dest_file = dest_dir / name
    if dest_file.exists():
        skipped += 1
        continue
    shutil.move(str(item), str(dest_file))
    moved += 1

print(f"Moved: {moved}")
print(f"Skipped: {skipped}")
