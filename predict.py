import tensorflow as tf
from transformers import BertTokenizer, TFBertModel
import pandas as pd
import numpy as np
import logging
import os
from tensorflow.keras.layers import Input, Dense, Dropout, LayerNormalization, Lambda
from tensorflow.keras.models import Model

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_model():
    """Create the model architecture"""
    # BERT input layers
    input_ids = Input(shape=(100,), dtype=tf.int32, name='input_ids')
    attention_mask = Input(shape=(100,), dtype=tf.int32, name='attention_mask')
    
    # Load BERT model
    bert_model = TFBertModel.from_pretrained('bert-base-uncased')
    
    # Get BERT outputs
    bert_outputs = bert_model([input_ids, attention_mask])
    pooled_output = bert_outputs[1]  # Get the pooled output
    
    # Add classification layers
    x = Dense(768, activation='relu')(pooled_output)
    x = LayerNormalization()(x)
    x = Dropout(0.1)(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.1)(x)
    output = Dense(1, activation='sigmoid')(x)
    
    # Create model
    model = Model(inputs=[input_ids, attention_mask], outputs=output)
    
    # Compile model
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=2e-5),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    return model

try:
    # Load the BERT tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    logger.info("BERT tokenizer loaded successfully")

    # Create model
    model = create_model()
    logger.info("Model created successfully")

    # Check if model file exists
    if os.path.exists('Deepfake.h5'):
        try:
            # Try to load weights
            model.load_weights('Deepfake.h5', by_name=True, skip_mismatch=True)
            logger.info("Model weights loaded successfully")
        except Exception as e:
            logger.error(f"Error loading weights: {str(e)}")
            raise
    else:
        logger.error("Model file 'Deepfake.h5' not found")
        raise FileNotFoundError("Model file not found")

except Exception as e:
    logger.error(f"Initialization error: {str(e)}")
    raise

def preprocess_text(text, max_length=100):
    """Preprocess text for BERT model"""
    try:
        # Tokenize text
        tokens = tokenizer.encode_plus(
            text,
            max_length=max_length,
            padding='max_length',
            truncation=True,
            return_tensors='tf'
        )
        return tokens
    except Exception as e:
        logger.error(f"Error in text preprocessing: {str(e)}")
        raise

def predict_news(text):
    """Make prediction on new text"""
    try:
        # Preprocess text
        tokens = preprocess_text(text)
        
        # Get model prediction
        prediction = model.predict([tokens['input_ids'], tokens['attention_mask']], verbose=0)
        
        # Convert prediction to label
        label = 'Fake' if prediction[0][0] > 0.5 else 'fake'
        confidence = float(prediction[0][0] if label == 'Real' else 1 - prediction[0][0])
        
        return {
            'text': text,
            'prediction': label,
            'confidence': confidence
        }
    except Exception as e:
        logger.error(f"Error in prediction: {str(e)}")
        raise

if __name__ == '__main__':
    # Example usage
    try:
        test_text = "India prime minister Narendra modi died on 2nd jan"
        result = predict_news(test_text)
        print("\nAnalysis Results:")
        print("-" * 50)
        print(f"Text: {result['text']}")
        print(f"Prediction: {result['prediction']}")
        print(f"Confidence: {result['confidence']:.2%}")
        print("-" * 50)
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        raise 