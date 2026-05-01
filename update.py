import os
import glob

html_files = glob.glob('**/*.html', recursive=True)
for file_path in html_files:
    if 'node_modules' in file_path: continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Replace em dash
    content = content.replace(' — ', ' - ')
    content = content.replace('—', ' - ')
    
    # Update Google Fonts link
    content = content.replace('Inter:wght@400;500;600;700;800', 'Inter:wght@200;300;400;500;600;700;800')
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")

print("Done")
