# 187
# Bonus Example


# Target:
# create a web app, the user can start the computer webcam
# and they can capture an image, a photo from the camera
# and they can convert that photo into grayscale.

# how to run, command from terminal:
# streamlit run 187-Bonus-Example.py

# use the library pillow (PIL), already installed from streamlit,
# which is a Python Imaging Library

###################################3

import streamlit as st
from PIL import Image

# Add an expander, with button, to control more the camera when to start
with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")
    # print(camera_image)

# Error in the beginning
# AttributeError: 'NoneType' object has no attribute 'read'
# so, add the following condition if only the camera_image is not None, i.e. created:
if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)