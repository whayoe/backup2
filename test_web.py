from flask import Flask
import os
import subprocess
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Test Server</h1>
    <button onclick="fetch('/run-backup').then(res => res.text()).then(html => alert(html))">Jalankan Backup</button>
    """

@app.route('/run-backup')
def run_backup():
    try:
        print("🚀 Menjalankan backup.py...")
        
        # Jalankan backup.py
        result = subprocess.run(
            [sys.executable, "backup.py"],
            cwd=r"F:\DOKUMEN\BACKUP",
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=30  # Timeout 30 detik
        )

        # Log output
        if result.stdout:
            print(f"STDOUT: {result.stdout}")
        if result.stderr:
            print(f"STDERR: {result.stderr}")

        if result.returncode == 0:
            return "<pre>✅ Backup berhasil!</pre>"
        else:
            return f"<pre>❌ Gagal: {result.stderr}</pre>"

    except subprocess.TimeoutExpired:
        print("⏰ ERROR: Backup timeout (melebihi 30 detik)")
        return "<pre>❌ Backup timeout! Proses terlalu lama.</pre>"

    except Exception as e:
        print(f"💥 ERROR: {str(e)}")
        return f"<pre>❌ Error: {str(e)}</pre>"

if __name__ == '__main__':
    app.run(port=5000)