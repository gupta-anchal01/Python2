from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Anchal Kumari"
    username = os.getlogin()
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    server_time = ist_time.strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True).stdout

    page = f"""
    <html>
        <head>
            <title>HTop Info</title>
            <style>
                body {{ font-family: Arial, sans-serif; }}
                pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <h1>HTop Endpoint</h1>
            <p><strong>Name:</strong> {full_name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h2>Top Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
