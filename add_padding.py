import os
import re

# All SVG files except the excluded ones
svg_files = [
    'Access.svg', 'Africanbank.svg', 'bank-zero.svg', 'Bank.svg',
    'bidvest.svg', 'Call-Center.svg', 'Capitec-1.svg', 'Capitec-2.svg',
    'Capitec-Business-1.svg', 'coffin.svg', 'finbond.svg',
    'Investec.svg', 'investor.svg', 'nedbank-1.svg', 'nedbank-2.svg',
    'phone.svg', 'resbank.svg', 'robot.svg', 'sasfin.svg', 'standardbank.svg',
    'Tyme-1.svg', 'Tyme-2.svg'
]

for svg_file in svg_files:
    if not os.path.exists(svg_file):
        print(f"Skipping {svg_file} - not found")
        continue
    
    with open(svg_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update width and height attributes to 700
    content = re.sub(r'width="500"', 'width="700"', content)
    content = re.sub(r'height="500"', 'height="700"', content)
    
    # Update the white background rect to 700x700
    content = re.sub(r'<rect width="500" height="500" fill="white"/>', 
                     '<rect width="700" height="700" fill="white"/>', content)
    
    # Add a group wrapper with transform to center the original 500x500 content
    # Find where to insert the group - after the white rect
    if '<rect width="700" height="700" fill="white"/>' in content:
        # Find the position after the white rect
        rect_end = content.find('<rect width="700" height="700" fill="white"/>') + len('<rect width="700" height="700" fill="white"/>')
        
        # Find the closing </svg> tag
        svg_close = content.rfind('</svg>')
        
        # Extract the content between rect and closing svg
        middle_content = content[rect_end:svg_close]
        
        # Wrap it in a group with translation
        wrapped_content = f'\n<g transform="translate(100, 100)">{middle_content}</g>\n'
        
        # Reconstruct the file
        content = content[:rect_end] + wrapped_content + '</svg>\n'
        
        with open(svg_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Added 100px padding to {svg_file}")
    else:
        print(f"✗ Could not find white background rect in {svg_file}")

print("\nDone!")
