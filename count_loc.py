import os

counts = {
    'Python LOC': 0,
    'HTML LOC': 0,
    'CSS LOC': 0,
    'JavaScript LOC': 0,
    'ML LOC': 0,
    'Test LOC': 0,
    'Total': 0
}

for r, d, files in os.walk('.'):
    if 'venv' in r or '__pycache__' in r:
        continue
    for f in files:
        path = os.path.join(r, f)
        if f.endswith(('.py', '.html', '.css', '.js')):
            try:
                with open(path, 'r', encoding='utf8', errors='ignore') as file:
                    lines = sum(1 for line in file if line.strip())
                    
                counts['Total'] += lines
                
                if f.endswith('.html'):
                    counts['HTML LOC'] += lines
                elif f.endswith('.css'):
                    counts['CSS LOC'] += lines
                elif f.endswith('.js'):
                    counts['JavaScript LOC'] += lines
                elif f.endswith('.py'):
                    if 'test' in f or 'test' in r:
                        counts['Test LOC'] += lines
                    elif 'ml' in r or 'ml' in f:
                        counts['ML LOC'] += lines
                    else:
                        counts['Python LOC'] += lines
            except Exception:
                pass

print("FINAL LOC:")
for k, v in counts.items():
    print(f"{k}: {v}")
