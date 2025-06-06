# Changelog

All notable changes to YouTube Downloader will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of YouTube Downloader
- Video download functionality with format selection
- Audio extraction to MP3 (192kbps)
- Transcript/subtitle download as clean text files
- Batch download support for multiple URLs
- Real-time progress tracking with WebSocket
- Multi-language support (8 languages)
- Flexible download directory selection
- Auto-cleanup of old files (24-hour retention)
- Direct folder opening from application
- Responsive web interface

### Security
- CSRF protection on all forms
- Secure filename handling
- Path traversal prevention
- Input validation and sanitization

## [1.0.0] - 2025-01-13

### Initial Features
- **Core Downloads**
  - Video download (MP4, multiple qualities)
  - Audio extraction (MP3)
  - Transcript download (TXT)
  
- **User Interface**
  - Modern Bootstrap 5 design
  - Real-time progress updates
  - Format selection interface
  - Language selection for transcripts
  - Batch URL input
  
- **Internationalization**
  - English
  - German (Deutsch)
  - French (Français)
  - Spanish (Español)
  - Italian (Italiano)
  - Ukrainian (Українська)
  - Russian (Русский)
  - Esperanto
  
- **File Management**
  - System Downloads folder support
  - Custom directory selection
  - Open download folder button
  - Show file in folder feature
  - Automatic cleanup after 24 hours
  
- **Technical Stack**
  - Flask 2.3.3 web framework
  - yt-dlp for YouTube integration
  - Socket.IO for real-time updates
  - Bootstrap 5 for UI
  - Flask-WTF for forms
  - Flask-Babel for translations

### Known Issues
- Rate limiting not yet implemented
- No user authentication (designed for single user)
- Production deployment guides need expansion

---

## Version History

### Version Numbering
- MAJOR version: Incompatible API changes
- MINOR version: Backwards-compatible functionality
- PATCH version: Backwards-compatible bug fixes

### Support Policy
- Latest version: Full support
- Previous minor version: Security updates only
- Older versions: No support

---

**Copyright (c) 2025 Olga Meier GmbH, Switzerland**  
**Developer: Beat Meier**
