import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image
import matplotlib.pyplot as plt

# Load the saved model
model = load_model('model/my_cnn_model.h5')

st.title('Age Detection with CNN')

# Upload and preprocess image
uploaded_image = st.file_uploader('Choose an image...', type=['jpg', 'png'])
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    resized_image = image.resize((32, 32))  # Resize the image to (32, 32)
    image_array = np.array(resized_image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    st.image(resized_image, caption='Uploaded and Resized Image.', use_column_width=True)

    # Make prediction
    prediction = model.predict(image_array)
    predicted_class = np.argmax(prediction)

    label = {0:"Middle", 1: "Old", 2: "Young"}

    st.write(f'Predicted Class: {label.get(predicted_class).upper()} Age')

    # Plot the predicted class probabilities
    plt.figure(figsize=(8, 5))
    plt.bar(range(3), prediction[0])
    plt.xlabel('Class')
    plt.ylabel('Probability')
    plt.title('Predicted Class Probabilities')
    plt.xticks(range(3), labels=['MIDDLE', 'OLD', 'YOUNG'], rotation=45)
    st.pyplot(plt)
