# Contributing to YouTube Downloader

First off, thank you for considering contributing to YouTube Downloader! It's people like you that make this tool better for everyone.

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples**
* **Describe the behavior you observed and what you expected**
* **Include screenshots if possible**
* **Include your environment details** (OS, Python version, browser)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a detailed description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and expected behavior**
* **Explain why this enhancement would be useful**

### Pull Requests

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes following our coding standards
4. Write or update tests as needed
5. Update documentation as needed
6. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
7. Push to the branch (`git push origin feature/AmazingFeature`)
8. Open a Pull Request

## Development Guidelines

### Setting Up Development Environment

```bash
# Clone your fork
git clone https://github.com/your-username/youtube-downloader.git
cd youtube-downloader

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install pytest flake8 mypy black

# Install pre-commit hooks (optional)
pre-commit install
```

### Coding Standards

#### Python Code Style
- Follow PEP 8
- Use type hints where appropriate
- Maximum line length: 100 characters
- Use Black for code formatting
- All code and comments must be in English

#### File Organization
- Keep files under 250 lines
- Create new modules when files grow too large
- Follow the existing project structure

#### Documentation
- Write docstrings for all functions (Google style)
- Update README.md for new features
- Comment complex logic with `# Reason:` explanations

Example docstring:
```python
def download_video(url: str, format_id: str = None) -> str:
    """
    Download a video from YouTube.
    
    Args:
        url: The YouTube video URL.
        format_id: Optional format identifier for quality selection.
        
    Returns:
        The filename of the downloaded video.
        
    Raises:
        ValueError: If the URL is invalid or download fails.
    """
```

### Testing

#### Writing Tests
- Write tests for all new features
- Place tests in the `/tests` directory
- Use pytest for testing
- Aim for at least 80% code coverage

#### Test Structure
```python
def test_feature_normal_case():
    """Test the expected use case."""
    pass

def test_feature_edge_case():
    """Test edge cases."""
    pass

def test_feature_error_case():
    """Test error handling."""
    pass
```

#### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_downloader.py
```

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Add batch download progress indicators

- Show individual file progress in batch mode
- Add total progress calculation
- Update UI to display current file being processed

Fixes #123
```

### Code Review Process

1. All code must be reviewed before merging
2. Reviews should check for:
   - Code quality and style
   - Test coverage
   - Documentation updates
   - Security implications
   - Performance impact

## Project Structure

When adding new features, maintain the existing structure:

```
/app.py              # Flask routes only
/downloader.py       # Download logic
/forms.py            # Form definitions
/config.py           # Configuration
/socket_manager.py   # WebSocket handling
/utils/              # Helper functions
  ├── file_utils.py
  └── validators.py
/templates/          # HTML templates
/static/             # CSS, JS, images
  ├── css/
  ├── js/
  └── img/
/tests/              # Test files
```

## Translation Guidelines

When adding new features that include user-facing text:

1. Add translations to `translations.py`
2. Use the `_()` function in templates
3. Provide translations for all 8 supported languages
4. Keep translations concise and clear

## Security Considerations

- Never trust user input
- Validate all URLs and filenames
- Prevent path traversal attacks
- Use CSRF tokens for all forms
- Sanitize all output
- Don't expose system paths in errors

## Questions?

Feel free to open an issue with the tag "question" if you have any questions about contributing.

## Legal

By contributing to this project, you agree that your contributions will be licensed under the MIT License and that Olga Meier GmbH retains all rights to the project.

---

Thank you for contributing! 🎉