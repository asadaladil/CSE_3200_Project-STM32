import tensorflow as tf
import numpy as np
import random

# --- Load Model Once (Global) ---
MODEL_PATH = 'mnist_digit_model.h5'
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

def predict_custom_matrix(image_matrix):
    """
    Accepts a 28x28 numpy array (values 0-255 or 0.0-1.0)
    and prints the AI prediction.
    """
    if model is None: 
        print("Model not loaded.")
        return

    print(f"\n--- Processing Custom 28x28 Matrix ---")
    
    # 1. Ensure it is a numpy array
    input_data = np.array(image_matrix)

    # 2. Validate Shape
    if input_data.shape != (28, 28):
        print(f"❌ Error: Matrix must be 28x28! Received: {input_data.shape}")
        return

    # 3. Preprocess
    #    Normalize to 0.0-1.0 (if it's 0-255)
    if np.max(input_data) > 1.0:
        input_data = input_data.astype('float32') / 255.0
    else:
        input_data = input_data.astype('float32')

    #    Reshape to (1, 28, 28, 1) [Batch Size, Height, Width, Channels]
    input_data = input_data.reshape(1, 28, 28, 1)

    # 4. Predict
    predictions = model.predict(input_data)
    predicted_digit = np.argmax(predictions) # max value carrying index
    print(predictions)
    confidence = np.max(predictions) * 100

    print(f"🤖 AI Prediction: {predicted_digit}")
    print(f"📊 Confidence:    {confidence:.2f}%")
    return predicted_digit

# if __name__ == "__main__":
#     # --- DEMO: How to pass a 28x28 matrix ---
    
#     # 1. Get a real digit from MNIST to test (Verification)
#     (_, _), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    
#     # Pick a specific index (e.g., index 0 is usually a '7')
#     test_index = 0
#     real_matrix_28x28 = x_test[test_index] # This is a (28, 28) array
    
#     print(f"Testing with known digit: {y_test[test_index]}")
    
#     # 2. Pass the 28x28 matrix to the function
#     predict_custom_matrix(real_matrix_28x28)

#     # --- DEMO: Creating a blank/manual matrix ---
#     print("\nTesting with a manually created blank matrix:")
#     blank_matrix = np.zeros((28, 28)) # All black
#     predict_custom_matrix(blank_matrix)