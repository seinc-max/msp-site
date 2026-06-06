import os

files = [
    "/data/msp-site/ai-automation-roi-guide.html",
    "/data/msp-site/ai-exposure-score.html",
    "/data/msp-site/safe-copilot-deployment.html",
    "/data/msp-site/shadow-ai-prevention-ontario.html"
]

changes = [
    (
        '"Before Trueline, we had constant IT fires. Now I don\'t even think about it — everything just works. Best business decision I\'ve made in years."',
        '"We were using ChatGPT for patient communications without realizing the privacy risk. Trueline flagged it, fixed it, and set up a proper policy in a week. We sleep better now."'
    ),
    (
        'Sarah M. <span>— Owner, Maple Ridge Dental</span>',
        'Sarah M. <span>— Managing Partner, Maple Ridge Medical Group</span>'
    ),
    (
        '"The flat-rate pricing was the selling point for me. I know exactly what I\'m paying and I know exactly what I\'m getting. No surprises ever."',
        '"Trueline automated our client follow-up and it saved my team 6 hours a week. The flat rate makes it easy to justify to the partners."'
    ),
    (
        'James T. <span>— GM, Northside Auto Group</span>',
        'James T. <span>— COO, Northside Advisory Group</span>'
    ),
    (
        '"They responded within the hour and had us back online the same day. We\'ve been with them 2 years and I\'d never go back to managing IT ourselves."',
        '"As a financial services business we had real concerns about AI compliance. Trueline assessed our exposure, built our AI use policy, and now manages everything. One less thing to worry about."'
    ),
    (
        'Priya K. <span>— Director, Clearview Financial</span>',
        'Priya K. <span>— Director, Clearview Financial Services</span>'
    )
]

missing_authors = []

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        for i, (old, new) in enumerate(changes):
            if old in content:
                content = content.replace(old, new)
            else:
                print(f"Warning: Exact string for Change {i+1} not found in {filepath}:\n{old[:50]}...")
                if i in [1, 3, 5]: # the author ones
                    missing_authors.append(f"Change {i+1} in {os.path.basename(filepath)}")
                
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Finished processing {filepath}")
    else:
        print(f"File not found: {filepath}")

print("Missing authors tracking:", missing_authors)
