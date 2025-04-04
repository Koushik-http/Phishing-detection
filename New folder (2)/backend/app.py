from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def is_phishing(url):
    # Implement your URL detection logic here
    if "https" not in url:
        return True
    return False

@app.route('/check-url', methods=['POST'])
def check_url():
    data = request.json
    url = data['url']
    
    if is_phishing(url):
        return jsonify({'message': 'This URL is suspected to be phishing! and it is not secured'})
    else:
        return jsonify({'message': 'This URL seems to be safe. Redirecting to the Link'})

if __name__ == '__main__':
    app.run(debug=True)
