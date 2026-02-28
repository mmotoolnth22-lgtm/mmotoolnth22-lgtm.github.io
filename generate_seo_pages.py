import os
import datetime
import re

# --- CONFIGURE SEO PAGES ---
BASE_TEMPLATE = "index.html"
OUTPUT_DIR = "."
SITE_URL = "https://d2down.com"

# Define the pages to generate
# Structure: (filename, keyword, h1_title, description, article_topic)
PAGES = [
    {
        "filename": "youtube-video-downloader.html",
        "keyword": "YouTube Video Downloader",
        "h1": "Free Online YouTube Video Downloader",
        "title": "YouTube Video Downloader - Download HD, 4K, 1080p MP4",
        "description": "Free YouTube video downloader online - Save videos in HD, 4K, MP4, WebM, MP3 formats. Download entire playlists, extract audio, no software installation needed. 100% free and unlimited downloads.",
        "topic": "YouTube"
    },
    {
        "filename": "youtube-playlist-downloader-online.html",
        "keyword": "YouTube Playlist Downloader",
        "h1": "Download Entire YouTube Playlists Online",
        "title": "YouTube Playlist Downloader - Save Full Channels & Mixes",
        "description": "Best YouTube Playlist Downloader based on yt-dlp. Download hundreds of videos from a playlist or channel in one click. Supports bulk MP3 conversion and 4K video downloads.",
        "topic": "YouTube Playlists"
    },
    {
        "filename": "youtube-to-mp3-converter.html",
        "keyword": "YouTube to MP3",
        "h1": "Convert YouTube to MP3 (High Quality 320kbps)",
        "title": "YouTube to MP3 Converter - Fast, Free, No Limits",
        "description": "Convert YouTube videos to MP3 audio instantly. Extract high-quality audio (320kbps) from music videos, podcasts, and lectures. Safe, fast, and no registration required.",
        "topic": "YouTube to MP3 Conversion"
    },
    {
        "filename": "4k-youtube-downloader.html",
        "keyword": "4K YouTube Downloader",
        "h1": "Download YouTube Videos in 4K & 8K HDR",
        "title": "4K YouTube Downloader - 2160p 60fps support",
        "description": "Download ultra-high definition videos from YouTube. Support for 4K, 5K, and 8K resolution downloads. Preserve original quality with high framerates (60fps/120fps).",
        "topic": "4K Video"
    },
    {
        "filename": "facebook-video-downloader.html",
        "keyword": "Facebook Video Downloader",
        "h1": "Download Facebook Videos (Public & Private)",
        "title": "Facebook Video Downloader - Save FB Reels & Stories",
        "description": "Easily download videos from Facebook to your device. Supports Facebook Reels, Watch videos, Live streams, and Private group videos. MP4 Quality.",
        "topic": "Facebook"
    },
    {
        "filename": "tiktok-video-downloader.html",
        "keyword": "TikTok Video Downloader",
        "h1": "TikTok Downloader Without Watermark",
        "title": "TikTok Video Downloader - No Watermark, HD Quality",
        "description": "Download TikTok videos without the watermark. Save high-quality MP4 videos from TikTok to your mobile or PC. Completely free and unlimited.",
        "topic": "TikTok"
    },
    {
        "filename": "instagram-video-downloader.html",
        "keyword": "Instagram Downloader",
        "h1": "Download Instagram Reels, Stories & Photos",
        "title": "Instagram Video Downloader - Save IG Reels & IGTV",
        "description": "All-in-one Instagram Downloader. Save Instagram Videos, Reels, Stories, and Photos (Carousel) directly to your gallery. Anonymous and secure downloading.",
        "topic": "Instagram"
    },
    {
        "filename": "reddit-video-downloader.html",
        "keyword": "Reddit Video Downloader",
        "h1": "Reddit Video Downloader with Audio",
        "title": "Reddit Video Downloader - Save Reddit with Sound",
        "description": "Download Reddit videos with audio embedded. Fix the common 'no sound' issue. Supports downloading GIFs and videos from any subreddit.",
        "topic": "Reddit"
    },
    {
        "filename": "twitter-video-downloader.html",
        "keyword": "Twitter Video Downloader",
        "h1": "Download Twitter (X) Videos & GIFs",
        "title": "Twitter Video Downloader - Save X.com Videos",
        "description": "Download videos and GIFs from Twitter (X.com). Save funny clips, news, and sports highlights in MP4 format directly to your phone or computer.",
        "topic": "Twitter"
    },
    {
        "filename": "youtube-1080p-download.html",
        "keyword": "YouTube Download 1080p",
        "h1": "Download YouTube Videos in Full HD 1080p",
        "title": "YouTube 1080p Downloader - Crisp Full HD Quality",
        "description": "Download YouTube videos in 1080p Full HD. Ensure crisp quality for all your offline viewing. Supports high bitrate and 60fps downloads.",
        "topic": "1080p Video"
    },
    {
        "filename": "dailymotion-video-downloader.html",
        "keyword": "Dailymotion Download",
        "h1": "Dailymotion Video Downloader",
        "title": "Dailymotion Downloader - Save Videos Offline",
        "description": "Download videos from Dailymotion easily. Support for playlists and long videos. Fast extraction speed and multiple format options.",
        "topic": "Dailymotion"
    },
    {
        "filename": "bilibili-video-downloader.html",
        "keyword": "Bilibili Download",
        "h1": "Bilibili Video Downloader (HD)",
        "title": "Bilibili Downloader - Download Anime & Content",
        "description": "Download videos from Bilibili.tv and Bilibili.com. Save high-quality anime, gaming clips, and AMVs with original subtitles and audio.",
        "topic": "Bilibili"
    },
    {
        "filename": "netflix-downloader-tool.html",
        "keyword": "Netflix Download",
        "h1": "Netflix Video Downloader Tool",
        "title": "Netflix Video Downloader - Save Clips & Trailers",
        "description": "Tool to help download non-DRM clips and trailers from Netflix related sources. Note: Use responsibly for personal archiving of allowed content.",
        "topic": "Netflix"
    },
    {
        "filename": "douyin-video-downloader.html",
        "keyword": "Douyin Download",
        "h1": "Douyin (Chinese TikTok) Downloader",
        "title": "Douyin Downloader - No Watermark HD",
        "description": "Download videos/images from Douyin (Chinese TikTok) without watermark. High speed server for users outside China.",
        "topic": "Douyin"
    },
    {
        "filename": "soundcloud-to-mp3.html",
        "keyword": "SoundCloud Download",
        "h1": "SoundCloud to MP3 Downloader",
        "title": "SoundCloud Downloader - Save Music Tracks",
        "description": "Download music and tracks from SoundCloud. Convert SoundCloud links to MP3 320kbps. Build your offline music library easily.",
        "topic": "SoundCloud"
    },
    {
        "filename": "tai-video-youtube-mien-phi.html",
        "keyword": "Tải Video Youtube Miễn Phí",
        "h1": "Tải Video Youtube Miễn Phí Tốc Độ Cao",
        "title": "Tải Video Youtube - Công cụ tải nhạc, video miễn phí",
        "description": "Công cụ tải video Youtube miễn phí tốt nhất Việt Nam. Hỗ trợ tải MP3, MP4, 4K, Full HD. Tải video từ Facebook, TikTok không logo, nhanh chóng và đơn giản.",
        "topic": "YouTube"
    }
]

def generate_seo_link_grid(current_filename=""):
    """Generates the HTML grid of links, highlighting the current one."""
    html = '<div class="seo-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 10px; font-size: 0.8rem; text-align: left; margin-top: 1rem;">\n'
    
    # Add Index (Home) link
    if current_filename == "index.html":
         html += f'    <a href="index.html" style="color: #fff; font-weight: bold; text-decoration: none;">🏠 Home</a>\n'
    else:
         html += f'    <a href="index.html" style="color: #ccc; text-decoration: none; transition: color 0.2s;">🏠 Home</a>\n'

    for page in PAGES:
        color = "#fff" if page['filename'] == current_filename else "#ccc"
        weight = "bold" if page['filename'] == current_filename else "normal"
        html += f'    <a href="{page["filename"]}" style="color: {color}; font-weight: {weight}; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color=\'#fff\'" onmouseout="this.style.color=\'{color}\'">{page["keyword"]}</a>\n'
    
    html += '</div>'
    return html

def generate_dummy_article(topic, keyword):
    """Generates a placeholder article structure better than generic text."""
    return f"""
    <div class="prose max-w-none text-left mb-12">
        <h2 class="text-2xl font-bold text-slate-800 mb-4">How to Download {topic} Videos Online?</h2>
        <p class="text-slate-600 mb-4">
            Looking for a reliable way to download <strong>{topic}</strong> content? You are in the right place. 
            Our <strong>{keyword}</strong> tool is designed to be the fastest and most secure way to save your media offline.
        </p>
        <h3 class="text-xl font-semibold text-slate-800 mb-3">Key Features</h3>
        <ul class="list-disc pl-5 space-y-2 text-slate-600 mb-6">
            <li><strong>No Watermark:</strong> High quality downloads without annoying logos.</li>
            <li><strong>High Speed:</strong> Direct connection to {topic} servers.</li>
            <li><strong>Multiple Formats:</strong> Support for MP4, MP3, and HD resolutions.</li>
            <li><strong>Free Forever:</strong> No registration or fees required.</li>
        </ul>
        <h3 class="text-xl font-semibold text-slate-800 mb-3">Step-by-Step Guide</h3>
        <ol class="list-decimal pl-5 space-y-2 text-slate-600">
            <li>Copy the link of the {topic} video you want to download.</li>
            <li>Paste the URL into the input box above.</li>
            <li>Click the "Download" button and wait for the options to appear.</li>
            <li>Select your preferred quality and click download.</li>
        </ol>
    </div>
    """

def get_faq_schema():
    """Returns a generic FAQ schema for the tool."""
    return """
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "How do I download videos?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Simply paste the URL into the box and click 'Download'. Then select your quality."
        }
      }, {
        "@type": "Question",
        "name": "Is this service free?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, it is 100% free and requires no software installation."
        }
      }, {
        "@type": "Question",
        "name": "Is it safe to use?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, we do not store any of your data or downloaded videos."
        }
      }]
    }
    </script>
    """

def create_sitemap():
    """Generates the sitemap.xml file automatically."""
    print("Generating sitemap.xml...")
    today = datetime.date.today().isoformat()
    
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # Add Home
    xml_content += f'  <url>\n    <loc>{SITE_URL}/index.html</loc>\n    <lastmod>{today}</lastmod>\n    <priority>1.0</priority>\n  </url>\n'
    
    # Add Pages
    for page in PAGES:
        xml_content += f'  <url>\n    <loc>{SITE_URL}/{page["filename"]}</loc>\n    <lastmod>{today}</lastmod>\n    <priority>0.8</priority>\n  </url>\n'
        
    xml_content += '</urlset>'
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml_content)
    print("sitemap.xml created.")

def main():
    print("Starting SEO Page Generation (Enhanced)...")
    
    # 1. Read the Template (Index.html)
    try:
        with open(BASE_TEMPLATE, "r", encoding="utf-8") as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"Error: {BASE_TEMPLATE} not found!")
        return

    # 2. Process Index.html
    print("Updating index.html footer links...")
    links_html = generate_seo_link_grid("index.html")
    if '<div class="seo-pages-links"' in template_content:
        pattern = re.compile(r'(<div class="seo-pages-links"[^>]*>).*?(</div>)', re.DOTALL)
        new_index_content = re.sub(pattern, f'\\1\n{links_html}\n\\2', template_content)
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(new_index_content)
    else:
        # First run injection if needed
        # Assuming user responsible for initial div placement or we just skip for now as per previous logic
        pass

    # 3. Generate Other Pages
    for page in PAGES:
        print(f"Generating {page['filename']}...")
        
        new_content = template_content # Start with fresh copy
        
        # A. Basic Replacements
        new_content = re.sub(r'<title>.*?</title>', f'<title>d2down.com - {page["title"]}</title>', new_content)
        new_content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="d2down.com - {page["description"]}">', new_content)
        new_content = re.sub(r'<h1>.*?</h1>', f'<h1>{page["h1"]}</h1>', new_content)
        new_content = re.sub(r'<p class="subtitle">.*?</p>', f'<p class="subtitle">{page["description"]}</p>', new_content)

        # B. Social Meta Tags (Open Graph / Twitter)
        og_tags = f"""
    <meta property="og:type" content="website">
    <meta property="og:url" content="{SITE_URL}/{page['filename']}">
    <meta property="og:title" content="{page['title']}">
    <meta property="og:description" content="{page['description']}">
    <meta property="og:image" content="{SITE_URL}/images/og-image.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{page['title']}">
    <meta name="twitter:description" content="{page['description']}">
        """
        if "</head>" in new_content:
            new_content = new_content.replace("</head>", f'{og_tags}\n</head>')

        # C. Inject Canonical Tag
        canonical_tag = f'<link rel="canonical" href="{SITE_URL}/{page["filename"]}">'
        if "</head>" in new_content:
            new_content = new_content.replace("</head>", f'{canonical_tag}\n</head>')

        # D. Inject Schema Markup (JSON-LD + FAQ)
        schema_markup = f"""
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "{page['keyword']}",
      "operatingSystem": "Web",
      "applicationCategory": "MultimediaApplication",
      "offers": {{
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }},
      "description": "{page['description']}"
    }}
    </script>
    {get_faq_schema()}
        """
        if "</body>" in new_content:
            new_content = new_content.replace("</body>", f'{schema_markup}\n</body>')

        # E. Rich Content Injection
        article_html = generate_dummy_article(page.get('topic', 'Video'), page['keyword'])
        if '<!-- SEO_CONTENT_MARKER -->' in new_content:
            new_content = new_content.replace('<!-- SEO_CONTENT_MARKER -->', article_html)

        # F. Inject Footer Links
        links_html = generate_seo_link_grid(page['filename'])
        if '<div class="seo-pages-links"' in new_content:
            pattern = re.compile(r'(<div class="seo-pages-links"[^>]*>).*?(</div>)', re.DOTALL)
            new_content = re.sub(pattern, f'\\1\n{links_html}\n\\2', new_content)
        
        # Write File
        with open(page['filename'], "w", encoding="utf-8") as f:
            f.write(new_content)

    # 4. Create Sitemap
    create_sitemap()
    print(f"Successfully generated {len(PAGES)} SEO pages with Advanced SEO features!")

if __name__ == "__main__":
    main()
