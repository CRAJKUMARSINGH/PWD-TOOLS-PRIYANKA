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

# Custom CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    .header {
        background: linear-gradient(to right, #667eea, #764ba2);
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
    }
    
    .tool-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        border-radius: 15px;
        padding: 30px;
        margin: 15px 0;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        color: white;
    }
    
    .tool-card:hover {
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #f093fb 100%);
    }
    
    .tool-card-1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    .tool-card-2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
    .tool-card-3 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
    .tool-card-4 { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }
    .tool-card-5 { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); }
    .tool-card-6 { background: linear-gradient(135deg, #30cfd0 0%, #330867 100%); }
    .tool-card-7 { background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); }
    .tool-card-8 { background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); }
    .tool-card-9 { background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); }
    .tool-card-10 { background: linear-gradient(135deg, #ff6e7f 0%, #bfe9ff 100%); }
    .tool-card-11 { background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%); }
    .tool-card-12 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
    .tool-card-13 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f5f7fa 0%, #e8ecf1 100%);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
    <h1>🏗️ PWD Tools Suite</h1>
    <p style="font-size: 1.3rem; margin: 0.5rem 0;">13 Professional Tools for Public Works Department</p>
    <p style="font-size: 1rem; opacity: 0.9; margin-top: 1rem;">
        Initiative: Mrs. Premlata Jain, AAO, PWD Udaipur
    </p>
</div>
""", unsafe_allow_html=True)

# Welcome message
if 'first_visit' not in st.session_state:
    st.session_state.first_visit = True
    st.balloons()

# Stats
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 20px; border-radius: 12px; text-align: center; color: white;'>
        <div style='font-size: 2.5rem;'>🏗️</div>
        <div style='font-size: 1.8rem; font-weight: bold; margin: 10px 0;'>13</div>
        <div style='font-size: 0.9rem;'>Total Tools</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                padding: 20px; border-radius: 12px; text-align: center; color: white;'>
        <div style='font-size: 2.5rem;'>✅</div>
        <div style='font-size: 1.8rem; font-weight: bold; margin: 10px 0;'>100%</div>
        <div style='font-size: 0.9rem;'>Ready</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                padding: 20px; border-radius: 12px; text-align: center; color: white;'>
        <div style='font-size: 2.5rem;'>⚡</div>
        <div style='font-size: 1.8rem; font-weight: bold; margin: 10px 0;'>Fast</div>
        <div style='font-size: 0.9rem;'>Performance</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
                padding: 20px; border-radius: 12px; text-align: center; color: white;'>
        <div style='font-size: 2.5rem;'>🚀</div>
        <div style='font-size: 1.8rem; font-weight: bold; margin: 10px 0;'>v2.0.1</div>
        <div style='font-size: 0.9rem;'>Version</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Instructions
st.info("👈 **Select a tool from the sidebar to get started!**")

st.markdown("---")

# Tool categories
st.markdown("## 🔧 Available Tools")

tools_data = [
    ("1__Bill_Generator", "🏗️", "Bill Generator Enterprise", "Complete bill package with all documents and PDFs"),
    ("2__Excel_to_EMD", "📊", "Excel to EMD", "Generate EMD receipts from Excel (batch processing)"),
    ("3__EMD_Refund", "💸", "EMD Refund Calculator", "Calculate EMD refunds with penalties"),
    ("4__Security_Refund", "🔒", "Security Refund", "Security deposit refund calculator"),
    ("5__Bill_Note_Sheet", "📝", "Bill Note Sheet", "Generate bill note sheets with LD calculation"),
    ("6__Deductions_Table", "➖", "Deductions Table", "Calculate TDS and security deductions"),
    ("7__Financial_Progress", "📈", "Financial Progress", "Track financial progress of projects"),
    ("8__APG_Calculator", "🧮", "APG Calculator", "50% of savings beyond -15% below G-Schedule"),
    ("9__Delay_Calculator", "⏱️", "Delay Calculator", "Calculate project delays and extensions"),
    ("10__Stamp_Duty", "⚖️", "Stamp Duty", "Calculate stamp duty for documents"),
    ("11__Hand_Receipt", "🧾", "Hand Receipt", "Generate RPWA 28 compliant hand receipts"),
    ("12__User_Manual", "📖", "User Manual", "Bilingual user manual (English/Hindi)"),
    ("13_ℹ_Main_Info", "ℹ️", "Main BAT Info", "Information about launcher program"),
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
        if st.button(f"Launch {name}", key=f"launch_{page_name}", use_container_width=True):
            st.switch_page(f"pages/{page_name}.py")

# Footer
st.markdown("---")
st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2.5rem; border-radius: 15px; text-align: center; color: white;
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);'>
    <p style='font-size: 1.5rem; font-weight: 700; margin: 0;'>
        🏗️ PWD Tools Suite v2.0
    </p>
    <p style='font-size: 1.1rem; margin: 1.5rem 0;'>
        <strong>Prepared on Initiative of:</strong><br>
        <span style='font-size: 1.3rem;'>Mrs. Premlata Jain, AAO</span><br>
        PWD Udaipur, Rajasthan
    </p>
    <p style='font-size: 1rem; margin: 1rem 0;'>
        13 Professional Tools | Unified Interface | 100% Production Ready
    </p>
    <p style='font-size: 0.95rem; margin: 0.5rem 0; opacity: 0.9;'>
        🤖 AI Development Partner: Kiro AI Assistant
    </p>
</div>
""", unsafe_allow_html=True)
