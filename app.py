from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from predict import predict_news
import os

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
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 