import os
import glob
from bs4 import BeautifulSoup
from collections import defaultdict

base_dir = r"C:\Users\Windows\.gemini\antigravity\scratch\mmotoolnth22-lgtm.github.io-main"
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)

DOMAIN = "https://d2down.com"

# Phân loại file theo basename để build Hreflang network.
# Ví dụ: "youtube-video-downloader.html" có tồn tại ở root (en), ở vi/, ở fr/, v.v.
file_map = defaultdict(dict)

# Map folder name to correct iso code
iso_fix = {"jp": "ja-JP", "kr": "ko-KR"}

for path in html_files:
    rel_path = os.path.relpath(path, base_dir).replace("\\", "/")
    parts = rel_path.split("/")
    filename = parts[-1]
    
    if len(parts) == 1:
        lang = "en"
        url = f"{DOMAIN}/{filename}"
    else:
        lang = parts[0]
        url = f"{DOMAIN}/{lang}/{filename}"
        
    iso_lang = iso_fix.get(lang, lang)
    file_map[filename][iso_lang] = url


count = 0
for path in html_files:
    rel_path = os.path.relpath(path, base_dir).replace("\\", "/")
    parts = rel_path.split("/")
    filename = parts[-1]
    
    if len(parts) == 1:
        lang = "en"
        canonical_url = f"{DOMAIN}/{filename}"
    else:
        lang = parts[0]
        canonical_url = f"{DOMAIN}/{lang}/{filename}"

    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    updated = False
    head = soup.head
    if head:
        # Xóa sạch canonical và hreflang rác/cũ nếu có
        for link in head.find_all("link", rel="canonical"):
            link.decompose()
        for link in head.find_all("link", rel="alternate", hreflang=True):
            link.decompose()
            
        # 1. Bơm Canonical mới
        canonical_tag = soup.new_tag("link", rel="canonical", href=canonical_url)
        head.append(canonical_tag)
        
        # 2. Xây cọc Hreflang
        # x-default luôn trỏ về bản tiếng Anh (Root)
        en_url = file_map[filename].get("en", f"{DOMAIN}/{filename}")
        xdefault_tag = soup.new_tag("link", rel="alternate", hreflang="x-default", href=en_url)
        head.append(xdefault_tag)
        
        # 3. Tiêm toàn bộ các mạng lưới ngôn ngữ khác
        for l_code, l_url in file_map[filename].items():
            href_tag = soup.new_tag("link", rel="alternate", hreflang=l_code, href=l_url)
            head.append(href_tag)
            
        updated = True
        
    if updated:
        with open(path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        count += 1
            
print(f"[+] Hreflang Network & Canonical đã cắm cọc thành công xuống {count} file HTML! Các Màng Nhện SEO đã được nối kín kẽ.")

