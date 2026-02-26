import streamlit as st
import streamlit.components.v1 as components
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb

# Page configuration
st.set_page_config(
    page_title="Main BAT Info | PWD Tools Hub",
    page_icon="🖥️",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Main BAT Info")

def main():
    st.markdown("""
    <style>
    .code-block {
        background-color: #f4f4f4;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 15px;
        font-family: monospace;
        white-space: pre-wrap;
        overflow-x: auto;
        margin: 10px 0;
    }
    
    .info-box {
        background-color: #e8f4f8;
        border-left: 5px solid #2196F3;
        padding: 15px;
        border-radius: 5px;
        margin: 20px 0;
    }
    
    .warning-box {
        background-color: #fff8e1;
        border-left: 5px solid #ff9800;
        padding: 15px;
        border-radius: 5px;
        margin: 20px 0;
    }
    
    .step-box {
        background-color: #f1f8e9;
        border-left: 5px solid #4CAF50;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("## 🖥️ Main BAT Program Information")
    
    st.markdown("""
    <div class="info-box">
    <h3>Overview</h3>
    <p>The <code>main.bat</code> file is a Windows batch script that serves as the primary launcher for the PWD Tools Hub application. 
    It provides a convenient way to start the Streamlit application without needing to remember complex command-line instructions.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📄 Program Contents")
    st.markdown("""
    <div class="code-block">@echo off
title PWD Tools Hub - Main Application
echo ========================================
echo   PWD Tools Hub - Main Application
echo ========================================
echo.
echo Starting the PWD Tools Hub application...
echo.
echo The app will be available at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python and make sure it's accessible from the command line
    echo.
    pause
    exit /b 1
)

echo Starting PWD Tools Hub...
echo.
python -m streamlit run app.py

pause</div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔍 Program Breakdown")
    
    st.markdown("""
    <div class="step-box">
    <h4>1. Initialization</h4>
    <ul>
        <li><code>@echo off</code> - Prevents commands from being displayed in the command prompt</li>
        <li><code>title PWD Tools Hub - Main Application</code> - Sets the window title</li>
        <li>Echo commands - Display welcome messages and instructions</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
    <h4>2. Python Check</h4>
    <ul>
        <li><code>python --version >nul 2>&1</code> - Checks if Python is installed</li>
        <li>If Python is not found, displays an error message and exits</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
    <h4>3. Application Launch</h4>
    <ul>
        <li><code>python -m streamlit run app.py</code> - Starts the Streamlit application</li>
        <li>The application will be accessible at <code>http://localhost:8501</code></li>
        <li><code>pause</code> - Keeps the window open after the application stops</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ▶️ How to Use")
    
    st.markdown("""
    <div class="step-box">
    <h4>Running the Program</h4>
    <ol>
        <li>Double-click on <code>main.bat</code> in the file explorer</li>
        <li>Or right-click and select "Run as administrator" if needed</li>
        <li>The command prompt window will open and display startup information</li>
        <li>Your default web browser will automatically open to <code>http://localhost:8501</code></li>
        <li>Press <code>Ctrl+C</code> in the command prompt window to stop the application</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-box">
    <h4>⚠️ Important Notes</h4>
    <ul>
        <li>Python must be installed on your system and added to the PATH environment variable</li>
        <li>Required Python packages must be installed (see requirements.txt)</li>
        <li>If you encounter errors, try running the batch file as administrator</li>
        <li>Firewall settings may need to be adjusted to allow access to port 8501</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🛠️ Alternative Execution Methods")
    
    st.markdown("""
    <div class="step-box">
    <h4>Command Line Execution</h4>
    <p>You can also run the application directly from the command line:</p>
    <div class="code-block">cd c:\\Users\\Rajkumar\\PWD-Tools-Genspark2
python -m streamlit run app.py</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
    <h4>Using the Direct Run Script</h4>
    <p>Alternatively, you can use the provided <code>main.bat</code> script:</p>
    <div class="code-block">main.bat</div>
    </div>
    """, unsafe_allow_html=True)

# Navigation function
def create_back_button():
    """Create a back to home button"""
    st.markdown('<div style="text-align: center; margin: 20px 0;">', unsafe_allow_html=True)
    if st.button("🏠 Back to Home", key="back_home", type="secondary"):
        st.switch_page("app.py")
    st.markdown('</div>', unsafe_allow_html=True)

# Create navigation
create_back_button()

# Run main function
if __name__ == "__main__":
    main()