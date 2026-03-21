"""
PWD Tools Suite - Main Application
"""

import streamlit as st
from pathlib import Path
import sys
import importlib.util

# Add tools directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Page configuration
st.set_page_config(
    page_title="PWD Tools Suite",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'selected_tool' not in st.session_state:
    st.session_state.selected_tool = None
if 'first_visit' not in st.session_state:
    st.session_state.first_visit = True

# Tool definitions
TOOLS = {
    "🏗️ Bill Generator": {
        "file": "tools/bill_generator_enterprise.py",
        "description": "Complete bill package with all documents and PDFs",
        "icon": "🏗️"
    },
    "📊 Excel to EMD": {
        "file": "tools/excel_to_emd_web.py",
        "description": "Generate EMD receipts from Excel",
        "icon": "📊"
    },
    "💸 EMD Refund": {
        "file": "tools/emd_refund.py",
        "description": "Calculate EMD refunds with penalties",
        "icon": "💸"
    },
    "🔒 Security Refund": {
        "file": "tools/security_refund.py",
        "description": "Security deposit refund calculator",
        "icon": "🔒"
    },
    "📝 Bill Note Sheet": {
        "file": "tools/bill_note_sheet.py",
        "description": "Complete Hindi bill note sheet with automated testing & PDF generation",
        "icon": "📝"
    },
    "➖ Deductions Table": {
        "file": "tools/deductions_table.py",
        "description": "Calculate TDS and security deductions",
        "icon": "➖"
    },
    "📈 Financial Progress": {
        "file": "tools/financial_progress.py",
        "description": "Track financial progress of projects",
        "icon": "📈"
    },
    "🧮 APG Calculator": {
        "file": "tools/apg_calculator.py",
        "description": "Calculate APG values",
        "icon": "🧮"
    },
    "⏱️ Delay Calculator": {
        "file": "tools/delay_calculator.py",
        "description": "Calculate project delays and extensions",
        "icon": "⏱️"
    },
    "⚖️ Stamp Duty": {
        "file": "tools/stamp_duty.py",
        "description": "Calculate stamp duty for documents",
        "icon": "⚖️"
    },
    "🧾 Hand Receipt": {
        "file": "tools/hand_receipt.py",
        "description": "Generate RPWA 28 compliant hand receipts",
        "icon": "🧾"
    },
    "📖 User Manual": {
        "file": "tools/user_manual.py",
        "description": "Bilingual user manual",
        "icon": "📖"
    },
    "ℹ️ Main Info": {
        "file": "tools/main_bat_info.py",
        "description": "Information about launcher program",
        "icon": "ℹ️"
    }
}

# Custom CSS with International 2025 Design Trends
st.markdown("""
<style>
    /* Dark/Light mode variables */
    :root {
        --bg-primary: #fce4ec;
        --bg-secondary: #f8bbd0;
        --text-primary: #880e4f;
        --accent-primary: #e91e63;
        --accent-secondary: #c2185b;
        --glass-bg: rgba(255, 255, 255, 0.15);
        --glass-border: rgba(255, 255, 255, 0.2);
        --shadow-glass: 0 8px 32px rgba(233, 30, 99, 0.2);
    }
    
    [data-theme="dark"] {
        --bg-primary: #0a0a0a;
        --bg-secondary: #1a1a1a;
        --text-primary: #ffffff;
        --accent-primary: #ff0080;
        --accent-secondary: #ff4081;
        --glass-bg: rgba(255, 255, 255, 0.1);
        --glass-border: rgba(255, 255, 255, 0.15);
        --shadow-glass: 0 8px 32px rgba(255, 0, 128, 0.3);
    }
    
    /* Main background with dynamic theming */
    .main {
        background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 50%, var(--bg-primary) 100%);
        transition: all 0.3s ease;
    }
    
    /* Hide Streamlit branding and clean up top area */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    header {visibility: hidden;}
    
    /* Clean up top toolbar area */
    [data-testid="stToolbar"] {
        display: none;
    }
    
    /* Hide the default Streamlit header */
    [data-testid="stHeader"] {
        background: transparent;
        display: none;
    }
    
    /* Remove top padding to eliminate ugly space */
    .block-container {
        padding-top: 2rem;
    }
    
    /* Dark Mode Toggle Button */
    .theme-toggle {
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: 50px;
        padding: 12px 20px;
        color: var(--text-primary);
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: var(--shadow-glass);
        font-size: 1.2rem;
    }
    
    .theme-toggle:hover {
        transform: scale(1.1);
        box-shadow: 0 12px 40px rgba(255, 0, 128, 0.4);
    }
    
    /* Glassmorphism Header with shimmer animation */
    .main-header {
        background: var(--glass-bg);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border: 1px solid var(--glass-border);
        padding: 2.5rem;
        border-radius: 20px;
        color: var(--text-primary);
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: var(--shadow-glass);
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(90deg, transparent, rgba(255, 0, 128, 0.2), transparent);
        animation: shimmer 4s linear infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) rotate(45deg); }
        100% { transform: translateX(100%) rotate(45deg); }
    }
    
    .main-header h1 {
        position: relative;
        z-index: 1;
        text-shadow: 2px 2px 8px rgba(233, 30, 99, 0.3);
    }
    
    .main-header p {
        position: relative;
        z-index: 1;
    }
    
    /* Glassmorphism Sidebar */
    [data-testid="stSidebar"] {
        background: var(--glass-bg);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border-right: 1px solid var(--glass-border);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: transparent;
    }
    
    /* Glassmorphism Tool Cards with Bento Grid Style */
    .tool-card {
        background: var(--glass-bg);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 30px;
        margin: 15px 0;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: var(--shadow-glass);
        color: var(--text-primary);
        position: relative;
        overflow: hidden;
    }
    
    .tool-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 0, 128, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .tool-card:hover::before {
        left: 100%;
    }
    
    .tool-card:hover {
        transform: translateY(-12px) scale(1.02);
        box-shadow: 0 20px 60px rgba(255, 0, 128, 0.4);
        border-color: var(--accent-primary);
    }
    
    /* Neon glow effect on hover */
    .tool-card:hover {
        box-shadow: 
            0 0 20px rgba(255, 0, 128, 0.3),
            0 0 40px rgba(255, 0, 128, 0.2),
            0 20px 60px rgba(255, 0, 128, 0.4);
    }
    
    /* Different glassmorphism variants for each tool - Bento style */
    .tool-card-0 { 
        background: linear-gradient(135deg, rgba(233, 30, 99, 0.2) 0%, rgba(194, 24, 91, 0.15) 100%);
        border-left: 3px solid #e91e63;
    }
    .tool-card-1 { 
        background: linear-gradient(135deg, rgba(240, 147, 251, 0.2) 0%, rgba(245, 87, 108, 0.15) 100%);
        border-left: 3px solid #f093fb;
    }
    .tool-card-2 { 
        background: linear-gradient(135deg, rgba(255, 107, 157, 0.2) 0%, rgba(192, 108, 132, 0.15) 100%);
        border-left: 3px solid #ff6b9d;
    }
    .tool-card-3 { 
        background: linear-gradient(135deg, rgba(255, 117, 140, 0.2) 0%, rgba(255, 126, 179, 0.15) 100%);
        border-left: 3px solid #ff758c;
    }
    .tool-card-4 { 
        background: linear-gradient(135deg, rgba(250, 112, 154, 0.2) 0%, rgba(254, 225, 64, 0.15) 100%);
        border-left: 3px solid #fa709a;
    }
    .tool-card-5 { 
        background: linear-gradient(135deg, rgba(213, 51, 105, 0.2) 0%, rgba(218, 174, 81, 0.15) 100%);
        border-left: 3px solid #d53369;
    }
    .tool-card-6 { 
        background: linear-gradient(135deg, rgba(248, 87, 166, 0.2) 0%, rgba(255, 88, 88, 0.15) 100%);
        border-left: 3px solid #f857a6;
    }
    .tool-card-7 { 
        background: linear-gradient(135deg, rgba(255, 154, 158, 0.2) 0%, rgba(254, 207, 239, 0.15) 100%);
        border-left: 3px solid #ff9a9e;
    }
    .tool-card-8 { 
        background: linear-gradient(135deg, rgba(255, 236, 210, 0.2) 0%, rgba(252, 182, 159, 0.15) 100%);
        border-left: 3px solid #ffecd2;
    }
    .tool-card-9 { 
        background: linear-gradient(135deg, rgba(255, 110, 127, 0.2) 0%, rgba(191, 233, 255, 0.15) 100%);
        border-left: 3px solid #ff6e7f;
    }
    .tool-card-10 { 
        background: linear-gradient(135deg, rgba(224, 195, 252, 0.2) 0%, rgba(142, 197, 252, 0.15) 100%);
        border-left: 3px solid #e0c3fc;
    }
    .tool-card-11 { 
        background: linear-gradient(135deg, rgba(240, 147, 251, 0.2) 0%, rgba(245, 87, 108, 0.15) 100%);
        border-left: 3px solid #f093fb;
    }
    .tool-card-12 { 
        background: linear-gradient(135deg, rgba(255, 117, 140, 0.2) 0%, rgba(255, 126, 179, 0.15) 100%);
        border-left: 3px solid #ff758c;
    }
    
    /* Enhanced Micro-interactions for Main Buttons */
    .stButton>button {
        background: var(--glass-bg);
        backdrop-filter: blur(10px) saturate(180%);
        -webkit-backdrop-filter: blur(10px) saturate(180%);
        color: var(--accent-primary);
        border: 2px solid var(--glass-border);
        border-radius: 15px;
        padding: 14px 28px;
        font-weight: 700;
        font-size: 1rem;
        width: 100%;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: var(--shadow-glass);
        position: relative;
        overflow: hidden;
    }
    
    .stButton>button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 0, 128, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton>button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
        color: white;
        transform: translateY(-4px) scale(1.02);
        box-shadow: 
            0 0 20px rgba(255, 0, 128, 0.4),
            0 10px 30px rgba(255, 0, 128, 0.3);
        border-color: var(--accent-primary);
    }
    
    .stButton>button:active {
        transform: translateY(-2px) scale(0.98);
    }
    
    /* Glassmorphism Sidebar Buttons with Micro-interactions */
    [data-testid="stSidebar"] .stButton>button {
        background: var(--glass-bg);
        backdrop-filter: blur(10px) saturate(180%);
        -webkit-backdrop-filter: blur(10px) saturate(180%);
        color: var(--text-primary);
        border: 1px solid var(--glass-border);
        border-radius: 12px;
        padding: 12px 18px;
        font-weight: 600;
        font-size: 0.95rem;
        text-align: left;
        box-shadow: var(--shadow-glass);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    [data-testid="stSidebar"] .stButton>button::after {
        content: '→';
        position: absolute;
        right: 15px;
        opacity: 0;
        transition: all 0.3s ease;
    }
    
    [data-testid="stSidebar"] .stButton>button:hover {
        background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
        color: white;
        transform: translateX(8px);
        box-shadow: 
            0 0 15px rgba(255, 0, 128, 0.4),
            0 5px 20px rgba(255, 0, 128, 0.3);
        border-color: transparent;
    }
    
    [data-testid="stSidebar"] .stButton>button:hover::after {
        opacity: 1;
        right: 10px;
    }
    
    /* Pulse animation for active elements */
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    /* Loading spinner with glassmorphism */
    .stSpinner > div {
        border-color: var(--accent-primary) transparent transparent transparent !important;
    }
    
    /* Info/Success/Warning boxes with glassmorphism */
    .stAlert {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(10px) saturate(180%);
        -webkit-backdrop-filter: blur(10px) saturate(180%);
        border: 1px solid var(--glass-border) !important;
        border-radius: 15px !important;
        box-shadow: var(--shadow-glass) !important;
    }
    
    /* Smooth scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--glass-bg);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--accent-primary);
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--accent-secondary);
        box-shadow: 0 0 10px rgba(255, 0, 128, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Welcome message on first visit
if st.session_state.first_visit:
    st.balloons()
    st.session_state.first_visit = False

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style='background: var(--glass-bg);
                backdrop-filter: blur(20px) saturate(180%);
                -webkit-backdrop-filter: blur(20px) saturate(180%);
                border: 1px solid var(--glass-border);
                padding: 1.5rem; border-radius: 15px; text-align: center; 
                margin-bottom: 1rem; color: var(--text-primary);
                box-shadow: var(--shadow-glass);
                position: relative;
                overflow: hidden;'>
        <div style='position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
                    background: linear-gradient(90deg, transparent, rgba(255, 0, 128, 0.1), transparent);
                    animation: shimmer 4s linear infinite;'></div>
        <h2 style='margin: 0; position: relative; z-index: 1; text-shadow: 2px 2px 4px rgba(233, 30, 99, 0.2);'>🎯 Select Tool</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Home button
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.selected_tool = None
        st.rerun()
    
    st.markdown("---")
    
    # Tool selection
    for tool_name, tool_info in TOOLS.items():
        if st.button(f"{tool_info['icon']} {tool_name.split(' ', 1)[1]}", 
                    key=f"btn_{tool_name}",
                    use_container_width=True):
            st.session_state.selected_tool = tool_name
            st.rerun()

# Main content
if st.session_state.selected_tool is None:
    # Home page - Show balloons on first visit
    if st.session_state.first_visit:
        st.balloons()
        st.session_state.first_visit = False
    
    st.markdown("""
    <div class="main-header">
        <h1>🏗️ PWD Tools Suite</h1>
        <p style="font-size: 1.2rem; margin: 0.5rem 0;">Professional Tools for Public Works Department</p>
        <p style="font-size: 0.95rem; opacity: 0.9; margin-top: 1rem;">
            Initiative: Mrs. Premlata Jain, AAO, PWD Udaipur
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Welcome message
    st.success("🎉 Welcome to PWD Tools Suite! Select any tool below to get started.")
    
    # Quick stats with icons
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🛠️ **13 Tools** available for your workflow")
    with col2:
        st.success("✅ **Production Ready** - Fully tested")
    with col3:
        st.warning("⚡ **Fast Performance** - Optimized")
    
    st.markdown("---")
    
    # Display tools in grid
    cols = st.columns(3)
    for idx, (tool_name, tool_info) in enumerate(TOOLS.items()):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="tool-card tool-card-{idx}">
                <div style="font-size: 3.5rem; text-align: center; margin-bottom: 15px; 
                            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">
                    {tool_info['icon']}
                </div>
                <div style="font-size: 0.95rem; color: rgba(255,255,255,0.95); text-align: center; 
                            min-height: 60px; line-height: 1.6; margin-bottom: 15px;">
                    {tool_info['description']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"🚀 {tool_name.split(' ', 1)[1]}", key=f"launch_{tool_name}", use_container_width=True):
                st.session_state.selected_tool = tool_name
                st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='background: var(--glass-bg);
                backdrop-filter: blur(20px) saturate(180%);
                -webkit-backdrop-filter: blur(20px) saturate(180%);
                border: 1px solid var(--glass-border);
                padding: 2rem; border-radius: 20px; text-align: center; color: var(--text-primary);
                box-shadow: var(--shadow-glass);
                position: relative;
                overflow: hidden;'>
        <div style='position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
                    background: linear-gradient(90deg, transparent, rgba(255, 0, 128, 0.1), transparent);
                    animation: shimmer 4s linear infinite;'></div>
        <p style='font-size: 1.3rem; font-weight: 700; margin: 0; position: relative; z-index: 1;
                   text-shadow: 2px 2px 4px rgba(233, 30, 99, 0.2);'>
            🏗️ PWD Tools Suite v2.0
        </p>
        <p style='font-size: 1rem; margin: 1rem 0; position: relative; z-index: 1;'>
            <strong>Prepared on Initiative of:</strong><br>
            Mrs. Premlata Jain, AAO | PWD Udaipur, Rajasthan
        </p>
    </div>
    """, unsafe_allow_html=True)

else:
    # Load and run selected tool
    tool_info = TOOLS[st.session_state.selected_tool]
    tool_file = tool_info['file']
    
    # Show tool header
    st.markdown(f"""
    <div style='background: var(--glass-bg);
                backdrop-filter: blur(20px) saturate(180%);
                -webkit-backdrop-filter: blur(20px) saturate(180%);
                border: 1px solid var(--glass-border);
                padding: 1.5rem; border-radius: 15px; color: var(--text-primary); margin-bottom: 1rem;
                box-shadow: var(--shadow-glass);
                position: relative;
                overflow: hidden;'>
        <div style='position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
                    background: linear-gradient(90deg, transparent, rgba(255, 0, 128, 0.1), transparent);
                    animation: shimmer 4s linear infinite;'></div>
        <h2 style='margin: 0; position: relative; z-index: 1;'>{tool_info['icon']} {st.session_state.selected_tool.split(' ', 1)[1]}</h2>
        <p style='margin: 0.5rem 0 0 0; opacity: 0.9; position: relative; z-index: 1;'>{tool_info['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load and execute the tool
    try:
        # Import the tool module
        spec = importlib.util.spec_from_file_location("tool_module", tool_file)
        tool_module = importlib.util.module_from_spec(spec)
        
        # Execute the tool (this will run its Streamlit code)
        spec.loader.exec_module(tool_module)
        
    except Exception as e:
        st.error(f"Error loading tool: {str(e)}")
        st.info(f"Tool file: {tool_file}")
        
        if st.button("🏠 Return to Home"):
            st.session_state.selected_tool = None
            st.rerun()
