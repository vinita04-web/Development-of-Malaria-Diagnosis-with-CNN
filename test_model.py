import numpy as np
import tensorflow as tf
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Load model
model = tf.keras.models.load_model("malaria_model.keras")

# Load saved test data
X_test = np.load("X_test.npy")
y_test = np.load("y_test.npy")

# Predict
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob > 0.5).astype(int).flatten()

# Metrics
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Manual Image Testing

import cv2
import numpy as np

print("\n========== MANUAL IMAGE TESTING ==========")

image_path = input("Enter image path: ")

img = cv2.imread(image_path)

if img is None:
    print("Invalid image path!")
else:
    img = cv2.resize(img, (50, 50))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        print("\nPrediction : Parasitized")
    else:
        print("\nPrediction : Uninfected")