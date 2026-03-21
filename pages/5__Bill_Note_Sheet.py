"""
Hindi Bill Note Sheet Generator - Complete Interactive App
Full features: Bilingual labels, auto-calculations, GST rounding, automated testing, PDF generation
Complete standalone HTML application with all features built-in
"""

import streamlit as st
import streamlit.components.v1 as components
import os

# Page configuration
st.set_page_config(
    page_title="Hindi Bill Note Sheet Generator",
    page_icon="📝",
    layout="wide"
)

def main():
    st.markdown("## 📝 Hindi Bill Note Sheet Generator")
    st.info("🌸 **Complete Interactive App** | Bilingual labels | Auto-calculations | GST rounding to higher even | Automated testing | PDF generation with 10mm margins")
    
    # Load the complete standalone HTML app
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    html_file_path = os.path.join(parent_dir, "hindi_bill_note_sheet_app", "COMPLETE_HINDI_BILL_NOTE_SHEET.html")
    
    try:
        # Read the complete standalone HTML file
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        st.markdown("---")
        
        # Display the complete app
        components.html(html_content, height=1600, scrolling=True)
        
        st.markdown("---")
        st.success("✅ Complete Hindi Bill Note Sheet app loaded successfully!")
        
        # Feature list
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("✅ **Bilingual Labels**\nHindi/English for all fields")
        with col2:
            st.info("✅ **Live Calculations**\nSD 10% | IT 2% | GST 2% | LC 1%")
        with col3:
            st.info("✅ **GST Rounding**\nRounds to nearest higher even number")
        
        col4, col5, col6 = st.columns(3)
        with col4:
            st.info("✅ **Live Preview**\nInstant updates as you type")
        with col5:
            st.info("✅ **PDF Generation**\nA4 with 10mm margins")
        with col6:
            st.info("✅ **Automated Testing**\nBuilt-in test suite with sample data")
        
    except FileNotFoundError as e:
        st.error(f"❌ Error: Could not find the HTML file")
        st.info(f"Missing file: {html_file_path}")
        st.code(f"""
Expected file:
- {html_file_path}

Current directory: {current_dir}
Parent directory: {parent_dir}
        """)
    except Exception as e:
        st.error(f"❌ Error loading the app: {str(e)}")
        st.code(f"Error details: {type(e).__name__}: {str(e)}")

if __name__ == "__main__":
    main()
