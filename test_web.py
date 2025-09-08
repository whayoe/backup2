from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Test Server</h1>
    <button onclick="fetch('/run-backup')">Jalankan Backup</button>
    """

@app.route('/run-backup')
def run_backup():
    try:
        result = subprocess.run(
            ["python", "backup.py"],
            cwd=r"F:\DOKUMEN\BACKUP",
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        return f"<pre>STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}</pre>"
    except Exception as e:
        return f"<pre>Error: {str(e)}</pre>"

if __name__ == '__main__':
    app.run(port=5000)