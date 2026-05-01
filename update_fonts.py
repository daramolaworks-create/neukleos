import glob

html_files = glob.glob('**/*.html', recursive=True)
for file_path in html_files:
    if 'node_modules' in file_path: continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update Google Fonts link to include 100
    if 'Inter:wght@200;300' in content:
        content = content.replace('Inter:wght@200;300', 'Inter:wght@100;200;300')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
