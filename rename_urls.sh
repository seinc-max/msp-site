#!/bin/bash

# Rename the files
mv managed-it-services-southern-ontario.html ai-governance-southern-ontario.html
mv managed-it-services-burlington.html ai-governance-burlington.html
mv managed-it-services-hamilton.html ai-governance-hamilton.html
mv managed-it-services-guelph.html ai-governance-guelph.html
mv managed-it-services-waterloo.html ai-governance-waterloo.html
mv managed-it-services-cambridge.html ai-governance-cambridge.html
mv managed-it-services-kitchener-waterloo.html ai-governance-kitchener-waterloo.html

# Fix internal references across all HTML files
for file in *.html; do
  sed -i 's/managed-it-services-southern-ontario\.html/ai-governance-southern-ontario.html/g' "$file"
  sed -i 's/managed-it-services-burlington\.html/ai-governance-burlington.html/g' "$file"
  sed -i 's/managed-it-services-hamilton\.html/ai-governance-hamilton.html/g' "$file"
  sed -i 's/managed-it-services-guelph\.html/ai-governance-guelph.html/g' "$file"
  sed -i 's/managed-it-services-waterloo\.html/ai-governance-waterloo.html/g' "$file"
  sed -i 's/managed-it-services-cambridge\.html/ai-governance-cambridge.html/g' "$file"
  sed -i 's/managed-it-services-kitchener-waterloo\.html/ai-governance-kitchener-waterloo.html/g' "$file"
  
  sed -i 's/managed-it-services-southern-ontario/ai-governance-southern-ontario/g' "$file"
  sed -i 's/managed-it-services-burlington/ai-governance-burlington/g' "$file"
  sed -i 's/managed-it-services-hamilton/ai-governance-hamilton/g' "$file"
  sed -i 's/managed-it-services-guelph/ai-governance-guelph/g' "$file"
  sed -i 's/managed-it-services-waterloo/ai-governance-waterloo/g' "$file"
  sed -i 's/managed-it-services-cambridge/ai-governance-cambridge/g' "$file"
  sed -i 's/managed-it-services-kitchener-waterloo/ai-governance-kitchener-waterloo/g' "$file"
done

# Check if there are still any 'managed-it-services' URLs lingering
echo "Lingering references:"
grep -Eo "href=\"[^\"]*managed-it-services[^\"]*\"" *.html || echo "None found!"

