"""
YouTube Downloader Flask Application

A web application for downloading YouTube videos, extracting audio,
and downloading transcripts with real-time progress updates.

Copyright (c) 2025 Olga Meier GmbH, Switzerland
Licensed under MIT License

DISCLAIMER: USE AT YOUR OWN RISK
This software is provided "AS IS" without warranty of any kind.
No support is provided. The user assumes all responsibility
for the use of this software.

Place of jurisdiction is Zug, Switzerland. Swiss law applies.
"""

import os
import uuid
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, session, jsonify
from werkzeug.utils import secure_filename
from forms import YouTubeURLForm, BatchURLForm, FormatSelectionForm
from downloader import YouTubeDownloader
from socket_manager import SocketManager
from config import config as app_config, Config
from utils.file_utils import get_default_download_directory
from translations import get_translation, get_all_translations
import logging
import platform
import subprocess
import sys


# Initialize Flask application
app = Flask(__name__)
app.config.from_object(app_config['development'])

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join('instance', 'app.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Initialize Socket.IO for real-time updates
socket_manager = SocketManager()
socketio = socket_manager.init_app(app)

# Initialize YouTube downloader with real-time updates
downloader = YouTubeDownloader(socketio)

# Supported languages
SUPPORTED_LANGUAGES = {
    'en': 'English',
    'de': 'Deutsch',
    'fr': 'Français',
    'es': 'Español',
    'it': 'Italiano',
    'uk': 'Українська',
    'ru': 'Русский',
    'eo': 'Esperanto'
}


@app.before_request
def before_request():
    """Set language before each request."""
    # Get language from session or browser preference
    lang = session.get('language')
    
    if not lang:
        # Try to get from Accept-Language header
        best_match = request.accept_languages.best_match(SUPPORTED_LANGUAGES.keys())
        lang = best_match if best_match else 'en'
        session['language'] = lang


@app.context_processor
def inject_translations():
    """Make translations available in all templates."""
    lang = session.get('language', 'en')
    return {
        'translations': get_all_translations(lang),
        'current_language': lang,
        'supported_languages': SUPPORTED_LANGUAGES,
        '_': lambda key: get_translation(lang, key)
    }


@app.route('/')
def index():
    """Render the main page with URL input form."""
    single_form = YouTubeURLForm()
    batch_form = BatchURLForm()
    return render_template('index.html', 
                         single_form=single_form, 
                         batch_form=batch_form,
                         config=Config)


@app.route('/process_url', methods=['POST'])
def process_url():
    """Process a single YouTube URL."""
    form = YouTubeURLForm()
    
    if form.validate_on_submit():
        url = form.url.data
        download_type = form.download_type.data
        
        # Process download directory choice
        use_system_dir = form.use_system_dir.data
        custom_dir = form.download_dir.data if form.download_dir.data else None
        
        # Save to session
        session['use_system_dir'] = use_system_dir
        
        # Configure download directory
        if use_system_dir == 'system':
            # Use system Downloads folder
            Config.set_download_folder(Config.DEFAULT_SYSTEM_DOWNLOAD_FOLDER)
            session['download_dir'] = Config.DEFAULT_SYSTEM_DOWNLOAD_FOLDER
        elif use_system_dir == 'custom' and custom_dir:
            # Use custom directory
            Config.set_download_folder(custom_dir)
            session['download_dir'] = custom_dir
        else:
            # Fallback to system Downloads folder
            Config.set_download_folder(Config.DEFAULT_SYSTEM_DOWNLOAD_FOLDER)
            session['download_dir'] = Config.DEFAULT_SYSTEM_DOWNLOAD_FOLDER
        
        # Downloader now uses Config.DOWNLOAD_FOLDER directly via property
        
        # Store information in session
        session['url'] = url
        session['download_type'] = download_type
        session['download_id'] = str(uuid.uuid4())
        
        try:
            if download_type == 'video':
                # For video, we need to show available formats
                formats = downloader.get_available_formats(url)
                return redirect(url_for('select_format'))
                
            elif download_type == 'audio':
                # For audio, proceed directly to download
                return redirect(url_for('download'))
                
            elif download_type == 'transcript':
                # For transcript, we need to show available languages
                subtitles = downloader.get_available_subtitles(url)
                if not subtitles:
                    flash('No subtitles available for this video.')
                    return redirect(url_for('index'))
                    
                # Store subtitles in session
                session['subtitles'] = subtitles
                return redirect(url_for('select_language'))
                
        except Exception as e:
            logger.error(f"Error processing URL {url}: {str(e)}")
            flash(f"Error: {str(e)}")
            return redirect(url_for('index'))
            
    return render_template('index.html', single_form=form, batch_form=BatchURLForm())


@app.route('/process_batch', methods=['POST'])
def process_batch():
    """Process multiple YouTube URLs."""
    form = BatchURLForm()
    
    if form.validate_on_submit():
        urls_text = form.urls.data
        download_type = form.download_type.data
        
        # Process download directory choice
        use_system_dir = form.use_system_dir.data
        custom_dir = form.download_dir.data if form.download_dir.data else None
        
        # Save to session
        session['use_system_dir'] = use_system_dir
        
        # Configure download directory
        if use_system_dir == 'system':
            # Use system Downloads folder
            Config.set_download_folder(Config.DEFAULT_SYSTEM_DOWNLOAD_FOLDER)
            session['download_dir'] = Config.DEFAULT_SYSTEM_DOWNLOAD_FOLDER
        elif use_system_dir == 'custom' and custom_dir:
            # Use custom directory
            Config.set_download_folder(custom_dir)
            session['download_dir'] = custom_dir
        else:
            # Fallback to system Downloads folder
            Config.set_download_folder(Config.DEFAULT_SYSTEM_DOWNLOAD_FOLDER)
            session['download_dir'] = Config.DEFAULT_SYSTEM_DOWNLOAD_FOLDER
        
        # Downloader now uses Config.DOWNLOAD_FOLDER directly via property
        
        # Split by newline and filter out empty lines
        urls = [url.strip() for url in urls_text.split('\n') if url.strip()]
        
        if not urls:
            flash('Please enter at least one valid URL.')
            return redirect(url_for('index'))
            
        # Store information in session
        session['urls'] = urls
        session['download_type'] = download_type
        session['download_id'] = str(uuid.uuid4())
        session['is_batch'] = True
        
        try:
            if download_type == 'video':
                # For batch video, we still need format selection
                # Use the first URL to get available formats
                formats = downloader.get_available_formats(urls[0])
                return redirect(url_for('select_format'))
                
            elif download_type == 'audio':
                # For audio, proceed directly to batch download
                return redirect(url_for('download'))
                
            elif download_type == 'transcript':
                # For transcript, we need language selection
                subtitles = downloader.get_available_subtitles(urls[0])
                if not subtitles:
                    flash('No subtitles available for the first video.')
                    return redirect(url_for('index'))
                    
                session['subtitles'] = subtitles
                return redirect(url_for('select_language'))
                
        except Exception as e:
            logger.error(f"Error processing batch URLs: {str(e)}")
            flash(f"Error: {str(e)}")
            return redirect(url_for('index'))
            
    return render_template('index.html', single_form=YouTubeURLForm(), batch_form=form)


@app.route('/select_format')
def select_format():
    """Display available video formats for selection."""
    if 'url' not in session and 'urls' not in session:
        flash('Please enter a YouTube URL first.')
        return redirect(url_for('index'))
        
    url = session.get('url') or session.get('urls', [])[0]
    
    try:
        formats = downloader.get_available_formats(url)
        form = FormatSelectionForm()
        
        # Populate format choices
        form.format_selection.choices = [
            (f['format_id'], f"{f['resolution']} ({f.get('format_note', 'mp4')})")
            for f in formats
        ]
        
        return render_template('select_format.html', form=form, formats=formats)
        
    except Exception as e:
        logger.error(f"Error fetching formats for {url}: {str(e)}")
        flash(f"Error: {str(e)}")
        return redirect(url_for('index'))


@app.route('/select_language')
def select_language():
    """Display available subtitle languages for selection."""
    if 'subtitles' not in session:
        flash('Please enter a YouTube URL first.')
        return redirect(url_for('index'))
        
    subtitles = session.get('subtitles', {})
    form = FormatSelectionForm()
    
    # Populate language choices
    form.format_selection.choices = [
        (lang_code, f"{subtitle_info['name']} ({subtitle_info['type']})")
        for lang_code, subtitle_info in subtitles.items()
    ]
    
    return render_template('select_language.html', form=form, subtitles=subtitles)


@app.route('/submit_format', methods=['POST'])
def submit_format():
    """Process format or language selection and redirect to download."""
    # Get the selected format directly from request
    selected_format = request.form.get('format_selection')
    
    if selected_format:
        # Store the selected format or language in session
        download_type = session.get('download_type')
        
        if download_type == 'video':
            session['selected_format'] = selected_format
        elif download_type == 'transcript':
            session['selected_language'] = selected_format
            
        return redirect(url_for('download'))
        
    flash('Please select a valid option.')
    if session.get('download_type') == 'video':
        return redirect(url_for('select_format'))
    else:
        return redirect(url_for('select_language'))


@app.route('/download')
def download():
    """Show download progress page."""
    download_id = session.get('download_id')
    download_type = session.get('download_type')
    
    if not download_id or not download_type:
        flash('Invalid session. Please start over.')
        return redirect(url_for('index'))
        
    # Collect all necessary session data
    context = {
        'download_id': download_id,
        'download_type': download_type,
        'is_batch': session.get('is_batch', False),
    }
    
    if session.get('is_batch'):
        context['urls'] = session.get('urls', [])
        context['url_count'] = len(context['urls'])
    else:
        context['url'] = session.get('url', '')
        
    if download_type == 'video':
        context['selected_format'] = session.get('selected_format')
    elif download_type == 'transcript':
        context['selected_language'] = session.get('selected_language')
        
    return render_template('download.html', config=Config, **context)


@app.route('/start_download', methods=['POST'])
def start_download():
    """Start the download process."""
    download_id = session.get('download_id')
    download_type = session.get('download_type')
    is_batch = session.get('is_batch', False)
    
    # Debug download location from session
    download_dir = session.get('download_dir')
    use_system_dir = session.get('use_system_dir', 'system')
    logger.info(f"[DEBUG] Starting download with download directory preferences:")
    logger.info(f"[DEBUG] - use_system_dir from session: {use_system_dir}")
    logger.info(f"[DEBUG] - download_dir from session: {download_dir}")
    logger.info(f"[DEBUG] - Current app download folder: {Config.DOWNLOAD_FOLDER}")
    logger.info(f"[DEBUG] - Downloader's folder: {downloader.download_folder}")
    
    if not download_id or not download_type:
        return jsonify({'status': 'error', 'message': 'Invalid session data'}), 400
        
    try:
        result = None
        files = []
        
        if is_batch:
            # Process batch download
            urls = session.get('urls', [])
            format_id = session.get('selected_format') if download_type == 'video' else None
            lang_code = session.get('selected_language') if download_type == 'transcript' else None
            
            # Process batch directly (without background task for now)
            results = downloader.process_batch(
                urls=urls,
                download_type=download_type,
                format_id=format_id,
                lang_code=lang_code,
                room=download_id
            )
            
            # Extract filenames from results
            for result in results:
                if result.get('status') == 'success' and 'filename' in result:
                    files.append(result['filename'])
            
            return jsonify({
                'status': 'success',
                'message': 'Batch download completed',
                'files': files
            })
            
        else:
            # Process single download
            url = session.get('url')
            filename = None
            
            if download_type == 'video':
                format_id = session.get('selected_format')
                filename = downloader.download_video(
                    url=url,
                    format_id=format_id,
                    room=download_id
                )
                
            elif download_type == 'audio':
                filename = downloader.download_audio(
                    url=url,
                    room=download_id
                )
                
            elif download_type == 'transcript':
                lang_code = session.get('selected_language')
                filename = downloader.download_subtitles(
                    url=url,
                    lang_code=lang_code,
                    room=download_id
                )
            
            if filename:
                files.append(filename)
                
            return jsonify({
                'status': 'success',
                'message': 'Download completed',
                'files': files
            })
            
    except Exception as e:
        logger.error(f"Error starting download: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/download_file/<filename>')
def download_file(filename):
    """Serve a downloaded file."""
    # Ensure the filename is secure and doesn't contain path traversal
    safe_filename = secure_filename(filename)
    
    # Get the actual download directory from Config
    download_directory = Config.DOWNLOAD_FOLDER
    logger.info(f"[DEBUG] Serving file: {safe_filename} from directory: {download_directory}")
    
    # Verify that the file exists in the download directory
    download_path = Path(download_directory)
    file_path = download_path / safe_filename
    
    if not file_path.exists() or not file_path.is_file():
        logger.error(f"[DEBUG] File not found at: {file_path}")
        flash('File not found.')
        return redirect(url_for('index'))
        
    # Determine the file type for the correct MIME type
    return send_from_directory(
        download_directory,
        safe_filename,
        as_attachment=True
    )


@app.route('/completed')
def completed():
    """Show download completion page with links to downloaded files."""
    files = request.args.getlist('files')
    download_type = session.get('download_type', 'unknown')
    
    if not files:
        flash('No downloaded files found.')
        return redirect(url_for('index'))
        
    # Clear session data that's no longer needed
    for key in ['url', 'urls', 'download_type', 'selected_format', 'selected_language', 'is_batch']:
        if key in session:
            session.pop(key)
            
    return render_template('completed.html', files=files, download_type=download_type, config=Config)


@app.route('/cleanup', methods=['POST'])
def cleanup():
    """Clean up old downloads."""
    try:
        count = downloader.cleanup_old_files()
        return jsonify({'status': 'success', 'count': count})
    except Exception as e:
        logger.error(f"Error during cleanup: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/set_language/<language>')
def set_language(language):
    """Set the user's language preference."""
    if language in SUPPORTED_LANGUAGES:
        session['language'] = language
        # Store the referrer to redirect back
        referrer = request.referrer or url_for('index')
        return redirect(referrer)
    else:
        flash('Unsupported language')
        return redirect(url_for('index'))


@app.route('/api/directories/browse', methods=['GET'])
def browse_directories():
    """API endpoint to browse directories."""
    current_path = request.args.get('path', os.path.expanduser('~'))
    
    try:
        # Normalize path
        current_path = os.path.abspath(current_path)
        
        # Get parent directory
        parent_path = os.path.dirname(current_path) if current_path != '/' else None
        
        # List directories in current path
        directories = []
        if os.path.exists(current_path) and os.path.isdir(current_path):
            for item in sorted(os.listdir(current_path)):
                item_path = os.path.join(current_path, item)
                try:
                    if os.path.isdir(item_path) and not item.startswith('.'):
                        directories.append({
                            'name': item,
                            'path': item_path
                        })
                except PermissionError:
                    continue
        
        return jsonify({
            'status': 'success',
            'current_path': current_path,
            'parent_path': parent_path,
            'directories': directories
        })
        
    except Exception as e:
        logger.error(f"Error browsing directories: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/directories/common', methods=['GET'])
def get_common_directories():
    """Get common system directories."""
    home_dir = os.path.expanduser('~')
    system = platform.system()
    
    common_dirs = []
    
    if system == "Windows":
        common_dirs = [
            {"name": "Downloads", "path": os.path.join(home_dir, "Downloads")},
            {"name": "Documents", "path": os.path.join(home_dir, "Documents")},
            {"name": "Desktop", "path": os.path.join(home_dir, "Desktop")},
            {"name": "Videos", "path": os.path.join(home_dir, "Videos")},
            {"name": "Music", "path": os.path.join(home_dir, "Music")}
        ]
    elif system == "Darwin":  # macOS
        common_dirs = [
            {"name": "Downloads", "path": os.path.join(home_dir, "Downloads")},
            {"name": "Documents", "path": os.path.join(home_dir, "Documents")},
            {"name": "Desktop", "path": os.path.join(home_dir, "Desktop")},
            {"name": "Movies", "path": os.path.join(home_dir, "Movies")},
            {"name": "Music", "path": os.path.join(home_dir, "Music")}
        ]
        
        # Add external volumes
        volumes_dir = "/Volumes"
        try:
            if os.path.exists(volumes_dir):
                for volume in os.listdir(volumes_dir):
                    vol_path = os.path.join(volumes_dir, volume)
                    if os.path.isdir(vol_path) and volume not in ["Macintosh HD"]:
                        common_dirs.append({"name": f"External: {volume}", "path": vol_path})
        except Exception as e:
            logger.warning(f"Error listing volumes: {str(e)}")
    else:  # Linux
        common_dirs = [
            {"name": "Downloads", "path": os.path.join(home_dir, "Downloads")},
            {"name": "Documents", "path": os.path.join(home_dir, "Documents")},
            {"name": "Desktop", "path": os.path.join(home_dir, "Desktop")},
            {"name": "Videos", "path": os.path.join(home_dir, "Videos")},
            {"name": "Music", "path": os.path.join(home_dir, "Music")}
        ]
    
    # Filter existing directories
    valid_dirs = []
    for directory in common_dirs:
        try:
            if os.path.exists(directory["path"]) and os.path.isdir(directory["path"]):
                valid_dirs.append(directory)
        except:
            pass
    
    return jsonify({"directories": valid_dirs})


@app.route('/api/settings/save', methods=['POST'])
def save_settings():
    """Save directory settings."""
    try:
        data = request.get_json()
        directory_type = data.get('directory_type', 'system')
        custom_directory = data.get('custom_directory', '')
        
        # Update session
        session['use_system_dir'] = directory_type
        session['download_dir'] = custom_directory if directory_type == 'custom' else Config.DEFAULT_SYSTEM_DOWNLOAD_FOLDER
        
        # Update configuration
        if directory_type == 'custom' and custom_directory:
            Config.set_download_folder(custom_directory)
        else:
            Config.set_download_folder(Config.DEFAULT_SYSTEM_DOWNLOAD_FOLDER)
            
        # Downloader now uses Config.DOWNLOAD_FOLDER directly via property
        
        return jsonify({
            'status': 'success',
            'message': 'Settings saved successfully'
        })
        
    except Exception as e:
        logger.error(f"Error saving settings: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/directories/validate', methods=['POST'])
def validate_directory():
    """Validate if a directory exists and is writable."""
    try:
        data = request.get_json()
        directory_path = data.get('path', '')
        
        if not directory_path:
            return jsonify({
                'status': 'error',
                'message': 'No directory path provided'
            }), 400
            
        # Check if directory exists
        if not os.path.exists(directory_path):
            return jsonify({
                'status': 'error',
                'message': 'Directory does not exist'
            }), 404
            
        # Check if it's a directory
        if not os.path.isdir(directory_path):
            return jsonify({
                'status': 'error',
                'message': 'Path is not a directory'
            }), 400
            
        # Check if writable
        if not os.access(directory_path, os.W_OK):
            return jsonify({
                'status': 'error',
                'message': 'Directory is not writable'
            }), 403
            
        return jsonify({
            'status': 'success',
            'message': 'Directory is valid and writable'
        })
        
    except Exception as e:
        logger.error(f"Error validating directory: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/license')
def serve_license():
    """Serve the LICENSE file."""
    return send_from_directory(
        app.root_path,
        'LICENSE',
        mimetype='text/plain'
    )


@app.route('/favicon.ico')
def favicon():
    """Serve favicon.ico from static/img directory."""
    return send_from_directory(
        os.path.join(app.root_path, 'static', 'img'),
        'favicon.svg',
        mimetype='image/svg+xml'
    )


@app.route('/robots.txt')
def robots():
    """Serve robots.txt from static directory."""
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'robots.txt',
        mimetype='text/plain'
    )


@app.route('/open_download_folder', methods=['POST'])
def open_download_folder():
    """Open the download folder in the system's file explorer."""
    try:
        # Check if running locally (not on a remote server)
        remote_addr = request.remote_addr
        is_local = remote_addr in ['127.0.0.1', 'localhost', '::1'] or request.host.startswith('localhost')
        
        if not is_local:
            return jsonify({
                'status': 'warning',
                'message': 'File explorer can only be opened when running the server locally'
            }), 200
        
        # Get the folder to open from request or use current config
        data = request.get_json() or {}
        directory_type = data.get('directory_type')
        custom_directory = data.get('custom_directory')
        
        # Determine which folder to open
        if directory_type == 'custom' and custom_directory:
            download_folder = os.path.expanduser(custom_directory)
        elif directory_type == 'system':
            download_folder = Config.DEFAULT_SYSTEM_DOWNLOAD_FOLDER
        else:
            # Fallback to current config
            download_folder = Config.DOWNLOAD_FOLDER
        
        # Ensure the folder exists
        if not os.path.exists(download_folder):
            os.makedirs(download_folder, exist_ok=True)
        
        # Open the folder based on the operating system
        system = platform.system()
        
        if system == 'Darwin':  # macOS
            subprocess.Popen(['open', download_folder])
        elif system == 'Windows':
            subprocess.Popen(['explorer', download_folder])
        elif system == 'Linux':
            # Try different file managers
            try:
                subprocess.Popen(['xdg-open', download_folder])
            except:
                # Fallback to common file managers
                for fm in ['nautilus', 'dolphin', 'thunar', 'pcmanfm']:
                    try:
                        subprocess.Popen([fm, download_folder])
                        break
                    except:
                        continue
        
        return jsonify({
            'status': 'success',
            'message': 'Download folder opened',
            'folder': download_folder
        })
        
    except Exception as e:
        logger.error(f"Error opening download folder: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': f'Could not open download folder: {str(e)}'
        }), 500


@app.route('/open_file_location/<filename>', methods=['POST'])
def open_file_location(filename):
    """Open the file location in the system's file explorer and select the file."""
    try:
        # Check if running locally
        remote_addr = request.remote_addr
        is_local = remote_addr in ['127.0.0.1', 'localhost', '::1'] or request.host.startswith('localhost')
        
        if not is_local:
            return jsonify({
                'status': 'warning',
                'message': 'File explorer can only be opened when running the server locally'
            }), 200
        
        # Secure the filename
        safe_filename = secure_filename(filename)
        file_path = os.path.join(Config.DOWNLOAD_FOLDER, safe_filename)
        
        # Check if file exists
        if not os.path.exists(file_path):
            return jsonify({
                'status': 'error',
                'message': 'File not found'
            }), 404
        
        # Open the file location based on the operating system
        system = platform.system()
        
        if system == 'Darwin':  # macOS
            # Open Finder and select the file
            subprocess.Popen(['open', '-R', file_path])
        elif system == 'Windows':
            # Open Explorer and select the file
            subprocess.Popen(['explorer', '/select,', file_path])
        elif system == 'Linux':
            # Open the containing folder
            folder = os.path.dirname(file_path)
            try:
                subprocess.Popen(['xdg-open', folder])
            except:
                # Fallback to common file managers
                for fm in ['nautilus', 'dolphin', 'thunar', 'pcmanfm']:
                    try:
                        subprocess.Popen([fm, folder])
                        break
                    except:
                        continue
        
        return jsonify({
            'status': 'success',
            'message': 'File location opened',
            'file': safe_filename
        })
        
    except Exception as e:
        logger.error(f"Error opening file location: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': f'Could not open file location: {str(e)}'
        }), 500


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    logger.error(f"Server error: {str(e)}")
    return render_template('500.html'), 500


if __name__ == '__main__':
    # Only create instance directory for logs, not download folder
    os.makedirs('instance', exist_ok=True)
    
    # Print server URL and copyright
    print("\n" + "="*60)
    print("YouTube Downloader")
    print("Copyright (c) 2025 Olga Meier GmbH, Switzerland")
    print("Licensed under MIT License")
    print("Place of jurisdiction is Zug, Switzerland. Swiss law applies.")
    print("\nDISCLAIMER: USE AT YOUR OWN RISK!")
    print("This software is provided 'AS IS' without warranty of any kind.")
    print("No support is provided.")
    print("="*60)
    print(f"\nServer running at: http://localhost:8080")
    print("Press Ctrl+C to stop the server\n")
    
    # Run the app with SocketIO
    socketio.run(app, host='0.0.0.0', port=8080, debug=app.config['DEBUG'], allow_unsafe_werkzeug=True)