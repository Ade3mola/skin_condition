import streamlit as st
from PIL import Image
import numpy as np


st.title(body = 'Skin Condition AI')
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)
    st.image(img)