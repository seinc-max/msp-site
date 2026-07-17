import re
import os

files_to_fix = [
    '/opt/data/msp-site/risk-assessment.html',
    '/opt/data/msp-site/safe-copilot-deployment.html'
]

for filepath in files_to_fix:
    with open(filepath, 'r') as f:
        html = f.read()

    # 1. Fallback for offsetWidth (iOS Safari edge case)
    # Sometimes void el.offsetWidth gets optimized away. Setting a dummy variable forces the reflow on old WebKit.
    html = html.replace('void nextStep.offsetWidth;', 'const _reflow = nextStep.offsetWidth;')

    # 2. Fix touch targets for thumbs
    # Ensure the entire label is a block with no dead zones
    html = html.replace('<label class="flex items-start', '<label class="flex items-start w-full relative touch-manipulation')

    # 3. Add explicit viewport touch-action constraint to prevent double-tap zooming on Android/iOS
    if '<meta name="viewport" content="width=device-width, initial-scale=1.0">' in html:
        html = html.replace(
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">'
        )
        
    # 4. IE11 / Old Chrome syntax polyfill (Ensure we aren't using let/const in global scope breaking older parsers)
    # We will wrap the JS in an IIFE (Immediately Invoked Function Expression) to protect the global scope
    if 'document.addEventListener("DOMContentLoaded"' in html and '(function() {' not in html:
        script_block = re.search(r'(<script>)(.*?)(</script>)', html[html.find('const form = document.getElementById'):], re.DOTALL)
        if script_block:
            original_script = script_block.group(2)
            safe_script = f"\n(function() {{\n{original_script}\n}})();\n"
            html = html.replace(original_script, safe_script)

    with open(filepath, 'w') as f:
        f.write(html)
        print(f"Patched cross-device safeties in {os.path.basename(filepath)}")
