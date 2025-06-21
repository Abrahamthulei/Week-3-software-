app.py

import streamlit as st import numpy as np import tensorflow as tf from PIL import Image

Load trained model (assuming it's saved as 'mnist_model.h5')

@st.cache_resource def load_model(): model = tf.keras.models.load_model("mnist_model.h5") return model

model = load_model()

Streamlit UI

st.set_page_config(page_title="MNIST Digit Classifier", layout="centered") st.title("🧠 MNIST Digit Classifier") st.write("Upload a black & white image (28x28 px) of a digit (0-9)")

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file: img = Image.open(uploaded_file).convert('L').resize((28, 28)) img_array = np.array(img)

st.image(img, caption="Uploaded Digit", width=150)

# Preprocess
img_array = img_array / 255.0  # Normalize
img_array = img_array.reshape(1, 28, 28, 1)

# Predict
prediction = model.predict(img_array)
predicted_class = np.argmax(prediction)

st.success(f"✅ Predicted Digit: {predicted_class}")
st.bar_chart(prediction[0])

st.write("### 🔍 Confidence Scores")
for i, score in enumerate(prediction[0]):
    st.write(f"{i}: {score:.4f}")

st.caption("Built with Streamlit and TensorFlow")

