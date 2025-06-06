/**
 * YouTube Downloader - Main JavaScript
 * Copyright (c) 2025 Olga Meier GmbH, Switzerland
 * Licensed under MIT License
 */

document.addEventListener('DOMContentLoaded', function() {
    // Enable tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });
    
    // Form validation
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
    
    // URL input validation (show preview when possible)
    const urlInput = document.getElementById('url');
    if (urlInput) {
        urlInput.addEventListener('input', debounce(function(e) {
            const url = e.target.value.trim();
            if (isYoutubeUrl(url)) {
                urlInput.classList.remove('is-invalid');
                urlInput.classList.add('is-valid');
            } else if (url.length > 0) {
                urlInput.classList.remove('is-valid');
                urlInput.classList.add('is-invalid');
            } else {
                urlInput.classList.remove('is-valid', 'is-invalid');
            }
        }, 300));
    }
    
    // Directory Browser Functionality
    const browseBtn = document.getElementById('browse_btn');
    const directoryBrowserModal = document.getElementById('directoryBrowserModal');
    const directoryList = document.getElementById('directory_list');
    const currentPathSpan = document.getElementById('current_path');
    const selectDirBtn = document.getElementById('select_directory_btn');
    const customDirInput = document.getElementById('custom_dir_input');
    
    let currentPath = '';
    
    // Initialize directory browser when modal opens
    if (directoryBrowserModal) {
        directoryBrowserModal.addEventListener('show.bs.modal', function() {
            loadDirectories(currentPath || customDirInput.value || '~');
        });
    }
    
    // Load directories function
    async function loadDirectories(path) {
        try {
            const response = await fetch(`/api/directories/browse?path=${encodeURIComponent(path)}`);
            const data = await response.json();
            
            if (data.status === 'success') {
                currentPath = data.current_path;
                currentPathSpan.textContent = currentPath;
                
                directoryList.innerHTML = '';
                
                // Add parent directory option
                if (data.parent_path) {
                    const parentItem = createDirectoryItem('..', data.parent_path, true);
                    directoryList.appendChild(parentItem);
                }
                
                // Add directories
                data.directories.forEach(dir => {
                    const item = createDirectoryItem(dir.name, dir.path, false);
                    directoryList.appendChild(item);
                });
                
                if (data.directories.length === 0 && !data.parent_path) {
                    directoryList.innerHTML = '<div class="text-muted text-center p-3">No subdirectories found</div>';
                }
            } else {
                showAlert('Error loading directories: ' + data.message, 'danger');
            }
        } catch (error) {
            showAlert('Error loading directories: ' + error.message, 'danger');
        }
    }
    
    // Create directory item element
    function createDirectoryItem(name, path, isParent) {
        const item = document.createElement('div');
        item.className = 'directory-item';
        item.innerHTML = `
            <i class="fas fa-folder${isParent ? '-open' : ''} me-2"></i>
            ${name}
        `;
        item.addEventListener('click', () => loadDirectories(path));
        return item;
    }
    
    // Select directory button
    if (selectDirBtn) {
        selectDirBtn.addEventListener('click', function() {
            customDirInput.value = currentPath;
            bootstrap.Modal.getInstance(directoryBrowserModal).hide();
        });
    }
    
    // Load common directories on page load
    loadCommonDirectories();
    
    async function loadCommonDirectories() {
        try {
            const response = await fetch('/api/directories/common');
            const data = await response.json();
            
            const quickAccessDiv = document.getElementById('quick_access_dirs');
            if (quickAccessDiv && data.directories) {
                quickAccessDiv.innerHTML = '';
                data.directories.forEach(dir => {
                    const col = document.createElement('div');
                    col.className = 'col-6 col-md-4 mb-2';
                    col.innerHTML = `
                        <button type="button" class="btn btn-outline-secondary btn-sm w-100" 
                                onclick="document.getElementById('custom_dir_input').value='${dir.path.replace(/'/g, "\\'")}'">
                            <i class="fas fa-folder me-1"></i>${dir.name}
                        </button>
                    `;
                    quickAccessDiv.appendChild(col);
                });
            }
        } catch (error) {
            console.error('Error loading common directories:', error);
        }
    }
    
    // Save settings functionality
    const saveSettingsBtn = document.getElementById('save_settings_btn');
    if (saveSettingsBtn) {
        saveSettingsBtn.addEventListener('click', async function() {
            const dirType = document.querySelector('input[name="directory_type"]:checked').value;
            const customDir = customDirInput.value;
            
            // Validate custom directory if selected
            if (dirType === 'custom' && customDir) {
                try {
                    const validateResponse = await fetch('/api/directories/validate', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ path: customDir })
                    });
                    
                    const validateData = await validateResponse.json();
                    if (validateData.status !== 'success') {
                        showAlert(validateData.message, 'danger');
                        return;
                    }
                } catch (error) {
                    showAlert('Error validating directory: ' + error.message, 'danger');
                    return;
                }
            }
            
            // Save settings
            try {
                const response = await fetch('/api/settings/save', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        directory_type: dirType,
                        custom_directory: customDir
                    })
                });
                
                const data = await response.json();
                if (data.status === 'success') {
                    // Update localStorage
                    localStorage.setItem('directory_type', dirType);
                    localStorage.setItem('custom_directory', customDir);
                    
                    // Update form fields
                    updateFormFields(dirType, customDir);
                    
                    // Show success message
                    const savedMsg = document.getElementById('settings_saved_msg');
                    savedMsg.style.display = 'inline';
                    setTimeout(() => {
                        savedMsg.style.display = 'none';
                    }, 3000);
                } else {
                    showAlert('Error saving settings: ' + data.message, 'danger');
                }
            } catch (error) {
                showAlert('Error saving settings: ' + error.message, 'danger');
            }
        });
    }
    
    // Update form fields based on settings
    function updateFormFields(dirType, customDir) {
        // Update single form
        const singleUseSystemDir = document.getElementById('single_use_system_dir');
        const singleDownloadDir = document.getElementById('single_download_dir');
        if (singleUseSystemDir) singleUseSystemDir.value = dirType;
        if (singleDownloadDir) singleDownloadDir.value = customDir;
        
        // Update batch form
        const batchUseSystemDir = document.getElementById('batch_use_system_dir');
        const batchDownloadDir = document.getElementById('batch_download_dir');
        if (batchUseSystemDir) batchUseSystemDir.value = dirType;
        if (batchDownloadDir) batchDownloadDir.value = customDir;
    }
    
    // Clean up periodically (admin function)
    const cleanupButton = document.getElementById('cleanup_button');
    if (cleanupButton) {
        cleanupButton.addEventListener('click', async function() {
            if (confirm('Are you sure you want to remove old downloads?')) {
                try {
                    const response = await fetch('/cleanup', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                    const data = await response.json();
                    if (data.status === 'success') {
                        showAlert(`Cleanup complete. Removed ${data.count} files.`, 'success');
                    } else {
                        showAlert('Cleanup failed: ' + data.message, 'danger');
                    }
                } catch (error) {
                    showAlert('Error: ' + error.message, 'danger');
                }
            }
        });
    }
});

/**
 * Debounce function to limit how often a function can be called
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Validate if a URL is a valid YouTube URL
 */
function isYoutubeUrl(url) {
    if (!url) return false;
    
    // Check if it's a valid URL
    try {
        const urlObj = new URL(url);
        const hostname = urlObj.hostname.toLowerCase();
        
        // Check if it's a YouTube domain
        const validDomains = ['youtube.com', 'youtu.be', 'm.youtube.com', 'www.youtube.com'];
        const isYoutubeDomain = validDomains.some(domain => 
            hostname === domain || hostname.endsWith('.' + domain)
        );
        
        if (!isYoutubeDomain) return false;
        
        // Check if it has a video ID or playlist ID
        const path = urlObj.pathname;
        const search = urlObj.search;
        
        // Video ID patterns
        const hasVideoId = 
            search.includes('v=') || // youtube.com/watch?v=ID
            path.match(/\/v\/([a-zA-Z0-9_-]{11})/) || // youtube.com/v/ID
            hostname === 'youtu.be' && path.length > 1; // youtu.be/ID
            
        // Playlist pattern
        const hasPlaylistId = search.includes('list=');
        
        return hasVideoId || hasPlaylistId;
        
    } catch (e) {
        return false;
    }
}

/**
 * Show alert message
 */
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'danger' ? 'exclamation-triangle' : 'info-circle'} me-2"></i>
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

/**
 * Show toast notification
 */
window.showToast = function(message, type = 'info') {
    const toastHtml = `
        <div class="toast align-items-center text-white bg-${type} border-0" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="d-flex">
                <div class="toast-body">
                    <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'danger' ? 'exclamation-triangle' : type === 'warning' ? 'exclamation-circle' : 'info-circle'} me-2"></i>
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        </div>
    `;
    
    // Create toast container if it doesn't exist
    let toastContainer = document.getElementById('toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'toast-container';
        toastContainer.className = 'toast-container position-fixed bottom-0 end-0 p-3';
        toastContainer.style.zIndex = '1080';
        document.body.appendChild(toastContainer);
    }
    
    // Add toast to container
    const toastElement = document.createElement('div');
    toastElement.innerHTML = toastHtml;
    toastContainer.appendChild(toastElement);
    
    // Initialize and show toast
    const toast = new bootstrap.Toast(toastElement.querySelector('.toast'), {
        autohide: true,
        delay: 3000
    });
    toast.show();
    
    // Remove toast element after it's hidden
    toastElement.addEventListener('hidden.bs.toast', () => {
        toastElement.remove();
    });
}