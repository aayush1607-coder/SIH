import streamlit as st
import pickle
from PIL import Image
import numpy as np
import io

# Load the trained model
with open('cnn_disease.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to preprocess the image and make predictions
def preprocess_image(image):
    # Convert the image to a format that your model expects
    image = image.resize((224, 224))  # Resize to the expected input size
    image_array = np.array(image)
    image_array = image_array / 255.0  # Normalize if required
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    return image_array

def predict_disease(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    return prediction

# Streamlit interface
st.title("Crop Disease Prediction")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    if st.button('Predict'):
        prediction = predict_disease(image)
        st.write(f"Prediction: {prediction}")
