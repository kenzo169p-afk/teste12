from bs4 import BeautifulSoup

filepath = r"c:\Users\gordo\Desktop\teste\teste12\topchoicecorretora\index.html"

try:
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Parse with html.parser which automatically fixes missing closing tags and structural issues
    soup = BeautifulSoup(html_content, 'html.parser')

    # Re-serialize the fixed HTML
    fixed_html = str(soup)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_html)
    
    print("HTML errors corrected successfully.")
except Exception as e:
    print(f"Error: {e}")
