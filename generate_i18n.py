import os
import shutil

# 1. Translation Dictionary (Massive Update)
# Note: For many languages, English fallback is used for long descriptions. 
# Ideally, these should be professionally translated.
TRANSLATIONS = {
    'es': {
        'name': 'Español',
        'replacements': {
            'Free Video Downloader': 'Descargador de Video Gratis',
            'Download videos from YouTube, TikTok, Instagram, Facebook, Twitter and 1000+ sites': 'Descarga videos de YouTube, TikTok, Instagram, Facebook y más de 1000 sitios',
            'Paste video link here...': 'Pega el enlace del video aquí...',
            'Download': 'Descargar',
            'Paste from clipboard': 'Pegar desde el portapapeles',
            'Supported Platforms': 'Plataformas Soportadas',
            'Copyrighted content is not available for download with this tool.': 'El contenido con derechos de autor no está disponible para descargar con esta herramienta.',
            'About Us': 'Sobre Nosotros', 'Terms of Service': 'Términos de Servicio', 'Privacy Policy': 'Política de Privacidad', 'Contact': 'Contacto', 'Home': 'Inicio', 'Language': 'Español'
        }
    },
    'fr': {
        'name': 'Français',
        'replacements': {
            'Free Video Downloader': 'Téléchargeur Vidéo Gratuit',
            'Download videos from YouTube, TikTok, Instagram, Facebook, Twitter and 1000+ sites': 'Téléchargez des vidéos de YouTube, TikTok, Instagram, Facebook et plus de 1000 sites',
            'Paste video link here...': 'Collez le lien vidéo ici...',
            'Download': 'Télécharger',
            'Paste from clipboard': 'Coller depuis le presse-papiers',
            'Supported Platforms': 'Plateformes Prises en Charge',
            'Copyrighted content is not available for download with this tool.': 'Le contenu protégé par le droit d\'auteur n\'est pas disponible au téléchargement.',
            'About Us': 'À Propos', 'Terms of Service': 'Conditions d\'Utilisation', 'Privacy Policy': 'Politique de Confidentialité', 'Contact': 'Contact', 'Home': 'Accueil', 'Language': 'Français'
        }
    },
    'vi': {
        'name': 'Tiếng Việt',
        'replacements': {
            'Free Video Downloader': 'Tải Video Miễn Phí',
            'Download videos from YouTube, TikTok, Instagram, Facebook, Twitter and 1000+ sites': 'Tải video từ YouTube, TikTok, Facebook, Instagram và hơn 1000 trang web',
            'Paste video link here...': 'Dán link video vào đây...',
            'Download': 'Tải Xuống',
            'Paste from clipboard': 'Dán từ bộ nhớ tạm',
            'Supported Platforms': 'Nền tảng hỗ trợ',
            'Copyrighted content is not available for download with this tool.': 'Không hỗ trợ tải nội dung có bản quyền bằng công cụ này.',
            'About Us': 'Giới Thiệu', 'Terms of Service': 'Điều Khoản', 'Privacy Policy': 'Chính Sách Riêng Tư', 'Contact': 'Liên Hệ', 'Home': 'Trang Chủ', 'Language': 'Tiếng Việt'
        }
    },
    'ja': { # Fixed code from jp to ja/jp standard
        'name': '日本語',
        'replacements': {
            'Free Video Downloader': '無料ビデオダウンローダー',
            'Download videos from YouTube, TikTok, Instagram, Facebook, Twitter and 1000+ sites': 'YouTube、TikTok、Instagram、Facebookなど1000以上のサイトから動画を保存',
            'Paste video link here...': '動画のリンクをここに貼り付け...',
            'Download': 'ダウンロード',
            'Paste from clipboard': 'クリップボードから貼り付け',
            'Supported Platforms': '対応プラットフォーム',
            'Copyrighted content is not available for download with this tool.': '著作権で保護されたコンテンツはこのツールではダウンロードできません。',
            'About Us': '私たちについて', 'Terms of Service': '利用規約', 'Privacy Policy': 'プライバシーポリシー', 'Contact': 'お問い合わせ', 'Home': 'ホーム', 'Language': '日本語'
        }
    },
    'ko': { # Fixed code from kr to ko
        'name': '한국어',
        'replacements': {
            'Free Video Downloader': '무료 비디오 다운로더',
            'Download videos from YouTube, TikTok, Instagram, Facebook, Twitter and 1000+ sites': 'YouTube, TikTok, Instagram, Facebook 등 1000개 이상의 사이트에서 동영상 다운로드',
            'Paste video link here...': '비디오 링크를 여기에 붙여넣으세요...',
            'Download': '다운로드',
            'Paste from clipboard': '클립보드에서 붙여넣기',
            'Supported Platforms': '지원되는 플랫폼',
            'Copyrighted content is not available for download with this tool.': '저작권이 있는 콘텐츠는 이 도구로 다운로드할 수 없습니다.',
            'About Us': '회사 소개', 'Terms of Service': '서비스 약관', 'Privacy Policy': '개인정보 처리방침', 'Contact': '문의하기', 'Home': '홈', 'Language': '한국어'
        }
    },
    'ru': {
        'name': 'Русский',
        'replacements': {
            'Free Video Downloader': 'Бесплатный загрузчик видео',
            'Download': 'Скачать',
            'Paste video link here...': 'Вставьте ссылку на видео...',
            'Supported Platforms': 'Поддерживаемые платформы',
            'Language': 'Русский'
        }
    },
    'id': {
        'name': 'Bahasa Indonesia',
        'replacements': {
            'Free Video Downloader': 'Pengunduh Video Gratis',
            'Download': 'Unduh',
            'Paste video link here...': 'Tempel tautan video di sini...',
            'Supported Platforms': 'Platform yang Didukung',
            'Language': 'Bahasa'
        }
    },
    'pt': {
        'name': 'Português',
        'replacements': {
            'Free Video Downloader': 'Baixador de Vídeo Grátis',
            'Download': 'Baixar',
            'Paste video link here...': 'Cole o link do vídeo aqui...',
            'Supported Platforms': 'Plataformas Suportadas',
            'Language': 'Português'
        }
    },
    'th': {
        'name': 'ไทย',
        'replacements': {
            'Free Video Downloader': 'โปรแกรมดาวน์โหลดวิดีโอฟรี',
            'Download': 'ดาวน์โหลด',
            'Paste video link here...': 'วางลิงก์วิดีโอที่นี่...',
            'Supported Platforms': 'แพลตฟอร์มที่รองรับ',
            'Language': 'ไทย'
        }
    },
    'tr': {
        'name': 'Türkçe',
        'replacements': {
            'Free Video Downloader': 'Ücretsiz Video İndirici',
            'Download': 'İndir',
            'Paste video link here...': 'Video bağlantısını buraya yapıştırın...',
            'Supported Platforms': 'Desteklenen Platformlar',
            'Language': 'Türkçe'
        }
    },
    'nl': {
        'name': 'Nederlands',
        'replacements': {
            'Free Video Downloader': 'Gratis video-downloader',
            'Download': 'Downloaden',
            'Paste video link here...': 'Plak hier de videolink...',
            'Supported Platforms': 'Ondersteunde platforms',
            'Language': 'Nederlands'
        }
    },
    'ar': {
        'name': 'العربية',
        'replacements': {
            'Free Video Downloader': 'تحميل الفيديو مجانا',
            'Download': 'تحميل',
            'Paste video link here...': 'الصق رابط الفيديو هنا...',
            'Supported Platforms': 'المنصات المدعومة',
            'Language': 'العربية'
        }
    },
    'de': {
        'name': 'Deutsch',
        'replacements': {
            'Free Video Downloader': 'Kostenloser Video-Downloader',
            'Download': 'Herunterladen',
            'Paste video link here...': 'Video-Link hier einfügen...',
            'Supported Platforms': 'Unterstützte Plattformen',
            'Language': 'Deutsch'
        }
    },
    'it': {
        'name': 'Italiano',
        'replacements': {
            'Free Video Downloader': 'Scaricatore di video gratuito',
            'Download': 'Scarica',
            'Paste video link here...': 'Incolla qui il link del video...',
            'Supported Platforms': 'Piattaforme supportate',
            'Language': 'Italiano'
        }
    },
    'zh': {
        'name': '中文',
        'replacements': {
            'Free Video Downloader': '免费视频下载器',
            'Download': '下载',
            'Paste video link here...': '在此处粘贴视频链接...',
            'Supported Platforms': '支持的平台',
            'Language': '中文'
        }
    },
    # Add minimal support for others to ensure folder creation
    'cs': {'name': 'Čeština', 'replacements': {'Free Video Downloader': 'Stahovač videa zdarma', 'Download': 'Stáhnout', 'Language': 'Čeština'}},
    'pl': {'name': 'Polski', 'replacements': {'Free Video Downloader': 'Darmowy program do pobierania wideo', 'Download': 'Pobierz', 'Language': 'Polski'}},
    'jv': {'name': 'Basa Jawa', 'replacements': {'Free Video Downloader': 'Pengunduh Video Gratis', 'Download': 'Ngundhuh', 'Language': 'Basa Jawa'}},
    'hi': {'name': 'हिन्दी', 'replacements': {'Free Video Downloader': 'मुफ्त वीडियो डाउनलोडर', 'Download': 'डाउनलोड', 'Language': 'हिन्दी'}},
    'hu': {'name': 'Magyar', 'replacements': {'Free Video Downloader': 'Ingyenes videó letöltő', 'Download': 'Letöltés', 'Language': 'Magyar'}},
    'uk': {'name': 'Українська', 'replacements': {'Free Video Downloader': 'Безкоштовний завантажувач відео', 'Download': 'Завантажити', 'Language': 'Українська'}},
    'ro': {'name': 'Română', 'replacements': {'Free Video Downloader': 'Descărcător video gratuit', 'Download': 'Descarcă', 'Language': 'Română'}},
    'ms': {'name': 'Melayu', 'replacements': {'Free Video Downloader': 'Pemuat Turun Video Percuma', 'Download': 'Muat turun', 'Language': 'Melayu'}},
    'el': {'name': 'Ελληνικά', 'replacements': {'Free Video Downloader': 'Δωρεάν πρόγραμμα λήψης βίντεο', 'Download': 'Λήψη', 'Language': 'Ελληνικά'}},
}

TEMPLATE_FILE = "index.html"

def main():
    print("Starting Multi-language Generation...")
    
    # Read Template
    if not os.path.exists(TEMPLATE_FILE):
        print("Error: index.html not found.")
        return
        
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template_content = f.read()

    for lang_code, data in TRANSLATIONS.items():
        print(f"Generating language code: {lang_code}...")
        
        # 1. Create Directory
        if not os.path.exists(lang_code):
            os.makedirs(lang_code)
            
        # 2. Perform Replacements
        new_content = template_content
        
        # Use a default replacement mechanism to avoid errors if some keys are missing in compact dicts
        # Sort replacements by length desc to avoid replacing substrings (e.g. 'Download' vs 'Free Video Download')
        replacements = data.get('replacements', {})
        
        for original, translated in replacements.items():
            new_content = new_content.replace(original, translated)
            
        # 3. Patch Paths with Cache Busting
        new_content = new_content.replace('href="style.css?v=2"', 'href="../style.css?v=2"') # Match if already has v=2 (from index.html updates)
        new_content = new_content.replace('href="style.css"', 'href="../style.css?v=2"') # Match if it doesn't
        new_content = new_content.replace('src="app.js"', 'src="../app.js?v=2"')
        new_content = new_content.replace('href="about.html"', 'href="../about.html"')
        new_content = new_content.replace('href="desktop-app.html"', 'href="../desktop-app.html"')
        new_content = new_content.replace('href="terms.html"', 'href="../terms.html"')
        new_content = new_content.replace('href="privacy.html"', 'href="../privacy.html"')
        new_content = new_content.replace('href="contact.html"', 'href="../contact.html"')
        new_content = new_content.replace('href="index.html"', 'href="../index.html"')
        
        # 4. Write File
        output_path = os.path.join(lang_code, "index.html")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    print("Multi-language pages generated successfully!")

if __name__ == "__main__":
    main()
