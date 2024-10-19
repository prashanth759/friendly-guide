from flask import Flask
import subprocess
import os
from datetime import datetime
import pytz

app = Flask(__name__)
@app.route('/')
def home():
    return "Flask is running!"

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME")

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get top output
    top_output = subprocess.check_output("top -b -n 1 | head -n 10", shell=True).decode('utf-8')

    # HTML format
    return f"""
    <html>
        <body>
            <h1>System Information</h1>
            <p>Name - N SRI SAI PRASHANTH REDDY</p>
            <p>Username - {username}</p>
            <p>Server Time in IST - {server_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
