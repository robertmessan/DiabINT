from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/app')
def get_streamlit_data():
    result = subprocess.run(['streamlit', 'run', 'dapp.py', '--browser.serverAddress=0.0.0.0', '--server.port=8501'], capture_output=True, text=True)
    return jsonify(result.stdout)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)