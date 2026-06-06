import re

def apply_fixes(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Fix duplicate price note
        content = content.replace(
            '<p class="offer-price-note">For businesses with 15–30 employees.</p>\n          <p class="offer-price-note">For businesses with 15–30 employees.</p>',
            '<p class="offer-price-note">For businesses with 15–30 employees.</p>'
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Applied fixes to {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

apply_fixes("/data/msp-site/shadow-ai-prevention-ontario.html")
