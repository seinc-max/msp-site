import sys

file_path = "/data/msp-site/ai-governance-guelph.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Removing the specific stale JSON-LD block from Guelph
stale_json_ld = '''"What does Trueline IT cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Essentials: $99/user/month. Professional: $149/user/month (most popular). Complete: $199/user/month. Minimum 10 users. Month-to-month, no long-term contract."
        }
      },
      {
        "@type": "Question",
        "name": '''

content = content.replace(stale_json_ld, '')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

