import os
import re

TEMPLATE_FILE = "index.html"

LEGAL_PAGES = [
    {
        "filename": "about.html",
        "title": "d2down.com - About Us",
        "h1": "About Us",
        "content": """
            <div class="legal-content" style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 12px; text-align: left; color: #eee; line-height: 1.6;">
                <p>Welcome to <strong>d2down.com</strong>, the web's most convenient tool for saving online videos.</p>
                <p>Our mission is to provide a fast, free, and secure way for users to download content for offline viewing. Whether it's a tutorial, a music video, or a funny clip, our tool helps you keep it on your device.</p>
                <p>We believe in an open internet where content is accessible. However, we strictly advocate for the <strong>legal and ethical use</strong> of this technology.</p>
                <h3>Copyright & Ethics</h3>
                <p><strong>Strictly Prohibited:</strong> We forbid the use of our tool to download copyrighted material for distribution, sale, or any commercial purpose without the explicit permission of the content creator.</p>
                <p>We respect the intellectual property rights of others and expect our users to do the same.</p>
            </div>
        """
    },
    {
        "filename": "terms.html",
        "title": "d2down.com - Terms of Service",
        "h1": "Terms of Service",
        "content": """
            <div class="legal-content" style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 12px; text-align: left; color: #eee; line-height: 1.6;">
                <p>By accessing or using this website, you agree to be bound by these Terms of Service.</p>
                <h3>1. Proper Use</h3>
                <p>You agree to use this service only for personal, non-commercial purposes. Any commercial use of the downloaded content is strictly prohibited.</p>
                <h3>2. Copyright Infringement</h3>
                <p style="color: #ffcccc; border-left: 4px solid #ff4444; padding-left: 10px;"><strong>Important:</strong> Downloading copyrighted videos (music videos, movies, protected content) without the copyright holder's permission is ILLEGAL. This tool is designed for downloading public domain content, your own videos, or content under Creative Commons licenses.</p>
                <p>We do not host any video content. All videos are downloaded directly from the content providers (e.g., YouTube, TikTok) servers.</p>
                <h3>3. Disclaimer</h3>
                <p>We are not responsible for any misuse of this tool. The user assumes full responsibility for any copyright violations.</p>
            </div>
        """
    },
    {
        "filename": "privacy.html",
        "title": "d2down.com - Privacy Policy",
        "h1": "Privacy Policy",
        "content": """
            <div class="legal-content" style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 12px; text-align: left; color: #eee; line-height: 1.6;">
                <p>Your privacy is important to us. This Privacy Policy explains how we handle your data.</p>
                <h3>Data Collection</h3>
                <p><strong>We do NOT collect personally identifiable information.</strong> We do not require registration or login.</p>
                <h3>Log Data</h3>
                <p>Like most websites, we may collect standard log information (IP address, browser type) for analytics and debugging purposes. This data is anonymized where possible.</p>
                <h3>Cookies</h3>
                <p>We use essential cookies to ensure the website functions correctly. We do not use tracking cookies for advertising purposes.</p>
                <h3>External Links</h3>
                <p>Our site allows you to download from third-party platforms. We are not responsible for the privacy practices of those external sites.</p>
            </div>
        """
    },
    {
        "filename": "contact.html",
        "title": "d2down.com - Contact Us",
        "h1": "Contact Us",
        "content": """
            <div class="legal-content" style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 12px; text-align: left; color: #eee; line-height: 1.6;">
                <p>Have questions, suggestions, or need to report an issue?</p>
                <p>We'd love to hear from you. Please reach out to us at:</p>
                <p style="font-size: 1.2rem; font-weight: bold; margin-top: 1rem;">📧 email@example.com</p>
                <p><em>(Please replace with your actual contact email)</em></p>
                <p style="margin-top: 2rem;"><strong>DMCA / Copyright Reports:</strong> If you believe your copyrighted work is being infringed upon, please contact us immediately for takedown requests.</p>
            </div>
        """
    }
]

def main():
    print("Generating Legal Pages...")
    
    try:
        with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
            template = f.read()
    except FileNotFoundError:
        print("Error: index.html not found!")
        return

    # Create the 'clean' template by removing the main downloader card and seo SEO content
    # We want to keep Header, Nav, and Footer
    
    # 1. Regex to find <main>...</main> content and replace it
    # But wait, we want to keep <main> wrapper.
    
    header_part = template.split('<main>')[0] + '<main>'
    footer_part = '</main>' + template.split('</main>')[-1]
    
    for page in LEGAL_PAGES:
        print(f"Creating {page['filename']}...")
        
        # Modify the header title in header_part (simple string replace might be risky if multiple titles, but <title> is in head)
        # 1. Update <title>
        current_header = re.sub(r'<title>.*?</title>', f'<title>{page["title"]}</title>', header_part)
        
        # 2. Update h1 (inside header) -> Actually usually Legal pages have their H1 inside the content area, 
        # but our design has H1 in the global header? No, index.html has H1 in <header>. 
        # Let's clean the global header H1 to be generic "Free Video Downloader" (it is already)
        # We will inject the page specific H1 into the MAIN content area.
        
        full_html = f"{current_header}\n{page['content']}\n{footer_part}"
        
        with open(page['filename'], "w", encoding="utf-8") as f:
            f.write(full_html)
            
    print("Legal pages generated successfully!")

if __name__ == "__main__":
    main()
