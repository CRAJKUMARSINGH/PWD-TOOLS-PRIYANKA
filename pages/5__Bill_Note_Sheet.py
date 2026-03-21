"""
Hindi Bill Note Sheet Generator - COMPLETE STANDALONE APPLICATION
Full Navratri/Diwali Theme | Floating Diyas | Automated Testing | All Features
NO COMPROMISES - Complete, Beautiful, Independent Application
"""

import streamlit as st
import streamlit.components.v1 as components
import os

# Page configuration
st.set_page_config(
    page_title="🪔 Hindi Bill Note Sheet Generator",
    page_icon="🪔",
    layout="wide"
)

def main():
    st.markdown("## 🪔 Hindi Bill Note Sheet Generator - Complete Application")
    st.success("🌸 **COMPLETE STANDALONE APP** | Navratri Theme | Floating Diyas & Flowers | Bilingual Interface | Live Calculations | Automated Testing | PDF Generation | Sample Data Loader")
    
    # Load the COMPLETE standalone HTML app
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    html_file_path = os.path.join(parent_dir, "hindi_bill_note_sheet_app", "COMPLETE_HINDI_BILL_NOTE_SHEET.html")
    
    try:
        # Read the complete standalone HTML file
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        st.markdown("---")
        
        # Display the complete app with full height
        components.html(html_content, height=1800, scrolling=True)
        
        st.markdown("---")
        st.success("✅ Complete Hindi Bill Note Sheet application loaded successfully!")
        
        # Feature showcase in 4 columns
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.info("🪔 **Navratri Theme**\nFloating diyas & festive decorations")
        with col2:
            st.info("🌸 **Bilingual Interface**\nHindi/English labels throughout")
        with col3:
            st.info("📊 **Live Calculations**\nSD, IT, GST, LC auto-calculated")
        with col4:
            st.info("🖨️ **PDF Generation**\nProfessional A4 output with 10mm margins")
        
        col5, col6, col7, col8 = st.columns(4)
        with col5:
            st.info("👁️ **Live Preview**\nSee changes instantly")
        with col6:
            st.info("✨ **GST Rounding**\nHigher even number logic")
        with col7:
            st.info("🧪 **Automated Testing**\nBuilt-in test suite")
        with col8:
            st.info("📝 **Sample Data**\nOne-click test data loader")
        
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
