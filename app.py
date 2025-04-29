from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        'status': 'success',
        'message': 'DeepFake News Detector API is running',
        'endpoints': {
            '/analyze': 'POST - Analyze content for deepfake detection'
        }
    })

@app.route('/analyze', methods=['POST'])
def analyze_content():
    data = request.json
    return jsonify({
        'status': 'success',
        'is_deepfake': False,
        'confidence': 0.0,
        'message': 'Analysis complete'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000) 