"""
Hindi Bill Note Sheet Generator - EXACT COPY
From https://hindibillnote.netlify.app/
Complete original app embedded
"""

import streamlit as st
import streamlit.components.v1 as components
import os

# Page configuration
st.set_page_config(
    page_title="Hindi Bill Note Sheet Generator",
    page_icon="🌸",
    layout="wide"
)

# Get the absolute path to the HTML file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
html_file_path = os.path.join(parent_dir, "ATTACHED_ASSETS", "Hindi_Bill_Note_Sheet", "full-app-test.html")

# Read the EXACT original HTML file
try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # Display the EXACT original app
    components.html(html_code, height=1200, scrolling=True)
    
    # Info at bottom
    st.markdown("---")
    st.success("✅ Original app loaded successfully from: " + html_file_path)
    st.info("🌸 **Original App:** https://hindibillnote.netlify.app/ | This is the EXACT original app with ALL features")
    
except FileNotFoundError:
    st.error(f"❌ Error: Could not find the HTML file at: {html_file_path}")
    st.info("Please ensure the file exists at the correct location.")
    
    # Show what we're looking for
    st.code(f"""
Expected file location:
{html_file_path}

Current directory: {current_dir}
Parent directory: {parent_dir}
    """)
except Exception as e:
    st.error(f"❌ Error loading the app: {str(e)}")
    st.code(f"Error details: {type(e).__name__}: {str(e)}")
