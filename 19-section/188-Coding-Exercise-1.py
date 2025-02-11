# 188
# Coding Exercise 1

# Target:
# Your task for this exercise is to add a new feature to the webcam Streamlit app
# we built in today's bonus example video.

# You need to add a feature to that program that allows users to upload an image from their computer files.
# Then, the app converts the uploaded image to grayscale and displays it.

# Hint: You can use uploaded_image = st.file_uploader("Upload Image") to create a "Browse File" component.
# The end product should be as shown in the screenshot down below.

# Solution:
# https://pythonhow.com/coding/d19c1/

# follows

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

# terminal command:
# streamlit run 188-Coding-Exercise-1.py

###################################3

import streamlit as st
from PIL import Image

# added feature
# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

# Add an expander, with button, to control more the camera when to start
with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")


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


# added feature
# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)
    # Convert the image to grayscale
    gray_uploaded_img = img.convert("L")
    # Display the grayscale image on the webpage
    st.image(gray_uploaded_img)