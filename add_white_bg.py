import os
import re

svg_files = [
    'Absa.svg', 'Access.svg', 'Africanbank.svg', 'bank-zero.svg', 'Bank.svg',
    'bidvest.svg', 'Call-Center.svg', 'Capitec-1.svg', 'Capitec-2.svg',
    'Capitec-Business-1.svg', 'coffin.svg', 'discovery.svg', 'finbond.svg',
    'fnb.svg', 'Investec.svg', 'investor.svg', 'nedbank-1.svg', 'nedbank-2.svg',
    'phone.svg', 'resbank.svg', 'robot.svg', 'sasfin.svg', 'standardbank.svg',
    'Tyme-1.svg', 'Tyme-2.svg'
]

white_rect = '<rect width="500" height="500" fill="white"/>'

for svg_file in svg_files:
    if not os.path.exists(svg_file):
        print(f"Skipping {svg_file} - not found")
        continue
    
    with open(svg_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if white background already exists
    if 'width="500" height="500" fill="white"' in content or 'fill="white"/>' in content:
        print(f"Skipping {svg_file} - appears to already have white background")
        continue
    
    # Find the first occurrence of either </defs>, </sodipodi:namedview>, or first <g tag
    patterns = [
        (r'(</defs>)', r'\1\n' + white_rect),
        (r'(</sodipodi:namedview>)', r'\1\n' + white_rect),
        (r'(<g[\s>])', white_rect + r'\n\1'),
        (r'(<polygon[\s>])', white_rect + r'\n\1'),
        (r'(<path[\s>])', white_rect + r'\n\1'),
        (r'(<image[\s>])', white_rect + r'\n\1'),
        (r'(<title[\s>])', white_rect + r'\n\1'),
    ]
    
    modified = False
    for pattern, replacement in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content, count=1)
            modified = True
            break
    
    if modified:
        with open(svg_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Added white background to {svg_file}")
    else:
        print(f"✗ Could not find insertion point for {svg_file}")

print("\nDone!")
