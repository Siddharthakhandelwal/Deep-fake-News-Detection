from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from predict import predict_news
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Ensure templates directory exists
os.makedirs('templates', exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_content():
    try:
        data = request.json
        if not data or 'text' not in data:
            return jsonify({
                'status': 'error',
                'message': 'No text provided for analysis'
            }), 400

        # Get prediction from the model
        result = predict_news(data['text'])
        
        return jsonify({
            'status': 'success',
            'prediction': result['prediction'],
            'confidence': result['confidence'],
            'text': result['text']
        })

    except Exception as e:
        logger.error(f"Error in analysis: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Service is running'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 