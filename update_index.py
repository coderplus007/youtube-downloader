"""
Script to update index.html with translations
"""
import re

# Read the current index.html
with open('/Volumes/NAS/Praxis_OM/SynologyDrive/04_IT_Infrastruktur/98_SW_Entwicklungen/01_Projekte/01_Automation/02_Youtube_downloader/templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define translation replacements
replacements = [
    # Title
    (r'{% block title %}YouTube Downloader - Download Videos, Audio & Transcripts{% endblock %}',
     r'{% block title %}{{ _("app_name") }} - {{ _("about_desc") }}{% endblock %}'),
    
    # Hero section
    (r'<h1 class="display-4 fw-bold">\s*<i class="fab fa-youtube text-danger"></i> YouTube Downloader\s*</h1>',
     r'<h1 class="display-4 fw-bold">\n                <i class="fab fa-youtube text-danger"></i> {{ _("app_name") }}\n            </h1>'),
    
    (r'<p class="lead text-muted">Download videos, extract audio, and save transcripts from YouTube with ease</p>',
     r'<p class="lead text-muted">{{ _("about_desc") }}</p>'),
    
    # Tab labels
    (r'<i class="fas fa-download me-2"></i>Single URL',
     r'<i class="fas fa-download me-2"></i>{{ _("single_url") }}'),
    
    (r'<i class="fas fa-list me-2"></i>Batch Download',
     r'<i class="fas fa-list me-2"></i>{{ _("batch_download") }}'),
    
    (r'<i class="fas fa-cog me-2"></i>Settings',
     r'<i class="fas fa-cog me-2"></i>{{ _("settings") }}'),
    
    # Form labels
    (r'<i class="fab fa-youtube text-danger me-2"></i>YouTube URL',
     r'<i class="fab fa-youtube text-danger me-2"></i>{{ _("youtube_url") }}'),
    
    (r'placeholder="https://www\.youtube\.com/watch\?v=\.\.\."',
     r'placeholder="{{ _("youtube_url_placeholder") }}"'),
    
    (r'<i class="fas fa-info-circle me-1"></i>Enter a valid YouTube video or playlist URL',
     r'<i class="fas fa-info-circle me-1"></i>{{ _("enter_valid_url") }}'),
    
    (r'<i class="fas fa-file-download me-2"></i>Download Type',
     r'<i class="fas fa-file-download me-2"></i>{{ _("download_type") }}'),
    
    (r'<strong>Video</strong>',
     r'<strong>{{ _("video") }}</strong>'),
    
    (r'<strong>Audio</strong>',
     r'<strong>{{ _("audio") }}</strong>'),
    
    (r'<strong>Transcript</strong>',
     r'<strong>{{ _("transcript") }}</strong>'),
    
    (r'<small class="d-block text-muted">Clean text file</small>',
     r'<small class="d-block text-muted">{{ _("clean_text") }}</small>'),
    
    (r'<i class="fas fa-arrow-right me-2"></i>Continue',
     r'<i class="fas fa-arrow-right me-2"></i>{{ _("continue") }}'),
    
    # Batch form
    (r'<i class="fas fa-list text-primary me-2"></i>YouTube URLs \(one per line\)',
     r'<i class="fas fa-list text-primary me-2"></i>{{ _("youtube_urls_multiline") }}'),
    
    (r'<i class="fas fa-info-circle me-1"></i>Enter multiple YouTube URLs, one per line',
     r'<i class="fas fa-info-circle me-1"></i>{{ _("enter_multiple_urls") }}'),
    
    # Settings tab
    (r'<i class="fas fa-folder me-2"></i>Download Directory Settings',
     r'<i class="fas fa-folder me-2"></i>{{ _("download_directory_settings") }}'),
    
    (r'<i class="fas fa-external-link-alt me-2"></i>Open Current Folder',
     r'<i class="fas fa-external-link-alt me-2"></i>{{ _("open_current_folder") }}'),
    
    (r'<strong>Use System Downloads Folder</strong>',
     r'<strong>{{ _("use_system_downloads") }}</strong>'),
    
    (r'<strong>Use Custom Directory</strong>',
     r'<strong>{{ _("use_custom_directory") }}</strong>'),
    
    (r'<i class="fas fa-folder-open me-2"></i>Browse',
     r'<i class="fas fa-folder-open me-2"></i>{{ _("browse") }}'),
    
    (r'<i class="fas fa-save me-2"></i>Save Settings',
     r'<i class="fas fa-save me-2"></i>{{ _("save_settings") }}'),
    
    (r'<i class="fas fa-check-circle me-1"></i>Settings saved!',
     r'<i class="fas fa-check-circle me-1"></i>{{ _("settings_saved") }}'),
    
    # How it works section
    (r'<h3 class="text-center mb-4">How It Works</h3>',
     r'<h3 class="text-center mb-4">{{ _("how_it_works") }}</h3>'),
    
    (r'<h5>1\. Paste URL</h5>',
     r'<h5>1. {{ _("paste_url") }}</h5>'),
    
    (r'<p>Enter a YouTube video or playlist URL</p>',
     r'<p>{{ _("paste_url_desc") }}</p>'),
    
    (r'<h5>2\. Choose Options</h5>',
     r'<h5>2. {{ _("choose_options") }}</h5>'),
    
    (r'<p>Select format, quality, and language</p>',
     r'<p>{{ _("choose_options_desc") }}</p>'),
    
    (r'<h5>3\. Download</h5>',
     r'<h5>3. {{ _("download") }}</h5>'),
    
    (r'<p>Get your content with progress tracking</p>',
     r'<p>{{ _("download_desc") }}</p>'),
    
    # What you can download section
    (r'<h3 class="text-center mb-4">What You Can Download</h3>',
     r'<h3 class="text-center mb-4">{{ _("what_you_can_download") }}</h3>'),
    
    (r'<h5 class="card-title">Videos</h5>',
     r'<h5 class="card-title">{{ _("videos") }}</h5>'),
    
    (r'<p class="card-text">Download in various resolutions from 360p to 4K</p>',
     r'<p class="card-text">{{ _("videos_desc") }}</p>'),
    
    (r'<h5 class="card-title">Audio</h5>',
     r'<h5 class="card-title">{{ _("audio") }}</h5>'),
    
    (r'<p class="card-text">Extract audio as high-quality MP3 files \(192kbps\)</p>',
     r'<p class="card-text">{{ _("audio_desc") }}</p>'),
    
    (r'<h5 class="card-title">Transcripts</h5>',
     r'<h5 class="card-title">{{ _("transcripts") }}</h5>'),
    
    (r'<p class="card-text">Clean text files without timestamps or formatting</p>',
     r'<p class="card-text">{{ _("transcripts_desc") }}</p>'),
    
    # Additional settings text
    (r'<label class="form-label">Quick Access:</label>',
     r'<label class="form-label">{{ _("quick_access") }}</label>'),
    
    (r'<i class="fas fa-cog me-2"></i>Download Preferences',
     r'<i class="fas fa-cog me-2"></i>{{ _("download_preferences") }}'),
    
    (r'<strong>Automatically open download folder after completion</strong>',
     r'<strong>{{ _("auto_open_downloads") }}</strong>'),
    
    (r'<small class="text-muted">When enabled, the download folder will open in your file explorer after downloads complete</small>',
     r'<small class="text-muted">{{ _("auto_open_description") }}</small>'),
    
    (r'<i class="fas fa-info-circle me-2"></i>About Directory Selection',
     r'<i class="fas fa-info-circle me-2"></i>{{ _("about_directory_selection") }}'),
    
    (r'You can choose where to save your downloaded files\. By default, files are saved to your system\'s Downloads folder\.\s*You can also select a custom directory, such as an external drive or a specific project folder\.',
     r'{{ _("directory_info") }}'),
    
    (r'<strong>Tip:</strong>',
     r'<strong>{{ _("tip") }}:</strong>'),
    
    (r'After downloading, the folder will automatically open in your file explorer \(Finder on Mac, Explorer on Windows\)\.\s*You can also click "Show in folder" next to any downloaded file to reveal it in the file browser\.',
     r'{{ _("directory_tip") }}'),
]

# Apply all replacements
for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content, flags=re.MULTILINE | re.DOTALL)

# Save the updated file
with open('/Volumes/NAS/Praxis_OM/SynologyDrive/04_IT_Infrastruktur/98_SW_Entwicklungen/01_Projekte/01_Automation/02_Youtube_downloader/templates/index_updated.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html has been updated with translations!")
