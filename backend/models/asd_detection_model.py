import tensorflow as tf
import numpy as np

# Create a simple dummy model
def create_dummy_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(224, 224, 3)),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', 
                  loss='binary_crossentropy', 
                  metrics=['accuracy'])
    
    # Generate dummy data
    x_dummy = np.random.random((100, 224, 224, 3))
    y_dummy = np.random.randint(2, size=(100, 1))
    
    # Fit the model with dummy data
    model.fit(x_dummy, y_dummy, epochs=1, verbose=0)
    
    # Save the model
    model.save('model.h5')
    print("Dummy model created and saved.")

# Run the model creation
create_dummy_model()