# This file is for the React <-> Python connection
# While the demo is going we want to share data every x seconds

from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
import base64

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "WebSocket Server is running!"
    
@socketio.on('connect', namespace='/connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

@socketio.on('message')
def handle_message(data):
    print("Received message:", data)
    
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)