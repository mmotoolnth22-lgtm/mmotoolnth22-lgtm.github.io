import os
import datetime
import re

# --- CONFIGURATION ---
BLOG_DIR = "blog"
BASE_TEMPLATE_PATH = "index.html" 
SITE_URL = "https://d2down.com"

# Blog Data
BLOG_POSTS = [
    # --- YOUTUBE ---
    {
        "slug": "how-to-download-youtube-4k",
        "title": "How to Download YouTube Videos in 4K (2026 Guide)",
        "description": "Learn the easiest way to download high-quality 4K and 8K videos from YouTube for free using d2down. No software required.",
        "date": "2026-02-06",
        "content": """
            <h2>Why Download in 4K?</h2>
            <p>4K resolution (3840 x 2160 pixels) offers four times the detail of Full HD (1080p). Watching travel vlogs, movie trailers, or gaming content in 4K creates an immersive experience. However, streaming 4K requires a very fast and stable internet connection. Downloading these videos ensures you can watch them buffer-free, anytime, anywhere.</p>

            <h2>Step 1: Get the Video Link</h2>
            <p>Go to YouTube and open the video you want to save. Click the <strong>Share</strong> button and select <strong>Copy Link</strong>. Alternatively, you can just copy the URL from your browser's address bar.</p>

            <h2>Step 2: Paste into d2down</h2>
            <p>Navigate to <a href="https://d2down.com">d2down.com</a>. You will see a large input box at the top of the page. Right-click and select <strong>Paste</strong> (or press Ctrl+V) to insert the link.</p>

            <h2>Step 3: Select Quality & Download</h2>
            <p>Click the <strong>Download</strong> button. Our system will analyze the video and present you with various download options. Look for the "Video (2160p 4K)" or "Video (WebM 4K)" option. Click the download button next to it, and your file will be saved to your device instantly.</p>
        """
    },
    {
        "slug": "youtube-shorts-downloader-guide",
        "title": "YouTube Shorts Downloader: Save Shorts to Gallery",
        "description": "Step-by-step guide to download YouTube Shorts videos to your mobile gallery or PC. Keep your favorite funny clips offline.",
        "date": "2026-02-06",
        "content": """
            <h2>What are YouTube Shorts?</h2>
            <p>YouTube Shorts are vertical videos up to 60 seconds long, similar to TikTok. While they are great for quick entertainment, YouTube doesn't offer a direct download button for offline viewing.</p>

            <h2>How to Save Shorts with d2down</h2>
            <ol>
                <li>Open the YouTube app or website and find the Short you want.</li>
                <li>Tap the <strong>Share</strong> icon (usually an arrow).</li>
                <li>Tap <strong>Copy Link</strong>.</li>
                <li>Go to <a href="https://d2down.com/youtube-video-downloader.html">d2down YouTube Downloader</a>.</li>
                <li>Paste the link and hit Download.</li>
            </ol>
            <p>The video will be saved as a high-quality MP4 file directly to your phone's gallery or computer's downloads folder.</p>
        """
    },
    {
        "slug": "convert-youtube-to-mp3-safe",
        "title": "Best Safe YouTube to MP3 Converter Online",
        "description": "Convert YouTube videos to MP3 audio files safely without viruses or pop-ups. High quality 320kbps audio extraction.",
        "date": "2026-02-06",
        "content": """
            <h2>Safety First</h2>
            <p>Many "YouTube to MP3" sites are filled with malicious ads and pop-ups. d2down is committed to being a clean, safe tool. We do not host malware or force you to install software.</p>

            <h2>Extracting Audio High Quality</h2>
            <p>To get the best sound quality for music or podcasts:</p>
            <ul>
                <li>Paste your video link into d2down.</li>
                <li>Wait for the options to load.</li>
                <li>Look for the <strong>Audio</strong> tab or section.</li>
                <li>Select <strong>MP3</strong> (best for compatibility) or <strong>M4A</strong> (often better quality at lower file size).</li>
            </ul>
        """
    },

    # --- TIKTOK ---
    {
        "slug": "remove-tiktok-watermark-online",
        "title": "How to Download TikTok Videos Without Watermark",
        "description": "Want to save TikToks without the annoying logo? Here is how to download clean TikTok videos for reposting or archiving.",
        "date": "2026-02-06",
        "content": """
            <h2>The Problem with Watermarks</h2>
            <p>TikTok automatically adds a bouncing watermark to every downloaded video. This looks unprofessional if you want to share it on other platforms like Instagram Reels.</p>

            <h2>How d2down Removes It</h2>
            <p>d2down fetches the raw video file directly from the server before the watermark overlay is applied. This method is 100% free and requires no login.</p>

            <h2>Instructions</h2>
            <ol>
                <li>Copy the TikTok video link.</li>
                <li>Paste it into <a href="https://d2down.com/tiktok-video-downloader.html">d2down TikTok Downloader</a>.</li>
                <li>Click <strong>Download</strong> and wait a few seconds.</li>
                <li>Your clean video will start downloading automatically.</li>
            </ol>
        """
    },
    {
        "slug": "download-tiktok-sound-mp3",
        "title": "Download TikTok Sound & Music (MP3)",
        "description": "Found a trending song on TikTok? Learn how to extract just the audio (MP3) from any TikTok video easily.",
        "date": "2026-02-06",
        "content": """
            <h2>Trending TikTok Sounds</h2>
            <p>TikTok is famous for its viral sounds and remixes. Sometimes you just want the audio to use as a ringtone or in your own video edit.</p>

            <h2>Extracting MP3 from TikTok</h2>
            <p>Using d2down, you don't have to download the whole video. Just paste the link, and in the download options, look for the <strong>Audio / MP3</strong> button. This will rip just the sound track in high quality.</p>
        """
    },

    # --- FACEBOOK ---
    {
        "slug": "download-facebook-private-videos",
        "title": "Download Facebook Private Videos - Step by Step",
        "description": "Downloading public Facebook videos is easy, but what about private ones? Follow this guide to save private videos safely.",
        "date": "2026-02-06",
        "content": """
            <h2>What are Private Videos?</h2>
            <p>Private videos on Facebook are restricted to specific audiences. Standard downloaders scan public URLs, so they cannot see these videos.</p>

            <h2>The Safe Way to Save Public Content</h2>
            <p>For any public Reel, Story, or Post:</p>
            <ul>
                <li><strong>Copy the Link:</strong> Click the three dots on the post and select "Copy link".</li>
                <li><strong>Use d2down:</strong> Paste it into our <a href="https://d2down.com/facebook-video-downloader.html">Facebook Downloader</a>.</li>
                <li><strong>Save:</strong> Download in HD quality.</li>
            </ul>
        """
    },
    {
        "slug": "save-facebook-reels-ios-android",
        "title": "How to Save Facebook Reels to iPhone & Android",
        "description": "Facebook Reels are taking over. Here is the ultimate guide to saving them to your phone's camera roll.",
        "date": "2026-02-06",
        "content": """
            <h2>Facebook Reels vs Stories</h2>
            <p>Reels are permanent short videos, while Stories disappear after 24 hours. Both can be downloaded using d2down.</p>

            <h2>Downloading on Mobile</h2>
            <p>You don't need a specific app from the App Store. Just use your browser (Safari on iPhone, Chrome on Android):</p>
            <ol>
                <li>Copy the Reel link from the Facebook App.</li>
                <li>Open <strong>d2down.com</strong> in your mobile browser.</li>
                <li>Paste and Download.</li>
                <li>On iPhone, tap 'Share' > 'Save Video' once the file opens to save it to Photos.</li>
            </ol>
        """
    },

    # --- DOUYIN ---
    {
        "slug": "download-douyin-no-watermark",
        "title": "Download Douyin (Chinese TikTok) Without Watermark",
        "description": "Access the original high-quality videos from Douyin without the logo. Essential guide for content creators.",
        "date": "2026-02-06",
        "content": """
            <h2>What is Douyin?</h2>
            <p>Douyin is the Chinese version of TikTok. It often has advanced editing trends before they reach the global market. Downloading these videos is great for inspiration.</p>

            <h2>Douyin vs TikTok Links</h2>
            <p>Douyin links often contain Chinese text. d2down is smart enough to extract just the URL. Just copy the whole text from the 'Share' menu in Douyin and paste it into our tool. We will handle the rest.</p>
        """
    },
    {
        "slug": "douyin-video-downloader-online",
        "title": "Douyin Video Downloader Online - No App Needed",
        "description": "Don't install shady APKs. Use our online web tool to download Douyin videos safely and quickly.",
        "date": "2026-02-06",
        "content": """
            <h2>Why Use an Online Tool?</h2>
            <p>Installing random APKs or apps to download Chinese videos can be a security risk. d2down works entirely in your browser (sandboxed), ensuring no malicious code touches your device.</p>

            <h2>High Speed from Anywhere</h2>
            <p>We use high-speed servers to bridge the connection to Douyin, so you get fast download speeds even if you are outside China.</p>
        """
    },

    # --- INSTAGRAM ---
    {
        "slug": "download-instagram-stories-anonymous",
        "title": "Download Instagram Stories Anonymously",
        "description": "View and download Instagram Stories without the user knowing. Save photos and videos from IG anonymously.",
        "date": "2026-02-06",
        "content": """
            <h2>Anonymous Viewing</h2>
            <p>When you view a Story on Instagram, your name appears in the viewer list. However, if you use d2down to download it via the link, the user won't know!</p>
            
            <h2>How to do it?</h2>
            <p>Note: You need the link to the story. If you can get the link (e.g. from a friend sharing it or browser url), paste it here to download the video file directly.</p>
        """
    },
    {
        "slug": "save-instagram-reels-audio",
        "title": "Save Instagram Reels Audio & Video",
        "description": "Download Instagram Reels with original audio. Perfect for creators looking to reuse trending audio.",
        "date": "2026-02-06",
        "content": """
            <h2>Reels are the Future</h2>
            <p>Instagram is pushing Reels hard. Saving them allows you to watch offline or share them on WhatsApp/Telegram easily.</p>

            <h2>Original Quality</h2>
            <p>d2down saves the MP4 file exactly as it is on Instagram's servers. No re-compression, no quality loss.</p>
        """
    }
]

def generate_blog_post(post):
    try:
        # UPDATED: Use relative path (current dir)
        with open(BASE_TEMPLATE_PATH, "r", encoding="utf-8") as f:
            template = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find base template at {BASE_TEMPLATE_PATH}")
        return

    # 1. Update Title and Meta
    template = re.sub(r'<title>.*?</title>', f'<title>{post["title"]} - d2down Blog</title>', template)
    template = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{post["description"]}">', template)
    
    # 2. Update Canonical
    template = re.sub(r'<link rel="canonical".*?>', f'<link rel="canonical" href="{SITE_URL}/blog/{post["slug"]}.html">', template)

    # 3. Clean up Main Content
    blog_content_html = f"""
    <div class="blog-container" style="max-width: 800px; margin: 0 auto; padding: 40px 20px; text-align: left;">
        <nav style="margin-bottom: 20px; font-size: 0.9rem;">
            <a href="../index.html" style="color: #6366f1; text-decoration: none;">← Back to Home</a>
        </nav>
        
        <article class="prose lg:prose-xl">
            <h1 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem; color: #1e293b; line-height: 1.2;">{post['title']}</h1>
            <p style="color: #64748b; margin-bottom: 2rem;">Published on {post['date']}</p>
            
            <div class="content" style="line-height: 1.8; color: #334155;">
                {post['content']}
            </div>
        </article>

        <div style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid #e2e8f0; text-align: center;">
            <h3 style="margin-bottom: 1rem;">Ready to try it?</h3>
            <a href="../index.html" style="background: #2563eb; color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; display: inline-block;">Go to Downloader</a>
        </div>
    </div>
    """
    
    pattern = re.compile(r'<main>.*?</main>', re.DOTALL)
    template = re.sub(pattern, f'<main>{blog_content_html}</main>', template)
    
    if blog_content_html not in template:
         pattern = re.compile(r'<main[^>]*>.*?</main>', re.DOTALL)
         template = re.sub(pattern, f'<main>{blog_content_html}</main>', template)

    # Fix Relative Links
    template = template.replace('href="style.css', 'href="../style.css')
    template = template.replace('href="index.html"', 'href="../index.html"')
    template = template.replace('src="app.js"', 'src="../app.js"')
    template = template.replace('src="script.js"', 'src="../script.js"')
    
    nav_links = ["about.html", "terms.html", "privacy.html", "contact.html", "desktop-app.html"]
    for link in nav_links:
        template = template.replace(f'href="{link}"', f'href="../{link}"')
    
    # Ensure blog directory exists (redundant check but safe)
    if not os.path.exists(BLOG_DIR):
        os.makedirs(BLOG_DIR)

    with open(f"{BLOG_DIR}/{post['slug']}.html", "w", encoding="utf-8") as f:
        f.write(template)
    print(f"Generated {post['slug']}.html")

def update_sitemap():
    try:
        # UPDATED: Use relative path (current dir)
        with open("sitemap.xml", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Warning: sitemap.xml not found. Run generating seo pages first.")
        return

    new_entries = ""
    for post in BLOG_POSTS:
        url = f"{SITE_URL}/blog/{post['slug']}.html"
        if url not in content:
            new_entries += f"""
  <url>
    <loc>{url}</loc>
    <lastmod>{post['date']}</lastmod>
    <priority>0.7</priority>
  </url>"""

    if new_entries:
        if "</urlset>" in content:
             content = content.replace("</urlset>", f"{new_entries}\n</urlset>")
             with open("sitemap.xml", "w", encoding="utf-8") as f:
                 f.write(content)
             print("Updated sitemap.xml with blog posts.")
        else:
            print("Error: Could not find </urlset> closing tag.")
    else:
        print("Sitemap already up to date with blog posts.")

def main():
    if not os.path.exists(BLOG_DIR):
        os.makedirs(BLOG_DIR)
        
    for post in BLOG_POSTS:
        generate_blog_post(post)
    
    # Update sitemap
    update_sitemap()
        
if __name__ == "__main__":
    main()
