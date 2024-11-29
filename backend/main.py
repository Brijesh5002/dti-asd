from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)
CORS(app)

# Load pre-trained ASD detection model
# Note: You'll need to replace this with an actual trained model
try:
    model = tf.keras.models.load_model('../ml_models/model.h5')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/detect', methods=['POST'])
def detect_asd():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    # Read image
    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    
    # Preprocess image
    processed_img = preprocess_image(img)
    
    # Make prediction
    prediction = model.predict(np.expand_dims(processed_img, axis=0))
    
    # Interpret results
    result = {
        'asd_probability': float(prediction[0][0]),
        'is_asd': bool(prediction[0][0] > 0.5)
    }
    
    return jsonify(result)

def preprocess_image(img):
    # Resize image to model's expected input size
    img_resized = cv2.resize(img, (224, 224))
    
    # Normalize pixel values
    img_normalized = img_resized / 255.0
    
    return img_normalized

if __name__ == '__main__':
    app.run(debug=True, port=5000)