import streamlit as st
import cv2
import numpy as np
from model import predict_image  # Replace with actual model function

st.title("DotNeuralNet - Braille Detection and Translation")

uploaded_file = st.file_uploader("Upload a Braille Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Prediction
    if st.button("Detect Braille"):
        st.write("Running prediction...")
        result = predict_image(image)  # You need to define or import this
        st.write("Detected Braille Dots:")
        st.json(result)

        # OPTIONAL: If you add Braille to English translation
        # from braille_translate import translate_braille
        # english_text = translate_braille(result)
        # st.write("Translated English Text:")
        # st.success(english_text)
