import streamlit as st
import os

def main():
    """Main function for APG Calculator"""
    st.set_page_config(
        page_title="APG Calculator",
        page_icon="🧮",
        layout="wide"
    )

    st.title("🧮 APG Calculator")
    st.markdown("**50% of savings beyond -15% below G-Schedule**")

    # Path to the HTML file
    html_file_path = os.path.join("static", "html", "apg_calculator.html")

    # Check if file exists
    if os.path.exists(html_file_path):
        # Read and display the HTML file
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Display the HTML in an iframe for better isolation
        st.components.v1.html(html_content, height=800, scrolling=True)
    else:
        st.error(f"APG Calculator HTML file not found at: {html_file_path}")
        st.info("Please ensure the file exists in the static/html directory.")

if __name__ == "__main__":
    main()
