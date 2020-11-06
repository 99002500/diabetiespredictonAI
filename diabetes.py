# This program detects if someone has diabeties or not

# import the libraries

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import streamlit as st

# Create a title and a subtitle
st.write("""
# Diabetes detection
Detect if someone has diabetes using machine learning and python
""")
# Open and display an image
image = Image.open("diabetes.png")
