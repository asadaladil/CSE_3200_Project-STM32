import tensorflow as tf
import numpy as np

MODEL_PATH="Trained_digit_model.h5"
try:
    model=tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model=None

def predict_custom_matrix(image_matrix):
    if model is None: 
        print("Model not loaded.")
        return

    print(f"\n--- Processing Custom 28x28 Matrix ---")
    
    input_data=np.array(image_matrix)

    if input_data.shape != (28, 28): #28/28 check
        print(f"Error: Matrix must be 28x28! Received:{input_data.shape}")
        return
    if np.max(input_data)==0:
        print("No digit Exists")
        return
    if np.max(input_data)>1.0:
        input_data=input_data.astype('float32')/255.0
    else:
        input_data=input_data.astype('float32')

    input_data = input_data.reshape(1, 28, 28, 1) #[Batch Size, Height, Width, Channels]

    predictions=model.predict(input_data)
    predicted_digit=np.argmax(predictions) # max value carrying index
    # print(predictions)
    confidence=np.max(predictions)*100

    print(f"Model's Predicted Digit: {predicted_digit}")
    print(f"Confidence:{confidence:.2f}%")
    return predicted_digit
