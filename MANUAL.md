# YouTube Downloader User Manual

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation](#installation)
   - [Windows Installation](#windows-installation)
   - [macOS Installation](#macos-installation)
3. [Starting the Application](#starting-the-application)
4. [Using the YouTube Downloader](#using-the-youtube-downloader)
5. [Troubleshooting](#troubleshooting)
6. [Security Notes](#security-notes)

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10/11 or macOS 10.14+
- **Python**: Version 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 500MB for application + space for downloads
- **Internet**: Stable broadband connection
- **Browser**: Modern web browser (Chrome, Firefox, Safari, Edge)

### Required Software
- Python 3.8+
- FFmpeg (for audio extraction and format conversion)
- Git (optional, for cloning repository)

## Installation

### Windows Installation

#### Step 1: Install Python
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation
4. Click "Install Now"
5. Verify installation:
   ```cmd
   python --version
   ```

#### Step 2: Install FFmpeg
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
   - Choose "Windows builds by BtbN"
   - Download the "ffmpeg-master-latest-win64-gpl.zip"
2. Extract the ZIP file to `C:\ffmpeg`
3. Add FFmpeg to PATH:
   - Right-click "This PC" → Properties
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables", find "Path" and click "Edit"
   - Click "New" and add `C:\ffmpeg\bin`
   - Click "OK" on all windows
4. Verify installation:
   ```cmd
   ffmpeg -version
   ```

#### Step 3: Download and Setup Application
1. Download the YouTube Downloader:
   ```cmd
   cd C:\
   git clone [repository-url] youtube-downloader
   ```
   Or download and extract the ZIP file

2. Navigate to the project directory:
   ```cmd
   cd C:\youtube-downloader
   ```

3. Create virtual environment:
   ```cmd
   python -m venv venv
   ```

4. Activate virtual environment:
   ```cmd
   venv\Scripts\activate
   ```

5. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```

### macOS Installation

#### Step 1: Install Homebrew (if not installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Step 2: Install Python
```bash
brew install python@3.11
```

Verify installation:
```bash
python3 --version
```

#### Step 3: Install FFmpeg
```bash
brew install ffmpeg
```

Verify installation:
```bash
ffmpeg -version
```

#### Step 4: Download and Setup Application
1. Clone or download the application:
   ```bash
   cd ~/Documents
   git clone [repository-url] youtube-downloader
   ```

2. Navigate to the project directory:
   ```bash
   cd youtube-downloader
   ```

3. Create virtual environment:
   ```bash
   python3 -m venv venv
   ```

4. Activate virtual environment:
   ```bash
   source venv/bin/activate
   ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Starting the Application

### Windows
1. Open Command Prompt
2. Navigate to the project directory:
   ```cmd
   cd C:\youtube-downloader
   ```
3. Activate virtual environment:
   ```cmd
   venv\Scripts\activate
   ```
4. Start the application:
   ```cmd
   python app.py
   ```
5. Open your browser and go to: `http://localhost:5000`

### macOS
1. Open Terminal
2. Navigate to the project directory:
   ```bash
   cd ~/Documents/youtube-downloader
   ```
3. Activate virtual environment:
   ```bash
   source venv/bin/activate
   ```
4. Start the application:
   ```bash
   python app.py
   ```
5. Open your browser and go to: `http://localhost:5000`

### Using the Start Script (macOS/Linux)
```bash
chmod +x start_server.sh
./start_server.sh
```

## Using the YouTube Downloader

### Step 1: Access the Application
1. Ensure the application is running
2. Open your web browser
3. Navigate to `http://localhost:5000`
4. Select your preferred language from the navigation bar

### Step 2: Download Content

#### Single Video Download
1. Copy the YouTube video URL
2. Paste it into the "YouTube URL" field
3. Select content type:
   - **Video**: Downloads video with audio
   - **Audio**: Extracts audio only (MP3)
   - **Transcript**: Downloads subtitles/captions
4. Click "Get Formats"
5. Select desired quality/format from the dropdown
6. For transcripts, select language if multiple available
7. Click "Download"
8. Monitor progress on the download page
9. Click the download link when complete

#### Batch Download (Multiple Videos)
1. Click "Switch to batch mode"
2. Enter multiple YouTube URLs (one per line)
3. Select content type for all videos
4. Click "Process Batch"
5. Monitor individual progress for each video
6. Download files as they complete

### Download Options

#### Video Formats
- **Best Quality**: Highest available resolution
- **1080p**: Full HD (if available)
- **720p**: HD
- **480p**: Standard Definition
- **360p**: Mobile quality

#### Audio Formats
- **MP3**: Most compatible format
- **Best Audio**: Highest quality available
- **128k**: Standard quality
- **192k**: High quality
- **320k**: Maximum quality

#### Transcript Options
- Auto-generated subtitles
- Manual subtitles (if available)
- Multiple language options
- SRT format output

### Advanced Features

#### Custom Download Location
Edit `config.py` to change the download directory:
```python
DOWNLOAD_DIR = '/path/to/your/downloads'
```

#### Concurrent Downloads
The application supports multiple simultaneous downloads. Progress for each is tracked independently.

## Troubleshooting

### Common Issues

#### "FFmpeg not found" Error
- **Windows**: Ensure FFmpeg is in PATH (restart after adding)
- **macOS**: Run `brew reinstall ffmpeg`

#### "Connection refused" on localhost:5000
- Ensure the application is running
- Check if port 5000 is blocked by firewall
- Try `http://127.0.0.1:5000` instead

#### Downloads Fail Immediately
- Check internet connection
- Verify the YouTube URL is valid
- Ensure the video is not private or age-restricted
- Update yt-dlp: `pip install --upgrade yt-dlp`

#### No Audio in Downloaded Video
- Ensure FFmpeg is properly installed
- Try selecting a different format
- Some formats may not include audio

### Debug Mode
Enable debug mode for detailed error messages:
1. Edit `config.py`
2. Set `DEBUG = True`
3. Restart the application

### Logs
Check application logs in the console where you started the server.

## Security Notes

### Important Warnings
1. **Legal Responsibility**: Users are responsible for complying with copyright laws
2. **Private Use Only**: Downloaded content should be for personal use
3. **No Warranty**: The application is provided as-is without warranty
4. **Network Security**: Only run on trusted networks
5. **Updates**: Keep yt-dlp and dependencies updated

### Best Practices
- Don't expose the application to the internet
- Use only for content you have permission to download
- Regularly update all dependencies
- Monitor disk space for downloads
- Clean up old downloads periodically

### Firewall Configuration
If you need to access from another device on your network:
1. Configure Flask to listen on all interfaces:
   ```python
   app.run(host='0.0.0.0', port=5000)
   ```
2. Allow port 5000 in your firewall
3. Access via your computer's IP address

## Support

For issues or questions:
1. Check the [CHANGELOG.md](CHANGELOG.md) for recent updates
2. Review [README.md](README.md) for additional information
3. Ensure all dependencies are up to date
4. Check console output for error messages

## License

This software is provided under the license terms specified in the [LICENSE](LICENSE) file. Users must comply with all applicable laws and YouTube's Terms of Service.