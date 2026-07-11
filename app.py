import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# Load trained model
model = tf.keras.models.load_model("malaria_model.keras")

st.set_page_config(
    page_title="Malaria Detection using CNN",
    page_icon="🦟",
    layout="centered"
)

st.title("🩸 Malaria Detection from Blood Cell Images 🧬")
st.subheader("Deep Learning Based CNN Classifier")

uploaded_file = st.file_uploader(
    "Choose a Blood Cell Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Display uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert PIL image to OpenCV format (BGR)
    img_array = np.array(image)
    img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    # Same preprocessing as training
    img_array = cv2.resize(img_array, (50, 50))
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array, verbose=0)
    probability = float(prediction[0][0])

    if probability > 0.5:
        st.error("Prediction: Parasitized (Malaria Infected)")
        st.write(f"Confidence: {probability:.2%}")
    else:
        st.success("Prediction: Uninfected")
        st.write(f"Confidence: {(1 - probability):.2%}")
