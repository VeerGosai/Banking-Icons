#!/usr/bin/env python3
import os
import re

# List of SVG files to resize
svg_files = [
    'Absa.svg', 'Access.svg', 'Africanbank.svg', 'bank-zero.svg', 'Bank.svg',
    'bidvest.svg', 'Call-Center.svg', 'Capitec-1.svg', 'Capitec-2.svg',
    'Capitec-Business-1.svg', 'coffin.svg', 'discovery.svg', 'finbond.svg',
    'fnb.svg', 'Investec.svg', 'investor.svg', 'nedbank-1.svg', 'nedbank-2.svg',
    'phone.svg', 'resbank.svg', 'robot.svg', 'sasfin.svg', 'standardbank.svg',
    'Tyme-1.svg', 'Tyme-2.svg'
]

def resize_svg(filename, new_width=700, new_height=700):
    """Resize SVG canvas to 700x700 while keeping content at 500x500 (centered with 100px padding)"""
    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        return False
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace width attribute (handles various formats)
        content = re.sub(
            r'width\s*=\s*["\']?\d+(\.\d+)?(px|pt|mm|cm)?["\']?',
            f'width="{new_width}"',
            content,
            count=1
        )
        
        # Replace height attribute (handles various formats)
        content = re.sub(
            r'height\s*=\s*["\']?\d+(\.\d+)?(px|pt|mm|cm)?["\']?',
            f'height="{new_height}"',
            content,
            count=1
        )
        
        # Update viewBox to maintain 500x500 content centered in 700x700 canvas
        # This adds 100px padding on all sides
        content = re.sub(
            r'viewBox\s*=\s*["\']0\s+0\s+500\s+500["\']',
            'viewBox="-100 -100 700 700"',
            content
        )
        
        # Also handle viewBox without spaces
        content = re.sub(
            r'viewBox\s*=\s*["\']0 0 500 500["\']',
            'viewBox="-100 -100 700 700"',
            content
        )
        
        # Check if any changes were made
        if content == original_content:
            print(f"⚠️  No size attributes found in: {filename}")
            return False
        
        # Write the modified content back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Resized {filename} to {new_width}x{new_height}")
        return True
        
    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")
        return False

def main():
    print("=" * 60)
    print("SVG Resizer - Expanding canvas to 700x700")
    print("Original content remains 500x500 (centered with 100px padding)")
    print("=" * 60)
    print()
    
    success_count = 0
    fail_count = 0
    
    for svg_file in svg_files:
        if resize_svg(svg_file):
            success_count += 1
        else:
            fail_count += 1
    
    print()
    print("=" * 60)
    print(f"Summary: {success_count} successful, {fail_count} failed/skipped")
    print("=" * 60)

if __name__ == "__main__":
    main()
