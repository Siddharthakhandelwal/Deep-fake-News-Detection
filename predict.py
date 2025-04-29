import tensorflow as tf
from transformers import BertTokenizer, TFBertModel
import pandas as pd
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('Deepfake.h5')

# Load the BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def preprocess_text(text, max_length=100):
    """Preprocess text for BERT model"""
    # Tokenize text
    tokens = tokenizer.encode_plus(
        text,
        max_length=max_length,
        padding='max_length',
        truncation=True,
        return_tensors='tf'
    )
    return tokens

def predict_news(text):
    """Make prediction on new text"""
    # Preprocess text
    tokens = preprocess_text(text)
    
    # Get model prediction
    prediction = model.predict([tokens['input_ids'], tokens['attention_mask']])
    
    # Convert prediction to label
    label = 'Fake' if prediction[0][0] > 0.5 else 'Real'
    confidence = prediction[0][0] if label == 'Fake' else 1 - prediction[0][0]
    
    return {
        'text': text,
        'prediction': label,
        'confidence': float(confidence)
    }

if __name__ == '__main__':
    # Example usage
    test_text = "India prime minister Narendra modi died on 2nd jan"
    result = predict_news(test_text)
    print(f"Text: {result['text']}")
    print(f"Prediction: {result['prediction']}")
    print(f"Confidence: {result['confidence']:.2%}") 