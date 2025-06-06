"""Form definitions for the YouTube Downloader application."""

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL, ValidationError, Optional
import re
from urllib.parse import urlparse
from config import Config
from utils.file_utils import is_valid_directory


def validate_youtube_url(form, field):
    """Validate that the URL is from an allowed YouTube domain."""
    try:
        parsed_url = urlparse(field.data)
        domain = parsed_url.netloc.lower()
        
        # Remove 'www.' prefix if present
        if domain.startswith('www.'):
            domain = domain[4:]
            
        if domain not in Config.ALLOWED_DOMAINS and not any(domain.endswith(f".{d}") for d in Config.ALLOWED_DOMAINS):
            raise ValidationError('Only YouTube URLs are allowed.')
            
        # Ensure the URL has a video ID or playlist ID
        path = parsed_url.path
        query = parsed_url.query
        
        # Check for video ID (either /watch?v=ID or /v/ID or youtu.be/ID)
        video_id_pattern = r'(?:v=|/v/|youtu\.be/)([a-zA-Z0-9_-]{11})'
        playlist_pattern = r'list=([a-zA-Z0-9_-]+)'
        
        if not (re.search(video_id_pattern, field.data) or re.search(playlist_pattern, field.data)):
            raise ValidationError('Invalid YouTube URL format. Must contain a video or playlist.')
            
    except Exception:
        raise ValidationError('Invalid URL format.')
        
        
def validate_directory(form, field):
    """Validate that the directory path is valid and writable."""
    # Skip validation if field is empty (will use default)
    if not field.data:
        return
        
    if not is_valid_directory(field.data):
        raise ValidationError('Invalid directory path or insufficient permissions.')


class YouTubeURLForm(FlaskForm):
    """Form for entering YouTube URLs and selecting download type."""
    
    url = StringField('YouTube URL', validators=[
        DataRequired(message='Please enter a YouTube URL.'),
        URL(message='Please enter a valid URL.'),
        validate_youtube_url
    ])
    
    download_type = RadioField('Download Type', choices=[
        ('video', 'Video (.mp4)'),
        ('audio', 'Audio (.mp3)'),
        ('transcript', 'Transcript (.txt - clean text)')
    ], default='video', validators=[DataRequired()])
    
    download_dir = StringField('Download Directory (Optional)', validators=[
        Optional(),
        validate_directory
    ])
    
    use_system_dir = RadioField('Save Location', choices=[
        ('system', 'Save in system Downloads folder'),
        ('custom', 'Save in custom location')
    ], default='system', validators=[DataRequired()])
    
    submit = SubmitField('Continue')


class BatchURLForm(FlaskForm):
    """Form for entering multiple YouTube URLs for batch processing."""
    
    urls = TextAreaField('YouTube URLs (one per line)', validators=[
        DataRequired(message='Please enter at least one YouTube URL.')
    ])
    
    download_type = RadioField('Download Type', choices=[
        ('video', 'Video (.mp4)'),
        ('audio', 'Audio (.mp3)'),
        ('transcript', 'Transcript (.txt - clean text)')
    ], default='video', validators=[DataRequired()])
    
    download_dir = StringField('Download Directory (Optional)', validators=[
        Optional(),
        validate_directory
    ])
    
    use_system_dir = RadioField('Save Location', choices=[
        ('system', 'Save in system Downloads folder'),
        ('custom', 'Save in custom location')
    ], default='system', validators=[DataRequired()])
    
    submit = SubmitField('Continue')
    
    def validate_urls(self, field):
        """Validate all URLs in the batch."""
        urls = [url.strip() for url in field.data.split('\n') if url.strip()]
        if not urls:
            raise ValidationError('Please enter at least one YouTube URL.')
            
        for url in urls:
            try:
                parsed_url = urlparse(url)
                domain = parsed_url.netloc.lower()
                
                # Remove 'www.' prefix if present
                if domain.startswith('www.'):
                    domain = domain[4:]
                    
                if domain not in Config.ALLOWED_DOMAINS and not any(domain.endswith(f".{d}") for d in Config.ALLOWED_DOMAINS):
                    raise ValidationError(f'Only YouTube URLs are allowed. Invalid URL: {url}')
                    
                # Ensure the URL has a video ID or playlist ID
                video_id_pattern = r'(?:v=|/v/|youtu\.be/)([a-zA-Z0-9_-]{11})'
                playlist_pattern = r'list=([a-zA-Z0-9_-]+)'
                
                if not (re.search(video_id_pattern, url) or re.search(playlist_pattern, url)):
                    raise ValidationError(f'Invalid YouTube URL format: {url}')
                    
            except Exception:
                raise ValidationError(f'Invalid URL format: {url}')


class FormatSelectionForm(FlaskForm):
    """Form for selecting video format/resolution or subtitle language."""
    
    format_selection = SelectField('Select Format', validators=[DataRequired()])
    submit = SubmitField('Download')


# Preferences form removed