# This file is for the React <-> Python connection
# While the demo is going we want to share data every x seconds

from flask import Flask, jsonify
from flask_socketio import SocketIO
import base64

app = Flask(__name__)
socketio = SocketIO(app)
    
@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

@socketio.on('message')
def handle_message(data):
    print("message")