import streamlit as st
import streamlit.components.v1 as components

# Set page configuration for wide studio layout
st.set_page_config(
    page_title="Intelligent Real Estate Video Generation using AI",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide default Streamlit header/footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem; 
        padding-bottom: 0rem; 
        padding-left: 0rem; 
        padding-right: 0rem;
        max-width: 100%;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load and render index.html
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    components.html(html_content, height=1250, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ `index.html` not found! Please make sure `index.html` is saved in the exact same directory as `app.py`.")