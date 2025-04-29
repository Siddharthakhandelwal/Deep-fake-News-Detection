from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze_content():
    data = request.json
    # This is where you'll integrate your deepfake detection model later
    # For now, we'll return a mock response
    return jsonify({
        'status': 'success',
        'is_deepfake': False,
        'confidence': 0.0,
        'message': 'Analysis complete'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000) 