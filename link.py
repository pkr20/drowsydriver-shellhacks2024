from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def process_frame():
    process = subprocess.Popen(['python', 'eyechecker.py'])  # or just ['app.exe']

    # Your main script can continue running without waiting for the GUI to close
    print("The GUI application has been launched.")

if __name__ == '__main__':
    app.run(debug=True)

