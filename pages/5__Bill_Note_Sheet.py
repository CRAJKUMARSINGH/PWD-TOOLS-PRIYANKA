"""
Hindi Bill Note Sheet Generator - Complete Interactive React App
Full features: M/s. auto-prefix, all fields, auto-calculations, floating balloons, Hindi notes
Fully integrated React application with all assets
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
    st.info("🌸 **Complete Interactive React App** | M/s. auto-prefix | All fields | Auto-calculations | Floating balloons | Hindi note generation")
    
    # Load the complete React app
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    html_file_path = os.path.join(parent_dir, "hindi_bill_note_sheet_app", "index.html")
    assets_dir = os.path.join(parent_dir, "hindi_bill_note_sheet_app")
    
    try:
        # Read the main HTML file
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Read the CSS file
        css_file = os.path.join(assets_dir, "assets", "index-Co3DCvaa.css")
        with open(css_file, "r", encoding="utf-8") as f:
            css_content = f.read()
        
        # Read the JS file
        js_file = os.path.join(assets_dir, "assets", "index-DVx-snOk.js")
        with open(js_file, "r", encoding="utf-8") as f:
            js_content = f.read()
        
        # Create a complete standalone HTML with embedded CSS and JS
        complete_html = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1" />
    <title>Hindi Bill Note Sheet</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
      @media print {{
        .no-print {{ display: none !important; }}
        .print-area {{ display: block !important; }}
      }}
      {css_content}
    </style>
  </head>
  <body>
    <div id="root"></div>
    <script type="module">
      {js_content}
    </script>
  </body>
</html>
"""
        
        st.markdown("---")
        
        # Display the complete React app
        components.html(complete_html, height=1400, scrolling=True)
        
        st.markdown("---")
        st.success("✅ Complete Hindi Bill Note Sheet React app loaded successfully!")
        st.info("💡 **Features:** Bilingual labels | Live calculations | GST rounding to higher even | Auto-preview | PDF generation | React-powered UI")
        
    except FileNotFoundError as e:
        st.error(f"❌ Error: Could not find required files")
        st.info(f"Missing file: {str(e)}")
        st.code(f"""
Expected files:
- {html_file_path}
- {css_file}
- {js_file}

Current directory: {current_dir}
Parent directory: {parent_dir}
Assets directory: {assets_dir}
        """)
    except Exception as e:
        st.error(f"❌ Error loading the app: {str(e)}")
        st.code(f"Error details: {type(e).__name__}: {str(e)}")

if __name__ == "__main__":
    main()
