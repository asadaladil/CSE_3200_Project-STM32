import tensorflow as tf
from keras import layers, models
import numpy as np

def train_model(x,y):
    
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data() # 60000 train image, 10000 test image
    
    x_train=list(x_train)+list(x_test)+x
    y_train=list(y_train)+list(y_test)+y
    
    x_train=np.array(x_train)
    y_train=np.array(y_train)
    
    # 2. Preprocessing
    x_train=x_train.astype('float32') / 255.0 # normalizing

    # Reshape images to (28, 28, 1) as CNN expect 3D data
    x_train=np.expand_dims(x_train,3)
    # x_test=np.expand_dims(x_test, -1)

    print(f"Training data shape: {x_train.shape}")

    # 3. CNN Model
    model=models.Sequential([
        # Layer1: Extracts features like edges,curves
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)), # Reduces size to make computation faster

        # Layer2
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),

        # Layer3
        layers.Conv2D(64, (3, 3), activation='relu'),

        # 3D to 1D for the final classification layers
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        
        # Output Layer: 10 neurons for digits 0-9
        layers.Dense(10, activation='softmax') 
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.summary()

    print("\nStarting training... (This might take a minute)")
    model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

    # 6. Save the Model
    model_filename = "mnist_digit_model.h5"
    model.save(model_filename)
    print(f"\n✅ Model saved successfully as '{model_filename}'")
    print(f"now run your interface script!")

# train_model([],[])