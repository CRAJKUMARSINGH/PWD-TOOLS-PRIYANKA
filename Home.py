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

# Custom CSS with Magenta Theme
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 50%, #fce4ec 100%);
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
    
    .header {
        background: linear-gradient(90deg, #880e4f, #c2185b, #e91e63, #c2185b, #880e4f);
        background-size: 200% auto;
        animation: shimmer 4s linear infinite;
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 20px rgba(233, 30, 99, 0.4);
    }
    
    @keyframes shimmer {
        0% { background-position: -200% center; }
        100% { background-position: 200% center; }
    }
    
    .tool-card {
        background: linear-gradient(135deg, #e91e63 0%, #c2185b 100%);
        border: none;
        border-radius: 15px;
        padding: 30px;
        margin: 15px 0;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 8px 20px rgba(233, 30, 99, 0.4);
        color: white;
    }
    
    .tool-card:hover {
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 15px 35px rgba(233, 30, 99, 0.6);
    }
    
    .tool-card-1 { background: linear-gradient(135deg, #e91e63 0%, #c2185b 100%); }
    .tool-card-2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
    .tool-card-3 { background: linear-gradient(135deg, #ff6b9d 0%, #c06c84 100%); }
    .tool-card-4 { background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%); }
    .tool-card-5 { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); }
    .tool-card-6 { background: linear-gradient(135deg, #d53369 0%, #daae51 100%); }
    .tool-card-7 { background: linear-gradient(135deg, #f857a6 0%, #ff5858 100%); }
    .tool-card-8 { background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); }
    .tool-card-9 { background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); }
    .tool-card-10 { background: linear-gradient(135deg, #ff6e7f 0%, #bfe9ff 100%); }
    .tool-card-11 { background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%); }
    .tool-card-12 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
    .tool-card-13 { background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%); }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fce4ec 0%, #f8bbd0 100%);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: linear-gradient(180deg, #fce4ec 0%, #f8bbd0 100%);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #ffffff 0%, #fce4ec 100%);
        color: #c2185b;
        border: 2px solid rgba(233, 30, 99, 0.3);
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 700;
        font-size: 1rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(233, 30, 99, 0.2);
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #e91e63 0%, #c2185b 100%);
        color: white;
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(233, 30, 99, 0.5);
        border-color: transparent;
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

# Footer
st.markdown("---")
st.markdown("""
<div style='background: linear-gradient(90deg, #880e4f, #c2185b, #e91e63, #c2185b, #880e4f);
            background-size: 200% auto;
            animation: shimmer 4s linear infinite;
            padding: 2.5rem; border-radius: 15px; text-align: center; color: white;
            box-shadow: 0 8px 20px rgba(233, 30, 99, 0.4);'>
    <p style='font-size: 1.5rem; font-weight: 700; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);'>
        🏗️ PWD Tools Suite v2.0
    </p>
    <p style='font-size: 1.1rem; margin: 1.5rem 0;'>
        <strong>Prepared on Initiative of:</strong><br>
        <span style='font-size: 1.3rem;'>Mrs. Premlata Jain, AAO</span><br>
        PWD Udaipur, Rajasthan
    </p>
</div>
""", unsafe_allow_html=True)
