import tensorflow as tf
from keras import layers, models
import numpy as np

layers=tf.keras.layers
models=tf.keras.models
ImageDataGenerator=tf.keras.preprocessing.image.ImageDataGenerator

def train_model():
    #1. Dataset Loading:
    (X, Y),(x, y)=tf.keras.datasets.mnist.load_data() # 60000 train image, 10000 test image
    
    x_train=list(X)+list(x)
    y_train=list(Y)+list(y)
    
    for digit in range(10):
        with open(f"./Digit_Image_Array/Digit{digit}.txt",mode="r") as file:
            a=[]
            file=file.readlines()
            for i in file:
                if len(i.split(' '))==1: #for taking y values
                    x_train.append(a)
                    y_train.append(int(i))
                    a=[]
                    continue
                temp=[]
                for j in i.split(' '):
                    try:
                        temp.append(int(j))
                    except:
                        continue
                a.append(temp)
    
    x_train=np.array(x_train)
    y_train=np.array(y_train)
    
    # 2. Preprocessing
    x_train=x_train.astype('float32') / 255.0 # normalizing
    
    # Shuffle the dataset
    indices=np.arange(len(x_train))
    np.random.shuffle(indices)
    x_train=x_train[indices]
    y_train=y_train[indices]
    
    
    # Reshape images to (28, 28, 1) as CNN expect 3D data
    x_train=np.expand_dims(x_train,-1)

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
    
    # 4. Augmentation
    datagen=ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.15,
        height_shift_range=0.15,
        zoom_range=0.15,
        validation_split=0.2
    )
    datagen.fit(x_train)
    
    # 5. CNN Model Fit
    print("\nStarting training... (This might take a minute)")
    model.fit(
            datagen.flow(x_train, y_train, batch_size=64),
            epochs=15,
        )

    # 6. Save the Model
    model_filename="Trained_digit_model.h5"
    model.save(model_filename)
    print(f"\n✅ Model saved successfully as '{model_filename}'")
    print(f"now run your interface script!")

train_model()


