"""Core downloading functionality using yt-dlp."""

import os
import json
import re
import uuid
from typing import Dict, List, Optional, Tuple, Any, Callable
from pathlib import Path
from datetime import datetime
import yt_dlp
from config import Config


class ProgressHook:
    """Hook for tracking download progress and emitting events via SocketIO."""
    
    def __init__(self, socketio=None, room=None):
        """Initialize with optional SocketIO instance and room for emitting events."""
        self.socketio = socketio
        self.room = room
        self.last_percent = 0
        self.last_emit_time = datetime.now()
    
    def __call__(self, data: Dict[str, Any]) -> None:
        """Progress hook callback function that will be called by yt-dlp."""
        if data['status'] == 'downloading':
            # Avoid flooding the client with too many updates
            now = datetime.now()
            time_diff = (now - self.last_emit_time).total_seconds()
            
            # Only emit every 0.5 seconds or if progress has changed significantly
            percent = float(data['_percent_str'].replace('%', '').strip())
            if self.socketio and (time_diff >= 0.5 or abs(percent - self.last_percent) >= 5):
                self.socketio.emit('download_progress', {
                    'percent': percent,
                    'speed': data.get('_speed_str', 'N/A'),
                    'eta': data.get('_eta_str', 'N/A'),
                    'filename': data.get('filename', 'Unknown'),
                    'downloaded_bytes': data.get('downloaded_bytes', 0),
                    'total_bytes': data.get('total_bytes', 0)
                }, room=self.room)
                
                self.last_percent = percent
                self.last_emit_time = now
                
        elif data['status'] == 'finished':
            if self.socketio:
                self.socketio.emit('download_progress', {
                    'percent': 100,
                    'status': 'finished',
                    'filename': data.get('filename', 'Unknown')
                }, room=self.room)
        
        elif data['status'] == 'error':
            if self.socketio:
                self.socketio.emit('download_error', {
                    'error': str(data.get('error', 'Unknown error')),
                    'filename': data.get('filename', 'Unknown')
                }, room=self.room)


class YouTubeDownloader:
    """Class for handling YouTube video downloads using yt-dlp."""
    
    def __init__(self, socketio=None):
        """Initialize the downloader with optional SocketIO instance."""
        self.socketio = socketio
        # Don't cache the download folder - always get it from Config
        # self.download_folder = Config.DOWNLOAD_FOLDER
    
    @property
    def download_folder(self):
        """Always get the current download folder from Config."""
        return Config.DOWNLOAD_FOLDER
    
    def get_video_info(self, url: str) -> Dict[str, Any]:
        """Fetch video metadata without downloading."""
        ydl_opts = {
            'skip_download': True,
            'quiet': True,
            'no_warnings': True,
            'no_color': True,
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            # Additional options to bypass restrictions
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'geo_bypass': True,
            'geo_bypass_country': 'US',
            'extractor_retries': 3,
            # Add user-agent to mimic a browser
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            },
            # Prevent .part files
            'nopart': True,
            'continuedl': False,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return info
        except yt_dlp.utils.DownloadError as e:
            raise ValueError(f"Error fetching video info: {str(e)}")
    
    def get_available_formats(self, url: str) -> List[Dict[str, Any]]:
        """Get available video formats/resolutions for a given URL."""
        print(f"Getting available formats for URL: {url}")
        info = self.get_video_info(url)
        
        # Filter and organize formats
        formats = []
        seen_resolutions = set()
        
        # Always add a "best" format option
        formats.append({
            'format_id': 'best',
            'resolution': 'Best Quality',
            'ext': 'mp4',
            'filesize': None,
            'format_note': 'Automatic best quality'
        })
        
        for f in info.get('formats', []):
            # Skip audio-only formats for video downloads
            if f.get('vcodec', '') == 'none':
                continue
                
            # Skip formats without resolution info
            height = f.get('height')
            if not height:
                continue
                
            # Create a resolution label
            resolution = f"{height}p"
            if resolution in seen_resolutions:
                continue
                
            # Add to our format list
            formats.append({
                'format_id': f['format_id'],
                'resolution': resolution,
                'ext': f.get('ext', 'mp4'),
                'filesize': f.get('filesize'),
                'format_note': f.get('format_note', '')
            })
            seen_resolutions.add(resolution)
        
        # Add a few common format options if not already present
        common_resolutions = ['720p', '480p', '360p']
        for res in common_resolutions:
            if res not in seen_resolutions and formats:
                # Use the best format ID with a format selector
                formats.append({
                    'format_id': f'best[height<={res[:-1]}]',
                    'resolution': res,
                    'ext': 'mp4',
                    'filesize': None,
                    'format_note': f'Best {res} quality'
                })
        
        # Sort by resolution (highest first)
        # Put "Best Quality" at the top
        formats.sort(key=lambda x: 9999 if x['resolution'] == 'Best Quality' else 
                                   int(x['resolution'].replace('p', '')) if x['resolution'].endswith('p') else 0, 
                     reverse=True)
        
        print(f"Found {len(formats)} formats")
        return formats
    
    def get_available_subtitles(self, url: str) -> Dict[str, Any]:
        """Get available subtitle languages for a given URL."""
        ydl_opts = {
            'skip_download': True,
            'quiet': True,
            'no_warnings': True,
            'no_color': True,
            'writesubtitles': True,
            'listsubtitles': True,
            # Additional options to bypass restrictions
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'geo_bypass': True,
            'geo_bypass_country': 'US',
            'extractor_retries': 3,
            # Add user-agent to mimic a browser
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            },
            # Prevent .part files
            'nopart': True,
            'continuedl': False,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # Get both manual and auto-generated subtitles
                subtitles = info.get('subtitles', {})
                auto_subtitles = info.get('automatic_captions', {})
                
                # Combine and format results
                result = {}
                
                # Process manual subtitles
                for lang_code, subs in subtitles.items():
                    if subs:  # Make sure it's not empty
                        lang_name = subs[0].get('name', lang_code)
                        result[lang_code] = {
                            'name': lang_name,
                            'type': 'manual'
                        }
                
                # Process auto-generated subtitles
                for lang_code, subs in auto_subtitles.items():
                    if subs and lang_code not in result:  # Only add if not already added
                        lang_name = subs[0].get('name', lang_code)
                        result[lang_code] = {
                            'name': lang_name,
                            'type': 'auto-generated'
                        }
                
                return result
        except yt_dlp.utils.DownloadError as e:
            raise ValueError(f"Error fetching subtitles info: {str(e)}")
    
    def download_video(self, url: str, format_id: str = None, room: str = None) -> str:
        """Download a video in the specified format."""
        import logging
        logging.basicConfig(level=logging.INFO)
        
        print(f"Starting download for URL: {url} with format: {format_id}")
        print(f"[DEBUG] Download folder is: {self.download_folder}")
        print(f"[DEBUG] Config.DOWNLOAD_FOLDER is: {Config.DOWNLOAD_FOLDER}")
        
        # Generate a unique filename
        unique_id = str(uuid.uuid4())
        output_template = os.path.join(self.download_folder, f"{unique_id}-%(title)s.%(ext)s")
        print(f"[DEBUG] Output template: {output_template}")
        
        # Ensure download folder exists
        os.makedirs(self.download_folder, exist_ok=True)
        
        # Set up options for video download
        ydl_opts = {
            'format': format_id or 'best[ext=mp4]/best',  # Simpler format selector
            'outtmpl': output_template,
            'quiet': True,  # Reduce verbosity
            'no_warnings': False,  # Show warnings
            'no_color': True,
            'progress_hooks': [ProgressHook(self.socketio, room)],
            # Prevent creating duplicate downloads
            'continuedl': False,  # Don't continue partial downloads
            'nopart': True,  # Don't use .part files
            # Additional options to bypass restrictions
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'geo_bypass': True,
            'geo_bypass_country': 'US',
            'extractor_retries': 3,  # Reasonable retries
            # Add user-agent to mimic a browser
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            },
            # Set a timeout for connections
            'socket_timeout': 30,
            # Ensure proper file handling
            'keepvideo': False,
            'overwrites': True,  # Overwrite existing files
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                
                # Find the downloaded file
                if info and 'requested_downloads' in info:
                    filepath = info['requested_downloads'][0].get('filepath')
                    print(f"[DEBUG] Downloaded file path: {filepath}")
                    print(f"[DEBUG] File exists: {os.path.exists(filepath)}")
                    return os.path.basename(filepath)
                else:
                    # Fallback to searching the directory
                    print(f"[DEBUG] Searching in directory: {self.download_folder}")
                    files = list(Path(self.download_folder).glob(f"{unique_id}*"))
                    print(f"[DEBUG] Found files: {files}")
                    if files:
                        return os.path.basename(files[0])
                    
                    raise ValueError("Could not determine downloaded file")
        except yt_dlp.utils.DownloadError as e:
            raise ValueError(f"Download error: {str(e)}")
    
    def download_audio(self, url: str, room: str = None) -> str:
        """Extract audio from video as MP3."""
        print(f"[DEBUG] Audio download - folder: {self.download_folder}")
        # Ensure download folder exists
        os.makedirs(self.download_folder, exist_ok=True)
        
        # Generate a unique filename
        unique_id = str(uuid.uuid4())
        output_template = os.path.join(self.download_folder, f"{unique_id}-%(title)s.%(ext)s")
        
        # Set up options for audio extraction
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_template,
            'quiet': True,
            'no_warnings': True,
            'no_color': True,
            'progress_hooks': [ProgressHook(self.socketio, room)],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            # Additional options to bypass restrictions
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'geo_bypass': True,
            'geo_bypass_country': 'US',
            'extractor_retries': 3,
            # Add user-agent to mimic a browser
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            }
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                
                # Find the downloaded file
                if info and 'requested_downloads' in info:
                    filename = info['requested_downloads'][0].get('filepath')
                    # yt-dlp changes the extension after extraction
                    filename = filename.replace('.webm', '.mp3').replace('.m4a', '.mp3')
                    return os.path.basename(filename)
                else:
                    # Fallback to searching the directory
                    files = list(Path(self.download_folder).glob(f"{unique_id}*.mp3"))
                    if files:
                        return os.path.basename(files[0])
                    
                    raise ValueError("Could not determine downloaded file")
        except yt_dlp.utils.DownloadError as e:
            raise ValueError(f"Download error: {str(e)}")
    
    def clean_subtitle_text(self, subtitle_file: Path) -> str:
        """Clean subtitle file and extract only the text content."""
        try:
            with open(subtitle_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove VTT header
            content = re.sub(r'^WEBVTT.*?\n\n', '', content, flags=re.MULTILINE | re.DOTALL)
            
            # Remove SRT subtitle numbers
            content = re.sub(r'^\d+\n', '', content, flags=re.MULTILINE)
            
            # Remove timestamps (VTT format: 00:00:00.000 --> 00:00:00.000)
            content = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}.*?\n', '', content)
            
            # Remove timestamps (SRT format: 00:00:00,000 --> 00:00:00,000)
            content = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}.*?\n', '', content)
            
            # Remove HTML tags
            content = re.sub(r'<[^>]+>', '', content)
            
            # Remove speaker tags like <v Name>
            content = re.sub(r'<v\s+[^>]+>', '', content)
            
            # Remove position tags
            content = re.sub(r'\{[^}]+\}', '', content)
            
            # Remove multiple empty lines
            content = re.sub(r'\n\s*\n', '\n\n', content)
            
            # Remove leading/trailing whitespace from each line
            lines = [line.strip() for line in content.split('\n') if line.strip()]
            
            # Join lines that are part of the same sentence
            cleaned_text = []
            current_sentence = []
            
            for line in lines:
                # Skip lines that are just numbers or contain timestamps
                if re.match(r'^\d+$', line) or '-->' in line:
                    continue
                    
                current_sentence.append(line)
                
                # If line ends with punctuation, it's likely end of sentence
                if line and line[-1] in '.!?;':
                    cleaned_text.append(' '.join(current_sentence))
                    current_sentence = []
            
            # Add any remaining sentence
            if current_sentence:
                cleaned_text.append(' '.join(current_sentence))
            
            # Join all sentences with proper spacing
            final_text = '\n\n'.join(cleaned_text)
            
            # Clean up any remaining artifacts
            final_text = re.sub(r'\s+', ' ', final_text)  # Multiple spaces to single space
            final_text = re.sub(r'\n\s*\n', '\n\n', final_text)  # Clean up empty lines
            
            return final_text.strip()
            
        except Exception as e:
            raise ValueError(f"Error cleaning subtitle text: {str(e)}")
    
    def download_subtitles(self, url: str, lang_code: str, room: str = None) -> str:
        """Download subtitles/transcript for a video."""
        # Generate a unique filename
        unique_id = str(uuid.uuid4())
        output_template = os.path.join(self.download_folder, f"{unique_id}-%(title)s")
        
        # Determine if we need auto-generated subtitles
        auto_subs = False
        subtitles_info = self.get_available_subtitles(url)
        
        if lang_code in subtitles_info:
            auto_subs = subtitles_info[lang_code]['type'] == 'auto-generated'
        
        # Set up options for subtitle download
        ydl_opts = {
            'skip_download': True,
            'outtmpl': output_template,
            'quiet': True,
            'no_warnings': True,
            'no_color': True,
            'progress_hooks': [ProgressHook(self.socketio, room)],
            'writesubtitles': True,
            'subtitleslangs': [lang_code],
            # Additional options to bypass restrictions
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'geo_bypass': True,
            'geo_bypass_country': 'US',
            'extractor_retries': 3,
            # Add user-agent to mimic a browser
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            }
        }
        
        if auto_subs:
            ydl_opts['writeautomaticsub'] = True
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                
                # Search for the subtitle file
                subs_ext = '.vtt'
                pattern = f"{unique_id}*{lang_code}*{subs_ext}"
                files = list(Path(self.download_folder).glob(pattern))
                
                if not files:
                    # Try alternative patterns
                    pattern = f"{unique_id}*.{lang_code}.*"
                    files = list(Path(self.download_folder).glob(pattern))
                
                if files:
                    subtitle_file = files[0]
                    
                    # Clean the subtitle content
                    cleaned_text = self.clean_subtitle_text(subtitle_file)
                    
                    # Save as .txt file with clean filename
                    video_title = subtitle_file.stem.replace(f"{unique_id}-", "")
                    txt_filename = f"{video_title}_transcript_{lang_code}.txt"
                    txt_path = subtitle_file.parent / txt_filename
                    
                    with open(txt_path, 'w', encoding='utf-8') as f:
                        # Add header to the file
                        f.write(f"YouTube Video Transcript\n")
                        f.write(f"Language: {subtitles_info[lang_code]['name']}\n")
                        f.write(f"Type: {subtitles_info[lang_code]['type']}\n")
                        f.write(f"{'=' * 50}\n\n")
                        f.write(cleaned_text)
                    
                    # Delete the original subtitle file
                    subtitle_file.unlink()
                    
                    # Emit completion
                    if self.socketio:
                        self.socketio.emit('download_progress', {
                            'percent': 100,
                            'status': 'finished',
                            'filename': txt_filename
                        }, room=room)
                    
                    return txt_filename
                else:
                    raise ValueError(f"Could not find subtitle file for language {lang_code}")
        except yt_dlp.utils.DownloadError as e:
            raise ValueError(f"Download error: {str(e)}")
    
    def process_batch(self, urls: List[str], download_type: str, format_id: str = None, 
                    lang_code: str = None, room: str = None) -> List[Dict[str, Any]]:
        """Process a batch of URLs for download."""
        results = []
        
        for i, url in enumerate(urls):
            try:
                # Emit batch progress update
                if self.socketio:
                    self.socketio.emit('batch_progress', {
                        'current': i + 1,
                        'total': len(urls),
                        'url': url,
                        'status': 'processing'
                    }, room=room)
                
                # Process based on download type
                if download_type == 'video':
                    filename = self.download_video(url, format_id, room)
                    results.append({
                        'url': url,
                        'filename': filename,
                        'type': 'video',
                        'status': 'success'
                    })
                    
                elif download_type == 'audio':
                    filename = self.download_audio(url, room)
                    results.append({
                        'url': url,
                        'filename': filename,
                        'type': 'audio',
                        'status': 'success'
                    })
                    
                elif download_type == 'transcript':
                    filename = self.download_subtitles(url, lang_code, room)
                    results.append({
                        'url': url,
                        'filename': filename,
                        'type': 'transcript',
                        'status': 'success'
                    })
                
                # Emit success for this item
                if self.socketio:
                    self.socketio.emit('batch_progress', {
                        'current': i + 1,
                        'total': len(urls),
                        'url': url,
                        'status': 'success',
                        'filename': filename
                    }, room=room)
                    
            except Exception as e:
                # Handle errors
                results.append({
                    'url': url,
                    'error': str(e),
                    'status': 'error'
                })
                
                # Emit error for this item
                if self.socketio:
                    self.socketio.emit('batch_progress', {
                        'current': i + 1,
                        'total': len(urls),
                        'url': url,
                        'status': 'error',
                        'error': str(e)
                    }, room=room)
        
        return results
    
    def cleanup_old_files(self, hours: int = None) -> int:
        """Delete files older than specified hours."""
        if hours is None:
            hours = Config.FILE_RETENTION_HOURS
            
        retention_seconds = hours * 3600
        now = datetime.now().timestamp()
        count = 0
        
        try:
            for item in Path(self.download_folder).glob('*'):
                if item.is_file():
                    file_age = now - item.stat().st_mtime
                    if file_age > retention_seconds:
                        item.unlink()
                        count += 1
        except Exception as e:
            print(f"Error during cleanup: {str(e)}")
            
        return count