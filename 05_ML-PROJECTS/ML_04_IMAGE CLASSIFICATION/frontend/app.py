import streamlit as st
import utils
import numpy as np
import cv2
import base64
from PIL import Image

# Load model and class dictionaries
utils.load_saved_artifacts()

def image_to_base64(img):
    _, buffer = cv2.imencode('.jpg', img)
    b64_str = base64.b64encode(buffer).decode()
    return "data:image/jpeg;base64," + b64_str

st.set_page_config(page_title="Image Classifier", layout="centered")
st.title("Celebrity Image Classifier")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    st.image(opencv_image, channels="BGR", caption="Uploaded Image")

    b64_image = image_to_base64(opencv_image)

    with st.spinner("Classifying..."):
        result = utils.classify_image(b64_image)

    if result:
        for i, res in enumerate(result):
            st.subheader(f"DETECTED AS")
            st.write(f"Predicted Class: **{res['class']}**")
            st.write("Class Probabilities:")
            for cls, prob in zip(res['class_dictionary'].keys(), res['class_probability']):
                st.write(f"  - {cls}: {prob:.2f}%")
    else:
        st.warning("No face with two eyes detected. Try another image.")
