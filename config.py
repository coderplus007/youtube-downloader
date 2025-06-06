"""Configuration settings for the YouTube Downloader application."""

import os
from pathlib import Path
from utils.file_utils import get_default_download_directory, ensure_directory_exists


class Config:
    """Base configuration class."""
    
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-for-development-only'
    DEBUG = False
    TESTING = False
    
    # Download settings
    DEFAULT_SYSTEM_DOWNLOAD_FOLDER = get_default_download_directory()
    # Always use system download folder by default, no local app folder
    APP_DOWNLOAD_FOLDER = os.environ.get('DOWNLOAD_FOLDER') or DEFAULT_SYSTEM_DOWNLOAD_FOLDER
    DOWNLOAD_FOLDER = APP_DOWNLOAD_FOLDER  # This can be changed at runtime
    MAX_CONTENT_LENGTH = 1024 * 1024 * 1024  # 1GB max upload size
    
    # YouTube settings
    ALLOWED_DOMAINS = ['youtube.com', 'youtu.be', 'm.youtube.com', 'www.youtube.com']
    MAX_VIDEO_DURATION = 10800  # 3 hours in seconds
    
    # File cleanup
    FILE_RETENTION_HOURS = 24  # Files are kept for 24 hours
    
    # WebSocket settings
    SOCKETIO_PING_TIMEOUT = 60
    SOCKETIO_PING_INTERVAL = 25
    
    @classmethod
    def set_download_folder(cls, folder_path: str = None):
        """Set the download folder, ensuring it exists."""
        if folder_path:
            cls.DOWNLOAD_FOLDER = ensure_directory_exists(folder_path)
        else:
            cls.DOWNLOAD_FOLDER = ensure_directory_exists(cls.DEFAULT_SYSTEM_DOWNLOAD_FOLDER)


class DevelopmentConfig(Config):
    """Development configuration."""
    
    DEBUG = True
    

class TestingConfig(Config):
    """Testing configuration."""
    
    TESTING = True
    DEBUG = True
    DOWNLOAD_FOLDER = str(Path(__file__).parent / 'tests' / 'downloads')


class ProductionConfig(Config):
    """Production configuration."""
    
    # In production, SECRET_KEY should be set as an environment variable
    # But we'll provide a fallback for easier testing
    SECRET_KEY = os.environ.get('SECRET_KEY', 'prod-key-for-testing-only-please-change-in-production')
    
    # Use stronger file retention policy in production
    FILE_RETENTION_HOURS = 12


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# Don't create any app-specific download directory
# Downloads will be handled by user-configured paths only