// Configuration
const CONFIG = {
    // Production Render backend URL
    // Mặc định dùng link Render của bạn.
    // Nếu muốn test ở máy (localhost) thì đổi thành 'http://localhost:5000'
    API_BASE_URL: 'https://video-downloader-zfoi.onrender.com'
};

// DOM Elements
const videoUrlInput = document.getElementById('videoUrl');
const pasteBtn = document.getElementById('pasteBtn');
const downloadBtn = document.getElementById('downloadBtn');
const loadingState = document.getElementById('loadingState');
const videoInfo = document.getElementById('videoInfo');
const errorMsg = document.getElementById('errorMsg');
const videoThumbnail = document.getElementById('videoThumbnail');
const videoTitle = document.getElementById('videoTitle');
const videoDuration = document.getElementById('videoDuration');
const qualitySelect = document.getElementById('qualitySelect');
const finalDownloadBtn = document.getElementById('final_dl_btn');

let currentVideoData = null;

// Utility Functions
function showElement(element) {
    element.classList.remove('hidden');
}

function hideElement(element) {
    element.classList.add('hidden');
}

function showError(message) {
    errorMsg.textContent = message;
    showElement(errorMsg);
    // Auto hide after 8 seconds
    setTimeout(() => hideElement(errorMsg), 8000);
}

function formatDuration(seconds) {
    if (!seconds) return '';
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = Math.floor(seconds % 60);

    if (hours > 0) {
        return `${hours}:${minutes.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }
    return `${minutes}:${secs.toString().padStart(2, '0')}`;
}

function formatFileSize(bytes) {
    if (!bytes) return '';
    const mb = bytes / (1024 * 1024);
    return `${mb.toFixed(2)} MB`;
}

// Main Functions
async function getVideoInfo(url) {
    try {
        hideElement(videoInfo);
        hideElement(errorMsg);
        showElement(loadingState);

        // Fetch info from backend
        const response = await fetch(`${CONFIG.API_BASE_URL}/api/info?url=${encodeURIComponent(url)}`);

        if (!response.ok) {
            // Try to parse error message from JSON
            const errData = await response.json().catch(() => ({}));
            throw new Error(errData.error || `Server error: ${response.status}`);
        }

        const data = await response.json();

        if (data.error) {
            throw new Error(data.error);
        }

        return data;
    } catch (error) {
        throw new Error(`Connection Error: ${error.message}. Is the backend running?`);
    } finally {
        hideElement(loadingState);
    }
}

function displayVideoInfo(data) {
    currentVideoData = data;

    // Set thumbnail and title
    videoThumbnail.src = data.thumbnail || 'https://via.placeholder.com/320x180?text=No+Thumbnail';
    videoTitle.textContent = data.title || 'Unknown Title';
    videoDuration.textContent = formatDuration(data.duration);

    // Check if uploader info exists
    if (data.uploader) {
        videoTitle.textContent += ` (by ${data.uploader})`;
    }

    // Populate quality options
    qualitySelect.innerHTML = '<option value="">-- Select Quality --</option>';

    if (data.formats && data.formats.length > 0) {
        // Sort: High quality first
        data.formats.sort((a, b) => (b.height || 0) - (a.height || 0));

        const addedIds = new Set();
        let hasOptions = false;

        data.formats.forEach(format => {
            // Prevent duplicates
            if (addedIds.has(format.format_id)) return;
            addedIds.add(format.format_id);

            const option = document.createElement('option');
            option.value = format.format_id;

            // Generate user-friendly label
            let label = format.resolution || `${format.height || '?'}p`;

            if (format.resolution === 'HD No Watermark') label = '🔥 HD No Watermark (Best)';
            else if (format.resolution === 'No Watermark') label = '✅ No Watermark';
            else if (format.resolution === 'Audio Only' || format.ext === 'mp3') label = '🎵 Audio Only (MP3)';
            else if (format.filesize) label += ` - ${formatFileSize(format.filesize)}`;
            else if (format.ext) label += ` (${format.ext})`;

            option.textContent = label;
            qualitySelect.appendChild(option);
            hasOptions = true;
        });

        if (!hasOptions) {
            const option = document.createElement('option');
            option.value = "best";
            option.textContent = "Best Quality (Auto)";
            qualitySelect.appendChild(option);
        }

    } else {
        const option = document.createElement('option');
        option.value = "best";
        option.textContent = "Best Quality (Auto)";
        qualitySelect.appendChild(option);
    }

    showElement(videoInfo);
}

async function downloadVideo() {
    const selectedFormat = qualitySelect.value;

    if (!selectedFormat) {
        showError('👉 Please select a quality first!');
        return;
    }

    if (!currentVideoData) {
        showError('Video infomation missing. Please search again.');
        return;
    }

    try {
        finalDownloadBtn.disabled = true;
        finalDownloadBtn.textContent = 'Processing...';

        const url = videoUrlInput.value.trim();
        const response = await fetch(
            `${CONFIG.API_BASE_URL}/api/download?url=${encodeURIComponent(url)}&format=${selectedFormat}`
        );

        if (!response.ok) {
            const errData = await response.json().catch(() => ({}));
            throw new Error(errData.error || `Server error: ${response.status}`);
        }

        const data = await response.json();

        if (data.error) {
            throw new Error(data.error);
        }

        if (data.direct_url) {
            // Hotlink Protection Bypass for Twitter/X/Others
            // Create a temporary link element to force clean referrer
            const tempLink = document.createElement('a');
            tempLink.href = data.direct_url;
            tempLink.target = '_blank';
            tempLink.rel = 'noreferrer noopener'; // CRITICAL: Hides that the request came from our site

            // For some browsers, dispatching click is safer than window.open
            document.body.appendChild(tempLink);
            tempLink.click();
            document.body.removeChild(tempLink);

        } else {
            throw new Error('Could not retrieve download link.');
        }
    } catch (error) {
        showError(`Download Failed: ${error.message}`);
        console.error(error);
    } finally {
        finalDownloadBtn.disabled = false;
        finalDownloadBtn.textContent = 'Download Video';
    }
}

// Event Listeners
downloadBtn.addEventListener('click', async () => {
    let url = videoUrlInput.value.trim();

    if (!url) {
        showError('Please paste a YouTube or TikTok link!');
        return;
    }

    // AUTO-FIX: Convert YouTube Shorts to Watch URL
    if (url.includes('/shorts/')) {
        url = url.replace('/shorts/', '/watch?v=');
        videoUrlInput.value = url; // Update input visibly for user
        console.log("Auto-converted Shorts link to Watch link");
    }

    if (!url.startsWith('http')) {
        showError('Invalid URL (Must start with http:// or https://)');
        return;
    }

    try {
        const videoData = await getVideoInfo(url);
        displayVideoInfo(videoData);
    } catch (error) {
        showError(error.message);
        console.error(error);
    }
});

finalDownloadBtn.addEventListener('click', downloadVideo);

// Input UX
videoUrlInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        downloadBtn.click();
    }
});
// Paste Button Logic
pasteBtn.addEventListener('click', async () => {
    try {
        const text = await navigator.clipboard.readText();
        if (text) {
            videoUrlInput.value = text;
            videoUrlInput.focus();
            // Trigger input event to clear errors if any
        }
    } catch (err) {
        console.error('Failed to read clipboard:', err);
        showError('Please allow clipboard permission or paste manually (Ctrl+V)');
    }
});

// Language Dropdown Logic (Click to Toggle)
document.addEventListener('DOMContentLoaded', () => {
    const langBtn = document.querySelector('.lang-btn');
    const langContent = document.querySelector('.lang-content');

    if (langBtn && langContent) {
        langBtn.addEventListener('click', (e) => {
            e.stopPropagation(); // Stop click from bubbling to window
            langContent.classList.toggle('show');
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if (!langBtn.contains(e.target) && !langContent.contains(e.target)) {
                langContent.classList.remove('show');
            }
        });
    }
});
