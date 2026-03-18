"""
PWD Tools Suite - Main Application
All 13 tools in one deployable app with beautiful UI
"""

import streamlit as st
from pathlib import Path
import sys
import importlib.util
from datetime import datetime

# Add tools directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Page configuration
st.set_page_config(
    page_title="PWD Tools Suite | Professional Infrastructure Management",
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
    "🏗️ Bill Generator Enterprise": {
        "file": "tools/bill_generator_enterprise.py",
        "description": "Complete bill package with all documents and PDFs",
        "icon": "🏗️"
    },
    "📊 Excel to EMD": {
        "file": "tools/excel_to_emd_web.py",
        "description": "Generate EMD receipts from Excel (batch processing)",
        "icon": "📊"
    },
    "💸 EMD Refund Calculator": {
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
        "description": "Generate bill note sheets with LD calculation",
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
        "description": "50% of savings beyond -15% below G-Schedule",
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
    "🧾 Hand Receipt (RPWA 28)": {
        "file": "tools/hand_receipt.py",
        "description": "Generate RPWA 28 compliant hand receipts",
        "icon": "🧾"
    },
    "📖 User Manual": {
        "file": "tools/user_manual.py",
        "description": "Bilingual user manual (English/Hindi)",
        "icon": "📖"
    },
    "ℹ️ Main BAT Info": {
        "file": "tools/main_bat_info.py",
        "description": "Information about launcher program",
        "icon": "ℹ️"
    }
}

# Custom CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    .main-header {
        background: linear-gradient(to right, #667eea, #764ba2);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
    }
    
    .tool-button {
        background: white;
        border: 2px solid #667eea;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .tool-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3);
        border-color: #764ba2;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4);
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
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 1.5rem; border-radius: 10px; text-align: center; 
                margin-bottom: 1rem; color: white;'>
        <h2 style='margin: 0;'>🎯 Select Tool</h2>
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
    
    st.markdown("---")
    st.info(f"""
    **PWD Tools Suite v2.0**
    
    ✅ {len(TOOLS)} tools available
    ✅ Production ready
    
    **Status:** 🟢 Operational
    """)

# Main content
if st.session_state.selected_tool is None:
    # Home page
    st.markdown("""
    <div class="main-header">
        <h1>🏗️ PWD Tools Suite</h1>
        <p style="font-size: 1.2rem; margin: 0.5rem 0;">13 Professional Tools for Public Works Department</p>
        <p style="font-size: 0.95rem; opacity: 0.9; margin-top: 1rem;">
            Initiative: Mrs. Premlata Jain, AAO, PWD Udaipur
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Tools", len(TOOLS))
    with col2:
        st.metric("Status", "Ready", delta="100%")
    with col3:
        st.metric("Performance", "Fast", delta="⚡")
    
    st.markdown("---")
    st.markdown("## 🔧 Available Tools")
    
    # Display tools in grid
    cols = st.columns(3)
    for idx, (tool_name, tool_info) in enumerate(TOOLS.items()):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="tool-button">
                <div style="font-size: 2.5rem; text-align: center; margin-bottom: 10px;">
                    {tool_info['icon']}
                </div>
                <div style="font-weight: bold; font-size: 1rem; text-align: center; margin-bottom: 10px;">
                    {tool_name.split(' ', 1)[1]}
                </div>
                <div style="font-size: 0.85rem; color: #636e72; text-align: center; min-height: 50px;">
                    {tool_info['description']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Launch", key=f"launch_{tool_name}", use_container_width=True):
                st.session_state.selected_tool = tool_name
                st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2rem; border-radius: 15px; text-align: center; color: white;'>
        <p style='font-size: 1.3rem; font-weight: 700; margin: 0;'>
            🏗️ PWD Tools Suite v2.0
        </p>
        <p style='font-size: 1rem; margin: 1rem 0;'>
            <strong>Prepared on Initiative of:</strong><br>
            Mrs. Premlata Jain, AAO | PWD Udaipur, Rajasthan
        </p>
        <p style='font-size: 0.9rem; margin: 0.5rem 0;'>
            13 Professional Tools | All Independently Deployable | 100% Production Ready
        </p>
    </div>
    """, unsafe_allow_html=True)

else:
    # Load and run selected tool
    tool_info = TOOLS[st.session_state.selected_tool]
    tool_file = tool_info['file']
    
    # Show tool header
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 1.5rem; border-radius: 10px; color: white; margin-bottom: 1rem;'>
        <h2 style='margin: 0;'>{tool_info['icon']} {st.session_state.selected_tool.split(' ', 1)[1]}</h2>
        <p style='margin: 0.5rem 0 0 0; opacity: 0.9;'>{tool_info['description']}</p>
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
