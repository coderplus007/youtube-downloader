# YouTube Downloader

⚠️ **DISCLAIMER: USE AT YOUR OWN RISK**  
This software is provided "AS IS" without warranty of any kind. No support is provided.  
The user assumes all responsibility for the use of this software.

A modern web application for downloading YouTube videos, extracting audio, and downloading transcripts with real-time progress tracking.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.3.3-green.svg)

## 🌟 Features

### Core Functionality
- **Video Download**: Multiple quality options (Best, 1080p, 720p, 480p, 360p)
- **Audio Extraction**: Convert videos to MP3 format (192kbps)
- **Transcript Download**: Download subtitles as clean text files
- **Batch Processing**: Download multiple videos at once
- **Real-time Progress**: Live progress updates via WebSockets

### User Experience
- **Multi-language Support**: 8 languages (EN, DE, FR, ES, IT, UK, RU, EO)
- **Flexible Download Locations**: System or custom download folders
- **Modern UI**: Responsive design with Bootstrap 5
- **File Management**: Automatic cleanup after 24 hours
- **Direct Folder Access**: Open download folder from the app

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- FFmpeg (for audio extraction)
- Modern web browser

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/youtube-downloader.git
cd youtube-downloader
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install FFmpeg:
- **macOS**: `brew install ffmpeg`
- **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

### Running the Application

```bash
python app.py
```

The application will be available at `http://localhost:8080`

## 📖 Usage

### Single Download
1. Navigate to the "Single URL" tab
2. Paste a YouTube URL
3. Select download type (Video/Audio/Transcript)
4. Choose format/quality (for videos) or language (for transcripts)
5. Click "Download" and watch the real-time progress

### Batch Download
1. Switch to the "Batch Download" tab
2. Paste multiple YouTube URLs (one per line)
3. Select download type
4. All videos will be downloaded with the same settings

### Download Settings
- Access the "Settings" tab to configure:
  - Download directory (system or custom)
  - Auto-open downloads folder
  - Language preference

## 🛠️ Technical Details

### Architecture
```
youtube-downloader/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── downloader.py       # YouTube download logic (yt-dlp)
├── forms.py            # Flask-WTF form definitions
├── socket_manager.py   # WebSocket handler
├── translations.py     # Multi-language support
├── templates/          # Jinja2 HTML templates
├── static/             # CSS, JS, images
├── utils/              # Helper utilities
└── tests/              # Unit tests
```

### Technologies
- **Backend**: Flask 2.3.3, Flask-SocketIO
- **Download Engine**: yt-dlp
- **Frontend**: Bootstrap 5, Socket.IO client
- **Forms**: Flask-WTF with CSRF protection
- **Internationalization**: Custom translation system

### API Endpoints
- `POST /process_url` - Process single YouTube URL
- `POST /process_batch` - Process multiple URLs
- `POST /start_download` - Initiate download
- `GET /download_file/<filename>` - Download completed file
- `POST /open_download_folder` - Open download directory
- `GET /api/directories/*` - Directory management APIs

## 🔒 Security Features

- CSRF protection on all forms
- Path traversal prevention
- Secure filename handling
- Input validation and sanitization
- Local-only file system access

## 🌍 Internationalization

Supported languages:
- 🇬🇧 English
- 🇩🇪 Deutsch (German)
- 🇫🇷 Français (French)
- 🇪🇸 Español (Spanish)
- 🇮🇹 Italiano (Italian)
- 🇺🇦 Українська (Ukrainian)
- 🇷🇺 Русский (Russian)
- 🌐 Esperanto

## 🐛 Known Issues

- Downloads may fail for age-restricted or private videos
- Some regional restrictions may apply
- Large playlists (>50 videos) may timeout

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Copyright (c) 2025 Olga Meier GmbH, Switzerland**  
**Developer: Beat Meier**

**Place of jurisdiction is Zug, Switzerland. Swiss law applies.**

### Disclaimer

**USE AT YOUR OWN RISK**

THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

**NO SUPPORT IS PROVIDED.** The user assumes all responsibility for the use of this software.

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the download functionality
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Socket.IO](https://socket.io/) for real-time communication
- [Bootstrap](https://getbootstrap.com/) for the UI components

## 📞 Support

For support, please open an issue on GitHub or contact the developer.

---

Made with ❤️ in Switzerland 🇨🇭