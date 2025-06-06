"""Socket.IO manager for real-time communication with clients."""

from flask_socketio import SocketIO, emit, join_room, leave_room
from typing import Dict, Any


class SocketManager:
    """Manager for WebSocket connections via Socket.IO."""
    
    def __init__(self, app=None):
        """Initialize SocketIO with optional Flask app."""
        self.socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')
        
        # Register event handlers if app is provided
        if app:
            self.register_handlers()
    
    def init_app(self, app):
        """Initialize with Flask app (alternative constructor)."""
        self.socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')
        self.register_handlers()
        return self.socketio
    
    def register_handlers(self):
        """Register Socket.IO event handlers."""
        
        @self.socketio.on('connect')
        def handle_connect():
            """Handle client connection."""
            pass  # No action needed, connection is established automatically
        
        @self.socketio.on('disconnect')
        def handle_disconnect():
            """Handle client disconnection."""
            pass  # No action needed, cleanup is handled by Socket.IO
        
        @self.socketio.on('join')
        def handle_join(data):
            """Handle client joining a room for download updates."""
            room = data.get('room')
            if room:
                join_room(room)
                emit('status', {'msg': f'Joined room: {room}'}, room=room)
        
        @self.socketio.on('leave')
        def handle_leave(data):
            """Handle client leaving a room."""
            room = data.get('room')
            if room:
                leave_room(room)
                emit('status', {'msg': f'Left room: {room}'})
    
    def emit_progress(self, progress_data: Dict[str, Any], room: str = None):
        """Emit download progress update to clients."""
        self.socketio.emit('download_progress', progress_data, room=room)
    
    def emit_error(self, error_data: Dict[str, Any], room: str = None):
        """Emit error message to clients."""
        self.socketio.emit('download_error', error_data, room=room)
    
    def emit_completion(self, completion_data: Dict[str, Any], room: str = None):
        """Emit download completion notification to clients."""
        self.socketio.emit('download_complete', completion_data, room=room)
    
    def emit_batch_progress(self, batch_data: Dict[str, Any], room: str = None):
        """Emit batch download progress update to clients."""
        self.socketio.emit('batch_progress', batch_data, room=room)