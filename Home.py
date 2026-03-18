"""
PWD Tools Suite - Unified Application
All 13 tools in one seamless interface
"""

import streamlit as st
from pathlib import Path
import sys

# Add paths
sys.path.insert(0, str(Path(__file__).parent))

# Page config
st.set_page_config(
    page_title="PWD Tools Suite",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with International 2025 Design Trends - Glassmorphism
st.markdown("""
<style>
    /* CSS Variables for theming */
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
    
    .main {
        background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 50%, var(--bg-primary) 100%);
        transition: all 0.3s ease;
    }
    
    /* Hide Streamlit branding and clean up top area */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    header {visibility: hidden;}
    
    [data-testid="stToolbar"] {
        display: none;
    }
    
    [data-testid="stHeader"] {
        background: transparent;
        display: none;
    }
    
    .block-container {
        padding-top: 2rem;
    }
    
    /* Glassmorphism Header */
    .header {
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
    }
    
    .header::before {
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
    
    .header h1, .header p {
        position: relative;
        z-index: 1;
        text-shadow: 2px 2px 8px rgba(233, 30, 99, 0.3);
    }
    
    /* Glassmorphism Tool Cards - Bento Grid Style */
    .tool-card {
        background: var(--glass-bg);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 30px;
        margin: 15px 0;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
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
        box-shadow: 
            0 0 20px rgba(255, 0, 128, 0.3),
            0 0 40px rgba(255, 0, 128, 0.2),
            0 20px 60px rgba(255, 0, 128, 0.4);
        border-color: var(--accent-primary);
    }
    
    /* Unique glassmorphism variants for each tool */
    .tool-card-1 { 
        background: linear-gradient(135deg, rgba(233, 30, 99, 0.2) 0%, rgba(194, 24, 91, 0.15) 100%);
        border-left: 3px solid #e91e63;
    }
    .tool-card-2 { 
        background: linear-gradient(135deg, rgba(240, 147, 251, 0.2) 0%, rgba(245, 87, 108, 0.15) 100%);
        border-left: 3px solid #f093fb;
    }
    .tool-card-3 { 
        background: linear-gradient(135deg, rgba(255, 107, 157, 0.2) 0%, rgba(192, 108, 132, 0.15) 100%);
        border-left: 3px solid #ff6b9d;
    }
    .tool-card-4 { 
        background: linear-gradient(135deg, rgba(255, 117, 140, 0.2) 0%, rgba(255, 126, 179, 0.15) 100%);
        border-left: 3px solid #ff758c;
    }
    .tool-card-5 { 
        background: linear-gradient(135deg, rgba(250, 112, 154, 0.2) 0%, rgba(254, 225, 64, 0.15) 100%);
        border-left: 3px solid #fa709a;
    }
    .tool-card-6 { 
        background: linear-gradient(135deg, rgba(213, 51, 105, 0.2) 0%, rgba(218, 174, 81, 0.15) 100%);
        border-left: 3px solid #d53369;
    }
    .tool-card-7 { 
        background: linear-gradient(135deg, rgba(248, 87, 166, 0.2) 0%, rgba(255, 88, 88, 0.15) 100%);
        border-left: 3px solid #f857a6;
    }
    .tool-card-8 { 
        background: linear-gradient(135deg, rgba(255, 154, 158, 0.2) 0%, rgba(254, 207, 239, 0.15) 100%);
        border-left: 3px solid #ff9a9e;
    }
    .tool-card-9 { 
        background: linear-gradient(135deg, rgba(255, 236, 210, 0.2) 0%, rgba(252, 182, 159, 0.15) 100%);
        border-left: 3px solid #ffecd2;
    }
    .tool-card-10 { 
        background: linear-gradient(135deg, rgba(255, 110, 127, 0.2) 0%, rgba(191, 233, 255, 0.15) 100%);
        border-left: 3px solid #ff6e7f;
    }
    .tool-card-11 { 
        background: linear-gradient(135deg, rgba(224, 195, 252, 0.2) 0%, rgba(142, 197, 252, 0.15) 100%);
        border-left: 3px solid #e0c3fc;
    }
    .tool-card-12 { 
        background: linear-gradient(135deg, rgba(240, 147, 251, 0.2) 0%, rgba(245, 87, 108, 0.15) 100%);
        border-left: 3px solid #f093fb;
    }
    .tool-card-13 { 
        background: linear-gradient(135deg, rgba(255, 117, 140, 0.2) 0%, rgba(255, 126, 179, 0.15) 100%);
        border-left: 3px solid #ff758c;
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
    
    /* Enhanced Micro-interactions for Buttons */
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

# Header
st.markdown("""
<div class="header">
    <h1>🏗️ PWD Tools Suite</h1>
    <p style="font-size: 1.3rem; margin: 0.5rem 0;">Professional Tools for Public Works Department</p>
    <p style="font-size: 1rem; opacity: 0.9; margin-top: 1rem;">
        Initiative: Mrs. Premlata Jain, AAO, PWD Udaipur
    </p>
</div>
""", unsafe_allow_html=True)

# Welcome message
if 'first_visit' not in st.session_state:
    st.session_state.first_visit = True
    st.balloons()

# Tool data
tools_data = [
    ("1__Bill_Generator", "🏗️", "Bill Generator", "Complete bill package with all documents and PDFs"),
    ("2__Excel_to_EMD", "📊", "Excel to EMD", "Generate EMD receipts from Excel"),
    ("3__EMD_Refund", "💸", "EMD Refund", "Calculate EMD refunds with penalties"),
    ("4__Security_Refund", "🔒", "Security Refund", "Security deposit refund calculator"),
    ("5__Bill_Note_Sheet", "📝", "Bill Note Sheet", "Generate bill note sheets with LD calculation"),
    ("6__Deductions_Table", "➖", "Deductions Table", "Calculate TDS and security deductions"),
    ("7__Financial_Progress", "📈", "Financial Progress", "Track financial progress of projects"),
    ("8__APG_Calculator", "🧮", "APG Calculator", "50% of savings beyond -15% below G-Schedule"),
    ("9__Delay_Calculator", "⏱️", "Delay Calculator", "Calculate project delays and extensions"),
    ("10__Stamp_Duty", "⚖️", "Stamp Duty", "Calculate stamp duty for documents"),
    ("11__Hand_Receipt", "🧾", "Hand Receipt", "Generate RPWA 28 compliant hand receipts"),
    ("12__User_Manual", "📖", "User Manual", "Bilingual user manual (English/Hindi)"),
    ("13_ℹ_Main_Info", "ℹ️", "Main Info", "Information about launcher program"),
]

# Display tools in grid with working buttons
cols = st.columns(3)
for idx, (page_name, icon, name, desc) in enumerate(tools_data):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="tool-card tool-card-{idx+1}">
            <div style="font-size: 3.5rem; text-align: center; margin-bottom: 15px; 
                        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">
                {icon}
            </div>
            <div style="font-weight: bold; font-size: 1.2rem; color: white; 
                        text-align: center; margin-bottom: 12px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);">
                {name}
            </div>
            <div style="font-size: 0.95rem; color: rgba(255,255,255,0.95); text-align: center; 
                        min-height: 60px; line-height: 1.6; margin-bottom: 15px;">
                {desc}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Add clickable button
        if st.button(f"🚀 Launch", key=f"launch_{page_name}", use_container_width=True):
            st.switch_page(f"pages/{page_name}.py")

# Footer with Glassmorphism
st.markdown("---")
st.markdown("""
<div style='background: var(--glass-bg);
            backdrop-filter: blur(20px) saturate(180%);
            -webkit-backdrop-filter: blur(20px) saturate(180%);
            border: 1px solid var(--glass-border);
            padding: 2.5rem; border-radius: 20px; text-align: center; color: var(--text-primary);
            box-shadow: var(--shadow-glass);
            position: relative;
            overflow: hidden;'>
    <div style='position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
                background: linear-gradient(90deg, transparent, rgba(255, 0, 128, 0.1), transparent);
                animation: shimmer 4s linear infinite;'></div>
    <p style='font-size: 1.5rem; font-weight: 700; margin: 0; position: relative; z-index: 1;
               text-shadow: 2px 2px 4px rgba(233, 30, 99, 0.2);'>
        🏗️ PWD Tools Suite v2.0
    </p>
    <p style='font-size: 1.1rem; margin: 1.5rem 0; position: relative; z-index: 1;'>
        <strong>Prepared on Initiative of:</strong><br>
        <span style='font-size: 1.3rem;'>Mrs. Premlata Jain, AAO</span><br>
        PWD Udaipur, Rajasthan
    </p>
</div>
""", unsafe_allow_html=True)
