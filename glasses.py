# Python program to control mouse based on head position # Import necessary modules
import numpy as np
import cv2
import tensorflow as tf
# from keras.models import load_model


# Load the model
# model = load_model('/Users/dev/Desktop/union_work/opencvlearning/converted_keras/keras_model.h5')
model = tf.keras.models.load_model('/Users/dev/Desktop/union_work/opencvlearning/converted_keras/keras_model.h5', compile=False)

# CAMERA can be 0 or 1 based on default camera of your computer.
cap = cv2.VideoCapture(0)

# Grab the labels from the labels.txt file. This will be used later.
labels = open('/Users/dev/Desktop/union_work/opencvlearning/converted_keras/labels.txt', 'r').readlines()

while True:
    # Grab the webcameras image.
    ret, image = cap.read()
    # Resize the raw image into (224-height,224-width) pixels.
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    # Show the image in a window
    # cv2.imshow('Image', frame)
    cv2.imshow('frame',image)
    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    # Normalize the image array
    image = (image / 127.5) - 1
    # Have the model predict what the current image is. Model.predict
    # returns an array of percentages. Example:[0.2,0.8] meaning its 20% sure
    # it is the first label and 80% sure its the second label.
    probabilities = model.predict(image)
    # Print what the highest value probabilitie label
    print(labels[np.argmax(probabilities)])
    # Listen to the keyboard for presses.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
