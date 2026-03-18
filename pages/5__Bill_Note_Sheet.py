"""
Hindi Bill Note Sheet Generator - Complete Interactive App
Full features: M/s. auto-prefix, all fields, auto-calculations, floating balloons, Hindi notes
Fully integrated standalone HTML/CSS/JavaScript version
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
    st.info("🌸 **Complete Interactive App** | M/s. auto-prefix | All fields | Auto-calculations | Floating balloons | Hindi note generation")
    
    # Load local HTML file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    html_file_path = os.path.join(parent_dir, "ATTACHED_ASSETS", "COMPLETE_HINDI_BILL_NOTE_SHEET.html")
    
    try:
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_code = f.read()
        
        st.markdown("---")
        
        # Display the complete app
        components.html(html_code, height=1400, scrolling=True)
        
        st.markdown("---")
        st.success("✅ Complete Hindi Bill Note Sheet loaded successfully!")
        st.info("💡 **Features:** Bilingual labels | Live calculations | GST rounding to higher even | Auto-preview | PDF generation with 10mm margins")
        
    except FileNotFoundError:
        st.error(f"❌ Error: Could not find the HTML file at: {html_file_path}")
        st.info("Please ensure the file exists at the correct location.")
        st.code(f"""
Expected file location:
{html_file_path}

Current directory: {current_dir}
Parent directory: {parent_dir}
        """)
    except Exception as e:
        st.error(f"❌ Error loading the app: {str(e)}")
        st.code(f"Error details: {type(e).__name__}: {str(e)}")

if __name__ == "__main__":
    main()
