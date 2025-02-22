from flask import Flask
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get your full name and system username
    full_name = "Somnath Choudhury"  # Replace with your full name
    username = subprocess.getoutput('whoami')

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get top output
    top_output = subprocess.getoutput('top -b -n 1 | head -n 20')

    # Format the response
    response = (
        f"Name - {full_name}<br>"
        f"Username - {username}<br>"
        f"Server Time in IST - {server_time}<br>"
        f"Top Output:<br><pre>{top_output}</pre>"
    )
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)