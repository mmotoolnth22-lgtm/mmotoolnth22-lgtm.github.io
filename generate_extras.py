import os
import datetime

SITE_URL = "https://d2down.com"

def generate_extras():
    print("Generating sitemap.xml and robots.txt...")
    
    # 1. Get all HTML files (Recursive)
    files = []
    for root, dirs, filenames in os.walk('.'):
        for filename in filenames:
            if filename.endswith('.html'):
                # Get relative path (e.g., "es/index.html")
                rel_path = os.path.relpath(os.path.join(root, filename), '.')
                # Normalize path separators for URL (Windows uses backslash)
                rel_path = rel_path.replace('\\', '/')
                # Skip if it starts with ./
                if rel_path.startswith('./'):
                    rel_path = rel_path[2:]
                files.append(rel_path)
    
    # 2. Generate Sitemap XML
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    today = datetime.date.today().isoformat()
    
    for f in files:
        priority = "1.0" if f == "index.html" else "0.8"
        sitemap_content += f"""  <url>
    <loc>{SITE_URL}/{f}</loc>
    <lastmod>{today}</lastmod>
    <priority>{priority}</priority>
  </url>
"""
    sitemap_content += '</urlset>'
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)
        
    # 3. Generate robots.txt
    robots_content = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(robots_content)

    print(f"Generated sitemap.xml ({len(files)} links) and robots.txt")

if __name__ == "__main__":
    generate_extras()
