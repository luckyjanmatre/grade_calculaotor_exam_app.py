import streamlit as st

# Set page configuration with a custom icon and layout
st.set_page_config(page_title="Grade Calculator", page_icon="💻", layout="centered")

# Inject custom CSS for a hacker-style theme
st.markdown(
    """
    <style>
    body {
        background-color: black;
        font-family: 'Courier New', monospace;
    }
    .stApp {
        background-color: black;
    }
    h1 {
        color: #00FF00;
        text-align: center;
        font-size: 30px;
        font-family: 'Courier New', monospace;
        text-shadow: 0px 0px 5px #00FF00;
    }
    .stNumberInput input {
        background-color: #333333;
        color: #00FF00;
        font-family: 'Courier New', monospace;
        border: 2px solid #00FF00;
    }
    .stButton button {
        background-color: black;
        color: #00FF00;
