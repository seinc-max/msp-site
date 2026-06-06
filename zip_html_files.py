import os
import zipfile

source_dir = "/data/msp-site"
zip_path = "/data/.openclaw/workspace/assets/trueline-all-html-files.zip"

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(source_dir):
        # Exclude git directories or node_modules just in case, though we only match .html
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)

print(f"Zip created at {zip_path}")
