"""
Translation strings for the YouTube Downloader application.
Copyright (c) 2025 Olga Meier GmbH, Switzerland
Licensed under MIT License
"""

translations = {
    'en': {
        'app_name': 'YouTube Downloader',
        'home': 'Home',
        'about': 'About',
        'language': 'Language',
        'support_ukraine': 'Support Ukraine',
        
        # Main page
        'download_youtube_content': 'Download YouTube Content',
        'single_url': 'Single URL',
        'batch_download': 'Batch Download',
        'settings': 'Settings',
        'youtube_url': 'YouTube URL',
        'youtube_url_placeholder': 'https://www.youtube.com/watch?v=...',
        'enter_valid_url': 'Enter a valid YouTube video or playlist URL',
        'download_type': 'Download Type',
        'video': 'Video',
        'audio': 'Audio',
        'transcript': 'Transcript',
        'clean_text': 'Clean text file',
        'continue': 'Continue',
        'download': 'Download',
        'download_more': 'Download More',
        
        # Batch
        'youtube_urls_multiline': 'YouTube URLs (one per line)',
        'enter_multiple_urls': 'Enter multiple YouTube URLs, one per line',
        
        # Settings
        'download_directory_settings': 'Download Directory Settings',
        'open_current_folder': 'Open Current Folder',
        'use_system_downloads': 'Use System Downloads Folder',
        'use_custom_directory': 'Use Custom Directory',
        'browse': 'Browse',
        'save_settings': 'Save Settings',
        'settings_saved': 'Settings saved!',
        'download_preferences': 'Download Preferences',
        'auto_open_downloads': 'Automatically open download folder after completion',
        'auto_open_description': 'When enabled, the download folder will open in your file explorer after downloads complete',
        'about_directory_selection': 'About Directory Selection',
        'directory_info': 'You can choose where to save your downloaded files. By default, files are saved to your system\'s Downloads folder. You can also select a custom directory, such as an external drive or a specific project folder.',
        'tip': 'Tip',
        'directory_tip': 'After downloading, the folder will automatically open in your file explorer (Finder on Mac, Explorer on Windows). You can also click "Show in folder" next to any downloaded file to reveal it in the file browser.',
        
        # Progress
        'download_progress': 'Download Progress',
        'batch_progress': 'Batch Download Progress',
        'initializing': 'Initializing download...',
        'processing': 'Processing',
        'preparing': 'Preparing download...',
        'download_details': 'Download Details:',
        'type': 'Type',
        'format': 'Format',
        'language': 'Language',
        
        # Completion
        'download_complete': 'Download Complete!',
        'success_message': 'Your files have been downloaded successfully.',
        'transcript_success': 'The transcript has been saved as a clean text file without timestamps or formatting codes.',
        'downloaded_files': 'Downloaded Files:',
        'open_download_folder': 'Open Download Folder',
        'show_in_folder': 'Show in folder',
        'print_list': 'Print List',
        'did_you_know': 'Did you know?',
        'batch_tip': 'You can download multiple videos at once using our Batch Download feature. Just paste multiple URLs (one per line) in the Batch Download tab!',
        
        # Format selection
        'select_video_format': 'Select Video Format',
        'choose_quality': 'Choose your preferred video quality and format:',
        'best_quality': 'Best Quality',
        'auto_best': 'Automatic best quality',
        'higher_resolution_tip': 'Higher resolutions provide better quality but result in larger file sizes.',
        
        # Language selection
        'select_subtitle_language': 'Select Subtitle Language',
        'choose_language': 'Choose the subtitle language you want to download:',
        'transcript_note': 'The transcript will be downloaded as a clean text file (.txt) without timestamps or formatting codes.',
        'manual': 'Manual',
        'auto_generated': 'Auto-generated',
        'subtitle_tip': 'Manual subtitles are usually more accurate than auto-generated ones. The downloaded file will contain only the spoken text, making it perfect for reading or text processing.',
        
        # How it works
        'how_it_works': 'How It Works',
        'paste_url': 'Paste URL',
        'paste_url_desc': 'Enter a YouTube video or playlist URL',
        'choose_options': 'Choose Options',
        'choose_options_desc': 'Select format, quality, and language',
        'download_desc': 'Get your content with progress tracking',
        
        # Features
        'what_you_can_download': 'What You Can Download',
        'videos': 'Videos',
        'videos_desc': 'Download in various resolutions from 360p to 4K',
        'audio_desc': 'Extract audio as high-quality MP3 files (192kbps)',
        'transcripts': 'Transcripts',
        'transcripts_desc': 'Clean text files without timestamps or formatting',
        
        # Footer
        'powered_by': 'Powered by Flask and yt-dlp',
        'open_source': 'Open Source Software',
        
        # About modal
        'about_title': 'About YouTube Downloader',
        'about_desc': 'YouTube Downloader is a powerful and user-friendly web application for downloading content from YouTube.',
        'features': 'Features:',
        'feature_1': 'Download videos in various formats and resolutions',
        'feature_2': 'Extract audio as MP3 files',
        'feature_3': 'Download subtitles and transcripts',
        'feature_4': 'Batch download multiple URLs',
        'feature_5': 'Real-time progress updates',
        'feature_6': 'Custom download directory selection',
        'technology_stack': 'Technology Stack:',
        'tech_desc': 'Built with Flask, yt-dlp, and Socket.IO for real-time updates.',
        'close': 'Close',
        'view_on_github': 'View on GitHub',
        
        # Errors
        'page_not_found': 'Page Not Found',
        'error_404': 'Oops! The page you\'re looking for doesn\'t exist.',
        'error_404_desc': 'It might have been removed, renamed, or didn\'t exist in the first place.',
        'go_home': 'Go Home',
        'go_back': 'Go Back',
        'server_error': 'Server Error',
        'error_500': 'Something went wrong on our end.',
        'error_500_desc': 'We\'re sorry for the inconvenience. Please try again later or contact support if the problem persists.',
        'try_again': 'Try Again',
        'contact_support': 'If this error persists, please contact support at',
        
        # Form validation
        'please_enter_url': 'Please enter a YouTube URL.',
        'please_enter_valid_url': 'Please enter a valid URL.',
        'only_youtube_allowed': 'Only YouTube URLs are allowed.',
        'invalid_url_format': 'Invalid YouTube URL format. Must contain a video or playlist.',
        'please_enter_one_url': 'Please enter at least one YouTube URL.',
        'invalid_directory': 'Invalid directory path or insufficient permissions.',
        
        # Messages
        'no_subtitles': 'No subtitles available for this video.',
        'no_files_found': 'No downloaded files found.',
        'file_not_found': 'File not found.',
        'cleanup_complete': 'Cleanup complete. Removed',
        'files': 'files.',
        
        # Quick access
        'quick_access': 'Quick Access:',
        'downloads': 'Downloads',
        'desktop': 'Desktop',
        'documents': 'Documents',
        'videos_folder': 'Videos',
        'music': 'Music',
        'external_drive': 'External Drive',
    },
    
    'de': {
        'app_name': 'YouTube Downloader',
        'home': 'Startseite',
        'about': 'Über',
        'language': 'Sprache',
        'support_ukraine': 'Ukraine unterstützen',
        
        # Main page
        'download_youtube_content': 'YouTube-Inhalte herunterladen',
        'single_url': 'Einzelne URL',
        'batch_download': 'Stapel-Download',
        'settings': 'Einstellungen',
        'youtube_url': 'YouTube-URL',
        'youtube_url_placeholder': 'https://www.youtube.com/watch?v=...',
        'enter_valid_url': 'Geben Sie eine gültige YouTube-Video- oder Playlist-URL ein',
        'download_type': 'Download-Typ',
        'video': 'Video',
        'audio': 'Audio',
        'transcript': 'Transkript',
        'clean_text': 'Bereinigte Textdatei',
        'continue': 'Weiter',
        'download': 'Herunterladen',
        'download_more': 'Mehr herunterladen',
        
        # Batch
        'youtube_urls_multiline': 'YouTube-URLs (eine pro Zeile)',
        'enter_multiple_urls': 'Geben Sie mehrere YouTube-URLs ein, eine pro Zeile',
        
        # Settings
        'download_directory_settings': 'Download-Verzeichnis Einstellungen',
        'open_current_folder': 'Aktuellen Ordner öffnen',
        'use_system_downloads': 'System-Downloads-Ordner verwenden',
        'use_custom_directory': 'Benutzerdefinierten Ordner verwenden',
        'browse': 'Durchsuchen',
        'save_settings': 'Einstellungen speichern',
        'settings_saved': 'Einstellungen gespeichert!',
        'download_preferences': 'Download-Einstellungen',
        'auto_open_downloads': 'Download-Ordner nach Abschluss automatisch öffnen',
        'auto_open_description': 'Wenn aktiviert, wird der Download-Ordner nach Abschluss automatisch im Datei-Explorer geöffnet',
        'about_directory_selection': 'Über die Verzeichnisauswahl',
        'directory_info': 'Sie können wählen, wo Ihre heruntergeladenen Dateien gespeichert werden sollen. Standardmäßig werden Dateien im System-Downloads-Ordner gespeichert. Sie können auch ein benutzerdefiniertes Verzeichnis auswählen.',
        'tip': 'Tipp',
        'directory_tip': 'Nach dem Download wird der Ordner automatisch im Datei-Explorer geöffnet. Sie können auch neben jeder heruntergeladenen Datei auf "Im Ordner anzeigen" klicken.',
        
        # Progress
        'download_progress': 'Download-Fortschritt',
        'batch_progress': 'Stapel-Download Fortschritt',
        'initializing': 'Download wird initialisiert...',
        'processing': 'Verarbeitung',
        'preparing': 'Download wird vorbereitet...',
        'download_details': 'Download-Details:',
        'type': 'Typ',
        'format': 'Format',
        'language': 'Sprache',
        
        # Completion
        'download_complete': 'Download abgeschlossen!',
        'success_message': 'Ihre Dateien wurden erfolgreich heruntergeladen.',
        'transcript_success': 'Das Transkript wurde als bereinigte Textdatei ohne Zeitstempel oder Formatierungscodes gespeichert.',
        'downloaded_files': 'Heruntergeladene Dateien:',
        'open_download_folder': 'Download-Ordner öffnen',
        'show_in_folder': 'Im Ordner anzeigen',
        'print_list': 'Liste drucken',
        'did_you_know': 'Wussten Sie schon?',
        'batch_tip': 'Sie können mehrere Videos gleichzeitig herunterladen! Fügen Sie einfach mehrere URLs (eine pro Zeile) im Stapel-Download-Tab ein.',
        
        # Format selection
        'select_video_format': 'Videoformat auswählen',
        'choose_quality': 'Wählen Sie Ihre bevorzugte Videoqualität und Format:',
        'best_quality': 'Beste Qualität',
        'auto_best': 'Automatisch beste Qualität',
        'higher_resolution_tip': 'Höhere Auflösungen bieten bessere Qualität, führen aber zu größeren Dateien.',
        
        # Language selection
        'select_subtitle_language': 'Untertitelsprache auswählen',
        'choose_language': 'Wählen Sie die Untertitelsprache zum Herunterladen:',
        'transcript_note': 'Das Transkript wird als bereinigte Textdatei (.txt) ohne Zeitstempel oder Formatierungscodes heruntergeladen.',
        'manual': 'Manuell',
        'auto_generated': 'Automatisch generiert',
        'subtitle_tip': 'Manuelle Untertitel sind normalerweise genauer als automatisch generierte. Die heruntergeladene Datei enthält nur den gesprochenen Text.',
        
        # How it works
        'how_it_works': 'So funktioniert es',
        'paste_url': 'URL einfügen',
        'paste_url_desc': 'YouTube-Video- oder Playlist-URL eingeben',
        'choose_options': 'Optionen wählen',
        'choose_options_desc': 'Format, Qualität und Sprache auswählen',
        'download_desc': 'Ihre Inhalte mit Fortschrittsverfolgung erhalten',
        
        # Features
        'what_you_can_download': 'Was Sie herunterladen können',
        'videos': 'Videos',
        'videos_desc': 'Download in verschiedenen Auflösungen von 360p bis 4K',
        'audio_desc': 'Audio als hochwertige MP3-Dateien extrahieren (192kbps)',
        'transcripts': 'Transkripte',
        'transcripts_desc': 'Bereinigte Textdateien ohne Zeitstempel oder Formatierung',
        
        # Footer
        'powered_by': 'Angetrieben von Flask und yt-dlp',
        'open_source': 'Open-Source-Software',
        
        # About modal
        'about_title': 'Über YouTube Downloader',
        'about_desc': 'YouTube Downloader ist eine leistungsstarke und benutzerfreundliche Webanwendung zum Herunterladen von YouTube-Inhalten.',
        'features': 'Funktionen:',
        'feature_1': 'Videos in verschiedenen Formaten und Auflösungen herunterladen',
        'feature_2': 'Audio als MP3-Dateien extrahieren',
        'feature_3': 'Untertitel und Transkripte herunterladen',
        'feature_4': 'Stapel-Download mehrerer URLs',
        'feature_5': 'Echtzeit-Fortschrittsaktualisierungen',
        'feature_6': 'Benutzerdefinierte Download-Verzeichnisauswahl',
        'technology_stack': 'Technologie-Stack:',
        'tech_desc': 'Erstellt mit Flask, yt-dlp und Socket.IO für Echtzeit-Updates.',
        'close': 'Schließen',
        'view_on_github': 'Auf GitHub ansehen',
        
        # Errors
        'page_not_found': 'Seite nicht gefunden',
        'error_404': 'Ups! Die gesuchte Seite existiert nicht.',
        'error_404_desc': 'Sie wurde möglicherweise entfernt, umbenannt oder existierte nie.',
        'go_home': 'Zur Startseite',
        'go_back': 'Zurück',
        'server_error': 'Serverfehler',
        'error_500': 'Etwas ist bei uns schiefgelaufen.',
        'error_500_desc': 'Wir entschuldigen uns für die Unannehmlichkeiten. Bitte versuchen Sie es später erneut.',
        'try_again': 'Erneut versuchen',
        'contact_support': 'Wenn dieser Fehler weiterhin besteht, kontaktieren Sie bitte den Support unter',
        
        # Quick access
        'quick_access': 'Schnellzugriff:',
        'downloads': 'Downloads',
        'desktop': 'Desktop',
        'documents': 'Dokumente',
        'videos_folder': 'Videos',
        'music': 'Musik',
        'external_drive': 'Externe Festplatte',
    },
    
    'fr': {
        'app_name': 'YouTube Downloader',
        'home': 'Accueil',
        'about': 'À propos',
        'language': 'Langue',
        'support_ukraine': 'Soutenir l\'Ukraine',
        
        # Main page
        'download_youtube_content': 'Télécharger du contenu YouTube',
        'single_url': 'URL unique',
        'batch_download': 'Téléchargement par lot',
        'settings': 'Paramètres',
        'youtube_url': 'URL YouTube',
        'youtube_url_placeholder': 'https://www.youtube.com/watch?v=...',
        'enter_valid_url': 'Entrez une URL de vidéo ou playlist YouTube valide',
        'download_type': 'Type de téléchargement',
        'video': 'Vidéo',
        'audio': 'Audio',
        'transcript': 'Transcription',
        'clean_text': 'Fichier texte propre',
        'continue': 'Continuer',
        'download': 'Télécharger',
        'download_more': 'Télécharger plus',
        
        # Batch
        'youtube_urls_multiline': 'URLs YouTube (une par ligne)',
        'enter_multiple_urls': 'Entrez plusieurs URLs YouTube, une par ligne',
        
        # Settings
        'download_directory_settings': 'Paramètres du répertoire de téléchargement',
        'open_current_folder': 'Ouvrir le dossier actuel',
        'use_system_downloads': 'Utiliser le dossier Téléchargements système',
        'use_custom_directory': 'Utiliser un répertoire personnalisé',
        'browse': 'Parcourir',
        'save_settings': 'Enregistrer les paramètres',
        'settings_saved': 'Paramètres enregistrés!',
        'download_preferences': 'Préférences de téléchargement',
        'auto_open_downloads': 'Ouvrir automatiquement le dossier après téléchargement',
        'auto_open_description': 'Si activé, le dossier de téléchargement s\'ouvrira automatiquement après la fin',
        'about_directory_selection': 'À propos de la sélection du répertoire',
        'directory_info': 'Vous pouvez choisir où enregistrer vos fichiers téléchargés. Par défaut, les fichiers sont enregistrés dans le dossier Téléchargements du système.',
        'tip': 'Astuce',
        'directory_tip': 'Après le téléchargement, le dossier s\'ouvrira automatiquement dans votre explorateur de fichiers.',
        
        # Progress
        'download_progress': 'Progression du téléchargement',
        'batch_progress': 'Progression du téléchargement par lot',
        'initializing': 'Initialisation du téléchargement...',
        'processing': 'Traitement',
        'preparing': 'Préparation du téléchargement...',
        'download_details': 'Détails du téléchargement:',
        'type': 'Type',
        'format': 'Format',
        'language': 'Langue',
        
        # Completion
        'download_complete': 'Téléchargement terminé!',
        'success_message': 'Vos fichiers ont été téléchargés avec succès.',
        'transcript_success': 'La transcription a été enregistrée comme fichier texte propre sans horodatages ni codes de formatage.',
        'downloaded_files': 'Fichiers téléchargés:',
        'open_download_folder': 'Ouvrir le dossier de téléchargement',
        'show_in_folder': 'Afficher dans le dossier',
        'print_list': 'Imprimer la liste',
        'did_you_know': 'Le saviez-vous?',
        'batch_tip': 'Vous pouvez télécharger plusieurs vidéos à la fois! Collez simplement plusieurs URLs (une par ligne) dans l\'onglet Téléchargement par lot.',
        
        # Format selection
        'select_video_format': 'Sélectionner le format vidéo',
        'choose_quality': 'Choisissez votre qualité et format vidéo préférés:',
        'best_quality': 'Meilleure qualité',
        'auto_best': 'Meilleure qualité automatique',
        'higher_resolution_tip': 'Les résolutions plus élevées offrent une meilleure qualité mais des fichiers plus volumineux.',
        
        # Language selection
        'select_subtitle_language': 'Sélectionner la langue des sous-titres',
        'choose_language': 'Choisissez la langue des sous-titres à télécharger:',
        'transcript_note': 'La transcription sera téléchargée comme fichier texte propre (.txt) sans horodatages ni codes de formatage.',
        'manual': 'Manuel',
        'auto_generated': 'Généré automatiquement',
        'subtitle_tip': 'Les sous-titres manuels sont généralement plus précis que ceux générés automatiquement.',
        
        # How it works
        'how_it_works': 'Comment ça marche',
        'paste_url': 'Coller l\'URL',
        'paste_url_desc': 'Entrez une URL de vidéo ou playlist YouTube',
        'choose_options': 'Choisir les options',
        'choose_options_desc': 'Sélectionnez le format, la qualité et la langue',
        'download_desc': 'Obtenez votre contenu avec suivi de progression',
        
        # Features
        'what_you_can_download': 'Ce que vous pouvez télécharger',
        'videos': 'Vidéos',
        'videos_desc': 'Télécharger dans diverses résolutions de 360p à 4K',
        'audio_desc': 'Extraire l\'audio en fichiers MP3 haute qualité (192kbps)',
        'transcripts': 'Transcriptions',
        'transcripts_desc': 'Fichiers texte propres sans horodatages ni formatage',
        
        # Footer
        'powered_by': 'Propulsé par Flask et yt-dlp',
        'open_source': 'Logiciel Open Source',
        
        # About modal
        'about_title': 'À propos de YouTube Downloader',
        'about_desc': 'YouTube Downloader est une application web puissante et conviviale pour télécharger du contenu YouTube.',
        'features': 'Fonctionnalités:',
        'feature_1': 'Télécharger des vidéos dans divers formats et résolutions',
        'feature_2': 'Extraire l\'audio en fichiers MP3',
        'feature_3': 'Télécharger les sous-titres et transcriptions',
        'feature_4': 'Téléchargement par lot de plusieurs URLs',
        'feature_5': 'Mises à jour de progression en temps réel',
        'feature_6': 'Sélection personnalisée du répertoire de téléchargement',
        'technology_stack': 'Stack technologique:',
        'tech_desc': 'Construit avec Flask, yt-dlp et Socket.IO pour les mises à jour en temps réel.',
        'close': 'Fermer',
        'view_on_github': 'Voir sur GitHub',
        
        # Errors
        'page_not_found': 'Page non trouvée',
        'error_404': 'Oups! La page que vous cherchez n\'existe pas.',
        'error_404_desc': 'Elle a peut-être été supprimée, renommée ou n\'a jamais existé.',
        'go_home': 'Retour à l\'accueil',
        'go_back': 'Retour',
        'server_error': 'Erreur serveur',
        'error_500': 'Quelque chose s\'est mal passé de notre côté.',
        'error_500_desc': 'Nous nous excusons pour le désagrément. Veuillez réessayer plus tard.',
        'try_again': 'Réessayer',
        'contact_support': 'Si cette erreur persiste, veuillez contacter le support à',
        
        # Form validation
        'please_enter_url': 'Veuillez entrer une URL YouTube.',
        'please_enter_valid_url': 'Veuillez entrer une URL valide.',
        'only_youtube_allowed': 'Seules les URLs YouTube sont autorisées.',
        'invalid_url_format': 'Format d\'URL YouTube invalide. Doit contenir une vidéo ou playlist.',
        'please_enter_one_url': 'Veuillez entrer au moins une URL YouTube.',
        'invalid_directory': 'Chemin de répertoire invalide ou permissions insuffisantes.',
        
        # Messages
        'no_subtitles': 'Aucun sous-titre disponible pour cette vidéo.',
        'no_files_found': 'Aucun fichier téléchargé trouvé.',
        'file_not_found': 'Fichier non trouvé.',
        'cleanup_complete': 'Nettoyage terminé. Supprimé',
        'files': 'fichiers.',
        
        # Quick access
        'quick_access': 'Accès rapide:',
        'downloads': 'Téléchargements',
        'desktop': 'Bureau',
        'documents': 'Documents',
        'videos_folder': 'Vidéos',
        'music': 'Musique',
        'external_drive': 'Disque externe',
    },
    
    'es': {
        'app_name': 'YouTube Downloader',
        'home': 'Inicio',
        'about': 'Acerca de',
        'language': 'Idioma',
        'support_ukraine': 'Apoyar a Ucrania',
        
        # Main page
        'download_youtube_content': 'Descargar contenido de YouTube',
        'single_url': 'URL única',
        'batch_download': 'Descarga por lotes',
        'settings': 'Configuración',
        'youtube_url': 'URL de YouTube',
        'youtube_url_placeholder': 'https://www.youtube.com/watch?v=...',
        'enter_valid_url': 'Ingrese una URL válida de video o lista de YouTube',
        'download_type': 'Tipo de descarga',
        'video': 'Video',
        'audio': 'Audio',
        'transcript': 'Transcripción',
        'clean_text': 'Archivo de texto limpio',
        'continue': 'Continuar',
        'download': 'Descargar',
        'download_more': 'Descargar más',
        
        # Batch
        'youtube_urls_multiline': 'URLs de YouTube (una por línea)',
        'enter_multiple_urls': 'Ingrese varias URLs de YouTube, una por línea',
        
        # Settings
        'download_directory_settings': 'Configuración del directorio de descarga',
        'open_current_folder': 'Abrir carpeta actual',
        'use_system_downloads': 'Usar carpeta de Descargas del sistema',
        'use_custom_directory': 'Usar directorio personalizado',
        'browse': 'Examinar',
        'save_settings': 'Guardar configuración',
        'settings_saved': '¡Configuración guardada!',
        'download_preferences': 'Preferencias de descarga',
        'auto_open_downloads': 'Abrir automáticamente la carpeta después de completar',
        'auto_open_description': 'Si está activado, la carpeta de descarga se abrirá automáticamente al finalizar',
        'about_directory_selection': 'Acerca de la selección de directorio',
        'directory_info': 'Puede elegir dónde guardar sus archivos descargados. Por defecto, los archivos se guardan en la carpeta Descargas del sistema.',
        'tip': 'Consejo',
        'directory_tip': 'Después de la descarga, la carpeta se abrirá automáticamente en su explorador de archivos.',
        
        # Progress
        'download_progress': 'Progreso de descarga',
        'batch_progress': 'Progreso de descarga por lotes',
        'initializing': 'Inicializando descarga...',
        'processing': 'Procesando',
        'preparing': 'Preparando descarga...',
        'download_details': 'Detalles de descarga:',
        'type': 'Tipo',
        'format': 'Formato',
        'language': 'Idioma',
        
        # Completion
        'download_complete': '¡Descarga completa!',
        'success_message': 'Sus archivos se han descargado exitosamente.',
        'transcript_success': 'La transcripción se ha guardado como archivo de texto limpio sin marcas de tiempo ni códigos de formato.',
        'downloaded_files': 'Archivos descargados:',
        'open_download_folder': 'Abrir carpeta de descarga',
        'show_in_folder': 'Mostrar en carpeta',
        'print_list': 'Imprimir lista',
        'did_you_know': '¿Sabías que?',
        'batch_tip': '¡Puedes descargar varios videos a la vez! Solo pega múltiples URLs (una por línea) en la pestaña de Descarga por lotes.',
        
        # Format selection
        'select_video_format': 'Seleccionar formato de video',
        'choose_quality': 'Elija su calidad y formato de video preferidos:',
        'best_quality': 'Mejor calidad',
        'auto_best': 'Mejor calidad automática',
        'higher_resolution_tip': 'Las resoluciones más altas ofrecen mejor calidad pero archivos más grandes.',
        
        # Language selection
        'select_subtitle_language': 'Seleccionar idioma de subtítulos',
        'choose_language': 'Elija el idioma de subtítulos para descargar:',
        'transcript_note': 'La transcripción se descargará como archivo de texto limpio (.txt) sin marcas de tiempo ni códigos de formato.',
        'manual': 'Manual',
        'auto_generated': 'Generado automáticamente',
        'subtitle_tip': 'Los subtítulos manuales suelen ser más precisos que los generados automáticamente.',
        
        # How it works
        'how_it_works': 'Cómo funciona',
        'paste_url': 'Pegar URL',
        'paste_url_desc': 'Ingrese una URL de video o lista de YouTube',
        'choose_options': 'Elegir opciones',
        'choose_options_desc': 'Seleccione formato, calidad e idioma',
        'download_desc': 'Obtén tu contenido con seguimiento de progreso',
        
        # Features
        'what_you_can_download': 'Lo que puedes descargar',
        'videos': 'Videos',
        'videos_desc': 'Descargar en varias resoluciones desde 360p hasta 4K',
        'audio_desc': 'Extraer audio como archivos MP3 de alta calidad (192kbps)',
        'transcripts': 'Transcripciones',
        'transcripts_desc': 'Archivos de texto limpios sin marcas de tiempo ni formato',
        
        # Footer
        'powered_by': 'Desarrollado con Flask y yt-dlp',
        'open_source': 'Software de código abierto',
        
        # About modal
        'about_title': 'Acerca de YouTube Downloader',
        'about_desc': 'YouTube Downloader es una aplicación web potente y fácil de usar para descargar contenido de YouTube.',
        'features': 'Características:',
        'feature_1': 'Descargar videos en varios formatos y resoluciones',
        'feature_2': 'Extraer audio como archivos MP3',
        'feature_3': 'Descargar subtítulos y transcripciones',
        'feature_4': 'Descarga por lotes de múltiples URLs',
        'feature_5': 'Actualizaciones de progreso en tiempo real',
        'feature_6': 'Selección personalizada de directorio de descarga',
        'technology_stack': 'Stack tecnológico:',
        'tech_desc': 'Construido con Flask, yt-dlp y Socket.IO para actualizaciones en tiempo real.',
        'close': 'Cerrar',
        'view_on_github': 'Ver en GitHub',
        
        # Errors
        'page_not_found': 'Página no encontrada',
        'error_404': '¡Ups! La página que buscas no existe.',
        'error_404_desc': 'Puede haber sido eliminada, renombrada o nunca existió.',
        'go_home': 'Ir al inicio',
        'go_back': 'Volver',
        'server_error': 'Error del servidor',
        'error_500': 'Algo salió mal de nuestro lado.',
        'error_500_desc': 'Disculpa las molestias. Por favor intenta de nuevo más tarde.',
        'try_again': 'Intentar de nuevo',
        'contact_support': 'Si este error persiste, por favor contacta soporte en',
        
        # Form validation
        'please_enter_url': 'Por favor ingrese una URL de YouTube.',
        'please_enter_valid_url': 'Por favor ingrese una URL válida.',
        'only_youtube_allowed': 'Solo se permiten URLs de YouTube.',
        'invalid_url_format': 'Formato de URL de YouTube inválido. Debe contener un video o lista.',
        'please_enter_one_url': 'Por favor ingrese al menos una URL de YouTube.',
        'invalid_directory': 'Ruta de directorio inválida o permisos insuficientes.',
        
        # Messages
        'no_subtitles': 'No hay subtítulos disponibles para este video.',
        'no_files_found': 'No se encontraron archivos descargados.',
        'file_not_found': 'Archivo no encontrado.',
        'cleanup_complete': 'Limpieza completa. Eliminados',
        'files': 'archivos.',
        
        # Quick access
        'quick_access': 'Acceso rápido:',
        'downloads': 'Descargas',
        'desktop': 'Escritorio',
        'documents': 'Documentos',
        'videos_folder': 'Videos',
        'music': 'Música',
        'external_drive': 'Disco externo',
    },
    
    'uk': {
        'app_name': 'YouTube Downloader',
        'home': 'Головна',
        'about': 'Про програму',
        'language': 'Мова',
        'support_ukraine': 'Підтримати Україну',
        
        # Main page
        'download_youtube_content': 'Завантажити контент з YouTube',
        'single_url': 'Одна URL-адреса',
        'batch_download': 'Масове завантаження',
        'settings': 'Налаштування',
        'youtube_url': 'URL YouTube',
        'youtube_url_placeholder': 'https://www.youtube.com/watch?v=...',
        'enter_valid_url': 'Введіть дійсну URL-адресу відео або плейлиста YouTube',
        'download_type': 'Тип завантаження',
        'video': 'Відео',
        'audio': 'Аудіо',
        'transcript': 'Транскрипт',
        'clean_text': 'Чистий текстовий файл',
        'continue': 'Продовжити',
        'download': 'Завантажити',
        'download_more': 'Завантажити ще',
        
        # Batch
        'youtube_urls_multiline': 'URL-адреси YouTube (одна на рядок)',
        'enter_multiple_urls': 'Введіть декілька URL-адрес YouTube, по одній на рядок',
        
        # Settings
        'download_directory_settings': 'Налаштування директорії завантаження',
        'open_current_folder': 'Відкрити поточну папку',
        'use_system_downloads': 'Використовувати системну папку Завантаження',
        'use_custom_directory': 'Використовувати власну директорію',
        'browse': 'Оглянути',
        'save_settings': 'Зберегти налаштування',
        'settings_saved': 'Налаштування збережено!',
        'download_preferences': 'Налаштування завантаження',
        'auto_open_downloads': 'Автоматично відкривати папку після завершення',
        'auto_open_description': 'Якщо ввімкнено, папка завантажень автоматично відкриється після завершення',
        'about_directory_selection': 'Про вибір директорії',
        'directory_info': 'Ви можете вибрати, де зберігати завантажені файли. За замовчуванням файли зберігаються в системній папці Завантаження.',
        'tip': 'Порада',
        'directory_tip': 'Після завантаження папка автоматично відкриється у вашому файловому менеджері.',
        
        # Progress
        'download_progress': 'Прогрес завантаження',
        'batch_progress': 'Прогрес масового завантаження',
        'initializing': 'Ініціалізація завантаження...',
        'processing': 'Обробка',
        'preparing': 'Підготовка завантаження...',
        'download_details': 'Деталі завантаження:',
        'type': 'Тип',
        'format': 'Формат',
        'language': 'Мова',
        
        # Completion
        'download_complete': 'Завантаження завершено!',
        'success_message': 'Ваші файли успішно завантажено.',
        'transcript_success': 'Транскрипт збережено як чистий текстовий файл без часових міток або кодів форматування.',
        'downloaded_files': 'Завантажені файли:',
        'open_download_folder': 'Відкрити папку завантажень',
        'show_in_folder': 'Показати в папці',
        'print_list': 'Роздрукувати список',
        'did_you_know': 'Чи знали ви?',
        'batch_tip': 'Ви можете завантажувати декілька відео одночасно! Просто вставте декілька URL (по одній на рядок) у вкладці Масове завантаження.',
        
        # Format selection
        'select_video_format': 'Вибрати формат відео',
        'choose_quality': 'Виберіть бажану якість та формат відео:',
        'best_quality': 'Найкраща якість',
        'auto_best': 'Автоматично найкраща якість',
        'higher_resolution_tip': 'Вищі роздільності забезпечують кращу якість, але більші файли.',
        
        # Language selection
        'select_subtitle_language': 'Вибрати мову субтитрів',
        'choose_language': 'Виберіть мову субтитрів для завантаження:',
        'transcript_note': 'Транскрипт буде завантажено як чистий текстовий файл (.txt) без часових міток або кодів форматування.',
        'manual': 'Ручні',
        'auto_generated': 'Автоматично створені',
        'subtitle_tip': 'Ручні субтитри зазвичай точніші за автоматично створені.',
        
        # How it works
        'how_it_works': 'Як це працює',
        'paste_url': 'Вставити URL',
        'paste_url_desc': 'Введіть URL відео або плейлиста YouTube',
        'choose_options': 'Вибрати опції',
        'choose_options_desc': 'Виберіть формат, якість та мову',
        'download_desc': 'Отримайте ваш контент з відстеженням прогресу',
        
        # Features
        'what_you_can_download': 'Що ви можете завантажити',
        'videos': 'Відео',
        'videos_desc': 'Завантаження в різних роздільностях від 360p до 4K',
        'audio_desc': 'Вилучення аудіо як високоякісні MP3-файли (192kbps)',
        'transcripts': 'Транскрипти',
        'transcripts_desc': 'Чисті текстові файли без часових міток або форматування',
        
        # Footer
        'powered_by': 'Працює на Flask та yt-dlp',
        'open_source': 'Програмне забезпечення з відкритим кодом',
        
        # About modal
        'about_title': 'Про YouTube Downloader',
        'about_desc': 'YouTube Downloader - це потужний та зручний веб-додаток для завантаження контенту з YouTube.',
        'features': 'Можливості:',
        'feature_1': 'Завантаження відео в різних форматах та роздільностях',
        'feature_2': 'Вилучення аудіо як MP3-файли',
        'feature_3': 'Завантаження субтитрів та транскриптів',
        'feature_4': 'Масове завантаження декількох URL',
        'feature_5': 'Оновлення прогресу в реальному часі',
        'feature_6': 'Власний вибір директорії для завантаження',
        'technology_stack': 'Технологічний стек:',
        'tech_desc': 'Побудовано на Flask, yt-dlp та Socket.IO для оновлень в реальному часі.',
        'close': 'Закрити',
        'view_on_github': 'Переглянути на GitHub',
        
        # Errors
        'page_not_found': 'Сторінку не знайдено',
        'error_404': 'Упс! Сторінка, яку ви шукаєте, не існує.',
        'error_404_desc': 'Можливо, її було видалено, перейменовано або вона ніколи не існувала.',
        'go_home': 'На головну',
        'go_back': 'Назад',
        'server_error': 'Помилка сервера',
        'error_500': 'Щось пішло не так з нашого боку.',
        'error_500_desc': 'Перепрошуємо за незручності. Будь ласка, спробуйте пізніше.',
        'try_again': 'Спробувати ще',
        'contact_support': 'Якщо ця помилка повторюється, зверніться до служби підтримки за адресою',
        
        # Form validation
        'please_enter_url': 'Будь ласка, введіть URL YouTube.',
        'please_enter_valid_url': 'Будь ласка, введіть дійсну URL.',
        'only_youtube_allowed': 'Дозволені лише URL YouTube.',
        'invalid_url_format': 'Невірний формат URL YouTube. Має містити відео або плейлист.',
        'please_enter_one_url': 'Будь ласка, введіть хоча б одну URL YouTube.',
        'invalid_directory': 'Невірний шлях до директорії або недостатні дозволи.',
        
        # Messages
        'no_subtitles': 'Немає субтитрів для цього відео.',
        'no_files_found': 'Завантажені файли не знайдено.',
        'file_not_found': 'Файл не знайдено.',
        'cleanup_complete': 'Очищення завершено. Видалено',
        'files': 'файлів.',
        
        # Quick access
        'quick_access': 'Швидкий доступ:',
        'downloads': 'Завантаження',
        'desktop': 'Робочий стіл',
        'documents': 'Документи',
        'videos_folder': 'Відео',
        'music': 'Музика',
        'external_drive': 'Зовнішній диск',
    },
    
    'ru': {
        'app_name': 'YouTube Downloader',
        'home': 'Главная',
        'about': 'О программе',
        'language': 'Язык',
        'support_ukraine': 'Поддержать Украину',
        
        # Main page
        'download_youtube_content': 'Скачать контент с YouTube',
        'single_url': 'Одиночная ссылка',
        'batch_download': 'Массовая загрузка',
        'settings': 'Настройки',
        'youtube_url': 'URL YouTube',
        'youtube_url_placeholder': 'https://www.youtube.com/watch?v=...',
        'enter_valid_url': 'Введите действительную ссылку на видео или плейлист YouTube',
        'download_type': 'Тип загрузки',
        'video': 'Видео',
        'audio': 'Аудио',
        'transcript': 'Транскрипт',
        'clean_text': 'Чистый текстовый файл',
        'continue': 'Продолжить',
        'download': 'Скачать',
        'download_more': 'Скачать ещё',
        
        # Batch
        'youtube_urls_multiline': 'URL-адреса YouTube (по одному на строку)',
        'enter_multiple_urls': 'Введите несколько URL-адресов YouTube, по одному на строку',
        
        # Settings
        'download_directory_settings': 'Настройки директории загрузки',
        'open_current_folder': 'Открыть текущую папку',
        'use_system_downloads': 'Использовать системную папку Загрузки',
        'use_custom_directory': 'Использовать пользовательскую директорию',
        'browse': 'Обзор',
        'save_settings': 'Сохранить настройки',
        'settings_saved': 'Настройки сохранены!',
        'download_preferences': 'Настройки загрузки',
        'auto_open_downloads': 'Автоматически открывать папку после завершения',
        'auto_open_description': 'Если включено, папка загрузок автоматически откроется после завершения',
        'about_directory_selection': 'О выборе директории',
        'directory_info': 'Вы можете выбрать, где сохранять загруженные файлы. По умолчанию файлы сохраняются в системной папке Загрузки.',
        'tip': 'Совет',
        'directory_tip': 'После загрузки папка автоматически откроется в вашем файловом менеджере.',
        
        # Progress
        'download_progress': 'Прогресс загрузки',
        'batch_progress': 'Прогресс массовой загрузки',
        'initializing': 'Инициализация загрузки...',
        'processing': 'Обработка',
        'preparing': 'Подготовка загрузки...',
        'download_details': 'Детали загрузки:',
        'type': 'Тип',
        'format': 'Формат',
        'language': 'Язык',
        
        # Completion
        'download_complete': 'Загрузка завершена!',
        'success_message': 'Ваши файлы успешно загружены.',
        'transcript_success': 'Транскрипт сохранён как чистый текстовый файл без временных меток или кодов форматирования.',
        'downloaded_files': 'Загруженные файлы:',
        'open_download_folder': 'Открыть папку загрузок',
        'show_in_folder': 'Показать в папке',
        'print_list': 'Распечатать список',
        'did_you_know': 'Знали ли вы?',
        'batch_tip': 'Вы можете загружать несколько видео одновременно! Просто вставьте несколько URL (по одному на строку) во вкладке Массовая загрузка.',
        
        # Format selection
        'select_video_format': 'Выбрать формат видео',
        'choose_quality': 'Выберите предпочтительные качество и формат видео:',
        'best_quality': 'Лучшее качество',
        'auto_best': 'Автоматически лучшее качество',
        'higher_resolution_tip': 'Более высокие разрешения обеспечивают лучшее качество, но большие файлы.',
        
        # Language selection
        'select_subtitle_language': 'Выбрать язык субтитров',
        'choose_language': 'Выберите язык субтитров для загрузки:',
        'transcript_note': 'Транскрипт будет загружен как чистый текстовый файл (.txt) без временных меток или кодов форматирования.',
        'manual': 'Ручные',
        'auto_generated': 'Автоматически созданные',
        'subtitle_tip': 'Ручные субтитры обычно более точные, чем автоматически созданные.',
        
        # How it works
        'how_it_works': 'Как это работает',
        'paste_url': 'Вставить URL',
        'paste_url_desc': 'Введите URL видео или плейлиста YouTube',
        'choose_options': 'Выбрать опции',
        'choose_options_desc': 'Выберите формат, качество и язык',
        'download_desc': 'Получите ваш контент с отслеживанием прогресса',
        
        # Features
        'what_you_can_download': 'Что вы можете скачать',
        'videos': 'Видео',
        'videos_desc': 'Загрузка в различных разрешениях от 360p до 4K',
        'audio_desc': 'Извлечение аудио как высококачественные MP3-файлы (192kbps)',
        'transcripts': 'Транскрипты',
        'transcripts_desc': 'Чистые текстовые файлы без временных меток или форматирования',
        
        # Footer
        'powered_by': 'Работает на Flask и yt-dlp',
        'open_source': 'Программное обеспечение с открытым исходным кодом',
        
        # About modal
        'about_title': 'О YouTube Downloader',
        'about_desc': 'YouTube Downloader - это мощное и удобное веб-приложение для загрузки контента с YouTube.',
        'features': 'Возможности:',
        'feature_1': 'Загрузка видео в различных форматах и разрешениях',
        'feature_2': 'Извлечение аудио как MP3-файлы',
        'feature_3': 'Загрузка субтитров и транскриптов',
        'feature_4': 'Массовая загрузка нескольких URL',
        'feature_5': 'Обновления прогресса в реальном времени',
        'feature_6': 'Пользовательский выбор директории для загрузки',
        'technology_stack': 'Технологический стек:',
        'tech_desc': 'Построено на Flask, yt-dlp и Socket.IO для обновлений в реальном времени.',
        'close': 'Закрыть',
        'view_on_github': 'Посмотреть на GitHub',
        
        # Errors
        'page_not_found': 'Страница не найдена',
        'error_404': 'Упс! Страница, которую вы ищете, не существует.',
        'error_404_desc': 'Она могла быть удалена, переименована или никогда не существовала.',
        'go_home': 'На главную',
        'go_back': 'Назад',
        'server_error': 'Ошибка сервера',
        'error_500': 'Что-то пошло не так с нашей стороны.',
        'error_500_desc': 'Приносим извинения за неудобства. Пожалуйста, попробуйте позже.',
        'try_again': 'Попробовать снова',
        'contact_support': 'Если эта ошибка повторяется, обратитесь в службу поддержки по адресу',
        
        # Form validation
        'please_enter_url': 'Пожалуйста, введите URL YouTube.',
        'please_enter_valid_url': 'Пожалуйста, введите действительный URL.',
        'only_youtube_allowed': 'Разрешены только URL YouTube.',
        'invalid_url_format': 'Неверный формат URL YouTube. Должен содержать видео или плейлист.',
        'please_enter_one_url': 'Пожалуйста, введите хотя бы один URL YouTube.',
        'invalid_directory': 'Неверный путь к директории или недостаточные разрешения.',
        
        # Messages
        'no_subtitles': 'Нет субтитров для этого видео.',
        'no_files_found': 'Загруженные файлы не найдены.',
        'file_not_found': 'Файл не найден.',
        'cleanup_complete': 'Очистка завершена. Удалено',
        'files': 'файлов.',
        
        # Quick access
        'quick_access': 'Быстрый доступ:',
        'downloads': 'Загрузки',
        'desktop': 'Рабочий стол',
        'documents': 'Документы',
        'videos_folder': 'Видео',
        'music': 'Музыка',
        'external_drive': 'Внешний диск',
    },
    
    'it': {
        'app_name': 'YouTube Downloader',
        'home': 'Home',
        'about': 'Informazioni',
        'language': 'Lingua',
        'support_ukraine': 'Sostieni l\'Ucraina',
        
        # Main page
        'download_youtube_content': 'Scarica contenuti da YouTube',
        'single_url': 'URL singolo',
        'batch_download': 'Download multiplo',
        'settings': 'Impostazioni',
        'youtube_url': 'URL YouTube',
        'youtube_url_placeholder': 'https://www.youtube.com/watch?v=...',
        'enter_valid_url': 'Inserisci un URL valido di un video o playlist YouTube',
        'download_type': 'Tipo di download',
        'video': 'Video',
        'audio': 'Audio',
        'transcript': 'Trascrizione',
        'clean_text': 'File di testo pulito',
        'continue': 'Continua',
        'download': 'Scarica',
        'download_more': 'Scarica altro',
        
        # Batch
        'youtube_urls_multiline': 'URL YouTube (uno per riga)',
        'enter_multiple_urls': 'Inserisci più URL YouTube, uno per riga',
        
        # Settings
        'download_directory_settings': 'Impostazioni cartella download',
        'open_current_folder': 'Apri cartella corrente',
        'use_system_downloads': 'Usa cartella Download di sistema',
        'use_custom_directory': 'Usa cartella personalizzata',
        'browse': 'Sfoglia',
        'save_settings': 'Salva impostazioni',
        'settings_saved': 'Impostazioni salvate!',
        'download_preferences': 'Preferenze download',
        'auto_open_downloads': 'Apri automaticamente la cartella dopo il completamento',
        'auto_open_description': 'Se abilitato, la cartella download si aprirà automaticamente al termine',
        'about_directory_selection': 'Informazioni sulla selezione cartella',
        'directory_info': 'Puoi scegliere dove salvare i file scaricati. Per impostazione predefinita, i file vengono salvati nella cartella Download del sistema.',
        'tip': 'Suggerimento',
        'directory_tip': 'Dopo il download, la cartella si aprirà automaticamente nel tuo file explorer.',
        
        # Progress
        'download_progress': 'Progresso download',
        'batch_progress': 'Progresso download multiplo',
        'initializing': 'Inizializzazione download...',
        'processing': 'Elaborazione',
        'preparing': 'Preparazione download...',
        'download_details': 'Dettagli download:',
        'type': 'Tipo',
        'format': 'Formato',
        'language': 'Lingua',
        
        # Completion
        'download_complete': 'Download completato!',
        'success_message': 'I tuoi file sono stati scaricati con successo.',
        'transcript_success': 'La trascrizione è stata salvata come file di testo pulito senza timestamp o codici di formattazione.',
        'downloaded_files': 'File scaricati:',
        'open_download_folder': 'Apri cartella download',
        'show_in_folder': 'Mostra nella cartella',
        'print_list': 'Stampa lista',
        'did_you_know': 'Lo sapevi?',
        'batch_tip': 'Puoi scaricare più video contemporaneamente! Incolla semplicemente più URL (uno per riga) nella scheda Download multiplo.',
        
        # Format selection
        'select_video_format': 'Seleziona formato video',
        'choose_quality': 'Scegli la qualità e il formato video preferiti:',
        'best_quality': 'Migliore qualità',
        'auto_best': 'Migliore qualità automatica',
        'higher_resolution_tip': 'Risoluzioni più alte offrono qualità migliore ma file più grandi.',
        
        # Language selection
        'select_subtitle_language': 'Seleziona lingua sottotitoli',
        'choose_language': 'Scegli la lingua dei sottotitoli da scaricare:',
        'transcript_note': 'La trascrizione verrà scaricata come file di testo pulito (.txt) senza timestamp o codici di formattazione.',
        'manual': 'Manuale',
        'auto_generated': 'Generato automaticamente',
        'subtitle_tip': 'I sottotitoli manuali sono solitamente più accurati di quelli generati automaticamente.',
        
        # How it works
        'how_it_works': 'Come funziona',
        'paste_url': 'Incolla URL',
        'paste_url_desc': 'Inserisci l\'URL di un video o playlist YouTube',
        'choose_options': 'Scegli opzioni',
        'choose_options_desc': 'Seleziona formato, qualità e lingua',
        'download_desc': 'Ottieni il tuo contenuto con tracciamento del progresso',
        
        # Features
        'what_you_can_download': 'Cosa puoi scaricare',
        'videos': 'Video',
        'videos_desc': 'Scarica in varie risoluzioni da 360p a 4K',
        'audio_desc': 'Estrai audio come file MP3 di alta qualità (192kbps)',
        'transcripts': 'Trascrizioni',
        'transcripts_desc': 'File di testo puliti senza timestamp o formattazione',
        
        # Footer
        'powered_by': 'Basato su Flask e yt-dlp',
        'open_source': 'Software Open Source',
        
        # About modal
        'about_title': 'Informazioni su YouTube Downloader',
        'about_desc': 'YouTube Downloader è un\'applicazione web potente e facile da usare per scaricare contenuti da YouTube.',
        'features': 'Caratteristiche:',
        'feature_1': 'Scarica video in vari formati e risoluzioni',
        'feature_2': 'Estrai audio come file MP3',
        'feature_3': 'Scarica sottotitoli e trascrizioni',
        'feature_4': 'Download multiplo di più URL',
        'feature_5': 'Aggiornamenti del progresso in tempo reale',
        'feature_6': 'Selezione personalizzata della cartella di download',
        'technology_stack': 'Stack tecnologico:',
        'tech_desc': 'Costruito con Flask, yt-dlp e Socket.IO per aggiornamenti in tempo reale.',
        'close': 'Chiudi',
        'view_on_github': 'Vedi su GitHub',
        
        # Errors
        'page_not_found': 'Pagina non trovata',
        'error_404': 'Ops! La pagina che stai cercando non esiste.',
        'error_404_desc': 'Potrebbe essere stata rimossa, rinominata o non è mai esistita.',
        'go_home': 'Vai alla home',
        'go_back': 'Torna indietro',
        'server_error': 'Errore del server',
        'error_500': 'Qualcosa è andato storto dal nostro lato.',
        'error_500_desc': 'Ci scusiamo per l\'inconveniente. Per favore riprova più tardi.',
        'try_again': 'Riprova',
        'contact_support': 'Se questo errore persiste, contatta il supporto a',
        
        # Form validation
        'please_enter_url': 'Per favore inserisci un URL YouTube.',
        'please_enter_valid_url': 'Per favore inserisci un URL valido.',
        'only_youtube_allowed': 'Sono ammessi solo URL YouTube.',
        'invalid_url_format': 'Formato URL YouTube non valido. Deve contenere un video o playlist.',
        'please_enter_one_url': 'Per favore inserisci almeno un URL YouTube.',
        'invalid_directory': 'Percorso cartella non valido o permessi insufficienti.',
        
        # Messages
        'no_subtitles': 'Nessun sottotitolo disponibile per questo video.',
        'no_files_found': 'Nessun file scaricato trovato.',
        'file_not_found': 'File non trovato.',
        'cleanup_complete': 'Pulizia completata. Rimossi',
        'files': 'file.',
        
        # Quick access
        'quick_access': 'Accesso rapido:',
        'downloads': 'Download',
        'desktop': 'Desktop',
        'documents': 'Documenti',
        'videos_folder': 'Video',
        'music': 'Musica',
        'external_drive': 'Disco esterno',
    },
    
    'eo': {
        'app_name': 'YouTube Elŝutilo',
        'home': 'Hejmo',
        'about': 'Pri',
        'language': 'Lingvo',
        'support_ukraine': 'Subteni Ukrainion',
        
        # Main page
        'download_youtube_content': 'Elŝuti YouTube-enhavon',
        'single_url': 'Unuopa URL',
        'batch_download': 'Amasa elŝuto',
        'settings': 'Agordoj',
        'youtube_url': 'YouTube URL',
        'youtube_url_placeholder': 'https://www.youtube.com/watch?v=...',
        'enter_valid_url': 'Enigu validan YouTube-videan aŭ ludlistan URL-on',
        'download_type': 'Elŝuta tipo',
        'video': 'Video',
        'audio': 'Aŭdio',
        'transcript': 'Transskribo',
        'clean_text': 'Pura tekstdosiero',
        'continue': 'Daŭrigi',
        'download': 'Elŝuti',
        'download_more': 'Elŝuti pli',
        
        # Batch
        'youtube_urls_multiline': 'YouTube URL-oj (unu por linio)',
        'enter_multiple_urls': 'Enigu plurajn YouTube URL-ojn, unu por linio',
        
        # Settings
        'download_directory_settings': 'Elŝuta dosierujo-agordoj',
        'open_current_folder': 'Malfermi nunan dosierujon',
        'use_system_downloads': 'Uzi sisteman Elŝutojn-dosierujon',
        'use_custom_directory': 'Uzi propran dosierujon',
        'browse': 'Foliumi',
        'save_settings': 'Konservi agordojn',
        'settings_saved': 'Agordoj konservitaj!',
        'download_preferences': 'Elŝutaj preferoj',
        'auto_open_downloads': 'Aŭtomate malfermi dosierujon post finado',
        'auto_open_description': 'Se ebligita, la elŝuta dosierujo aŭtomate malfermiĝos post finado',
        'about_directory_selection': 'Pri dosierujo-elekto',
        'directory_info': 'Vi povas elekti kie konservi viajn elŝutitajn dosierojn. Defaŭlte, dosieroj estas konservitaj en la sistema Elŝutoj-dosierujo.',
        'tip': 'Konsilo',
        'directory_tip': 'Post elŝuto, la dosierujo aŭtomate malfermiĝos en via dosier-esplorilo.',
        
        # Progress
        'download_progress': 'Elŝuta progreso',
        'batch_progress': 'Amasa elŝuta progreso',
        'initializing': 'Pravalorizado de elŝuto...',
        'processing': 'Prilaborado',
        'preparing': 'Preparado de elŝuto...',
        'download_details': 'Elŝutaj detaloj:',
        'type': 'Tipo',
        'format': 'Formato',
        'language': 'Lingvo',
        
        # Completion
        'download_complete': 'Elŝuto finita!',
        'success_message': 'Viaj dosieroj estis sukcese elŝutitaj.',
        'transcript_success': 'La transskribo estis konservita kiel pura tekstdosiero sen tempmarkoj aŭ formataj kodoj.',
        'downloaded_files': 'Elŝutitaj dosieroj:',
        'open_download_folder': 'Malfermi elŝutan dosierujon',
        'show_in_folder': 'Montri en dosierujo',
        'print_list': 'Presi liston',
        'did_you_know': 'Ĉu vi sciis?',
        'batch_tip': 'Vi povas elŝuti plurajn videojn samtempe! Simple algluu plurajn URL-ojn (unu por linio) en la Amasa Elŝuto-langeto.',
        
        # Format selection
        'select_video_format': 'Elekti video-formaton',
        'choose_quality': 'Elektu vian preferatan video-kvaliton kaj formaton:',
        'best_quality': 'Plej bona kvalito',
        'auto_best': 'Aŭtomate plej bona kvalito',
        'higher_resolution_tip': 'Pli altaj rezolucioj provizas pli bonan kvaliton sed pli grandajn dosierojn.',
        
        # Language selection
        'select_subtitle_language': 'Elekti subtekstan lingvon',
        'choose_language': 'Elektu la subtekstan lingvon por elŝuti:',
        'transcript_note': 'La transskribo estos elŝutita kiel pura tekstdosiero (.txt) sen tempmarkoj aŭ formataj kodoj.',
        'manual': 'Mana',
        'auto_generated': 'Aŭtomate generita',
        'subtitle_tip': 'Manaj subtekstoj kutime estas pli precizaj ol aŭtomate generitaj.',
        
        # How it works
        'how_it_works': 'Kiel ĝi funkcias',
        'paste_url': 'Alglui URL',
        'paste_url_desc': 'Enigu YouTube-videan aŭ ludlistan URL-on',
        'choose_options': 'Elekti opciojn',
        'choose_options_desc': 'Elektu formaton, kvaliton kaj lingvon',
        'download_desc': 'Akiru vian enhavon kun progres-spurado',
        
        # Features
        'what_you_can_download': 'Kion vi povas elŝuti',
        'videos': 'Videoj',
        'videos_desc': 'Elŝuti en diversaj rezolucioj de 360p ĝis 4K',
        'audio_desc': 'Eltiri aŭdion kiel altkvalitajn MP3-dosierojn (192kbps)',
        'transcripts': 'Transkriboj',
        'transcripts_desc': 'Puraj tekstdosieroj sen tempmarkoj aŭ formatado',
        
        # Footer
        'powered_by': 'Funkciigita per Flask kaj yt-dlp',
        'open_source': 'Malferma programaro',
        
        # About modal
        'about_title': 'Pri YouTube Elŝutilo',
        'about_desc': 'YouTube Elŝutilo estas potenca kaj uzant-amika retaplikaĵo por elŝuti enhavon de YouTube.',
        'features': 'Funkcioj:',
        'feature_1': 'Elŝuti videojn en diversaj formatoj kaj rezolucioj',
        'feature_2': 'Eltiri aŭdion kiel MP3-dosierojn',
        'feature_3': 'Elŝuti subtekstojn kaj transkribojn',
        'feature_4': 'Amasa elŝuto de pluraj URL-oj',
        'feature_5': 'Realtempaj progres-ĝisdatigoj',
        'feature_6': 'Propra elekto de elŝuta dosierujo',
        'technology_stack': 'Teknologia stako:',
        'tech_desc': 'Konstruita per Flask, yt-dlp kaj Socket.IO por realtempaj ĝisdatigoj.',
        'close': 'Fermi',
        'view_on_github': 'Vidi sur GitHub',
        
        # Errors
        'page_not_found': 'Paĝo ne trovita',
        'error_404': 'Ho ve! La paĝo kiun vi serĉas ne ekzistas.',
        'error_404_desc': 'Ĝi eble estis forigita, alinomita aŭ neniam ekzistis.',
        'go_home': 'Iri hejmen',
        'go_back': 'Reen',
        'server_error': 'Servila eraro',
        'error_500': 'Io misfunkciis ĉe nia flanko.',
        'error_500_desc': 'Ni pardonpetas pro la ĝeno. Bonvolu provi denove poste.',
        'try_again': 'Provi denove',
        'contact_support': 'Se ĉi tiu eraro persistas, bonvolu kontakti subtenon ĉe',
        
        # Form validation
        'please_enter_url': 'Bonvolu enigi YouTube URL.',
        'please_enter_valid_url': 'Bonvolu enigi validan URL.',
        'only_youtube_allowed': 'Nur YouTube URL-oj estas permesitaj.',
        'invalid_url_format': 'Nevalida YouTube URL-formato. Devas enhavi videon aŭ ludliston.',
        'please_enter_one_url': 'Bonvolu enigi almenaŭ unu YouTube URL.',
        'invalid_directory': 'Nevalida dosieruja vojo aŭ nesufiĉaj permesoj.',
        
        # Messages
        'no_subtitles': 'Neniuj subtekstoj disponeblas por ĉi tiu video.',
        'no_files_found': 'Neniuj elŝutitaj dosieroj trovitaj.',
        'file_not_found': 'Dosiero ne trovita.',
        'cleanup_complete': 'Purigado finita. Forigis',
        'files': 'dosierojn.',
        
        # Quick access
        'quick_access': 'Rapida aliro:',
        'downloads': 'Elŝutoj',
        'desktop': 'Labortablo',
        'documents': 'Dokumentoj',
        'videos_folder': 'Videoj',
        'music': 'Muziko',
        'external_drive': 'Ekstera disko',
    }
}

def get_translation(lang_code, key):
    """Get translation for a specific key in the given language."""
    if lang_code not in translations:
        lang_code = 'en'
    
    return translations.get(lang_code, {}).get(key, translations['en'].get(key, key))

def get_all_translations(lang_code):
    """Get all translations for a specific language."""
    if lang_code not in translations:
        lang_code = 'en'
    
    # Merge with English translations as fallback
    base_translations = translations['en'].copy()
    if lang_code != 'en':
        base_translations.update(translations[lang_code])
    
    return base_translations