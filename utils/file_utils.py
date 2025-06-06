"""Utility functions for file handling."""

import os
import platform
from pathlib import Path
import tempfile


def get_default_download_directory() -> str:
    """
    Get the default download directory for the current operating system.
    
    Returns:
        str: The path to the default download directory
    """
    system = platform.system()
    
    if system == "Windows":
        # On Windows, use the Downloads folder in the user profile
        return str(Path.home() / "Downloads")
    elif system == "Darwin":  # macOS
        # On macOS, use the Downloads folder in the user's home
        return str(Path.home() / "Downloads")
    elif system == "Linux":
        # On Linux, use the Downloads folder in the user's home
        return str(Path.home() / "Downloads")
    else:
        # Fallback to a temporary directory
        return tempfile.gettempdir()


def ensure_directory_exists(directory: str) -> str:
    """
    Ensure that the specified directory exists, creating it if necessary.
    
    Args:
        directory (str): The directory path to check/create
        
    Returns:
        str: The validated directory path
    """
    # Convert to Path for easier manipulation
    dir_path = Path(directory)
    
    # Create the directory if it doesn't exist
    try:
        os.makedirs(dir_path, exist_ok=True)
        return str(dir_path)
    except Exception as e:
        # If we can't create the directory, fall back to the default downloads dir
        print(f"Error creating directory {directory}: {e}")
        fallback_dir = get_default_download_directory()
        os.makedirs(fallback_dir, exist_ok=True)
        return fallback_dir


def is_valid_directory(directory: str) -> bool:
    """
    Check if a directory path is valid and writable.
    
    Args:
        directory (str): The directory path to check
        
    Returns:
        bool: True if the directory is valid and writable, False otherwise
    """
    if not directory:
        return False
        
    # Convert to Path for easier manipulation
    dir_path = Path(directory)
    
    # Check if the directory exists and is writable
    if not dir_path.exists():
        try:
            os.makedirs(dir_path, exist_ok=True)
        except Exception:
            return False
    
    # Check if it's a directory and we have write permissions
    return dir_path.is_dir() and os.access(str(dir_path), os.W_OK)