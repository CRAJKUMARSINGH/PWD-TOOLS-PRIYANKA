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

# Custom CSS with Beautiful Magenta Theme
st.markdown("""
<style>
    /* Main background */
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
    
    /* Beautiful header with magenta gradient */
    .main-header {
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
    
    /* Sidebar styling with magenta */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fce4ec 0%, #f8bbd0 100%);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: linear-gradient(180deg, #fce4ec 0%, #f8bbd0 100%);
    }
    
    /* Tool cards with beautiful gradients */
    .tool-card {
        background: linear-gradient(135deg, #e91e63 0%, #c2185b 100%);
        border: none;
        border-radius: 15px;
        padding: 30px;
        margin: 15px 0;
        transition: all 0.3s ease;
        box-shadow: 0 8px 20px rgba(233, 30, 99, 0.4);
        color: white;
    }
    
    .tool-card:hover {
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 15px 35px rgba(233, 30, 99, 0.6);
    }
    
    /* Different magenta/pink gradients for each tool */
    .tool-card-0 { background: linear-gradient(135deg, #e91e63 0%, #c2185b 100%); }
    .tool-card-1 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
    .tool-card-2 { background: linear-gradient(135deg, #ff6b9d 0%, #c06c84 100%); }
    .tool-card-3 { background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%); }
    .tool-card-4 { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); }
    .tool-card-5 { background: linear-gradient(135deg, #d53369 0%, #daae51 100%); }
    .tool-card-6 { background: linear-gradient(135deg, #f857a6 0%, #ff5858 100%); }
    .tool-card-7 { background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); }
    .tool-card-8 { background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); }
    .tool-card-9 { background: linear-gradient(135deg, #ff6e7f 0%, #bfe9ff 100%); }
    .tool-card-10 { background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%); }
    .tool-card-11 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
    .tool-card-12 { background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%); }
    
    /* Main area buttons with magenta theme */
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
    
    /* Sidebar buttons with magenta gradient */
    [data-testid="stSidebar"] .stButton>button {
        background: linear-gradient(135deg, #e91e63 0%, #c2185b 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 16px;
        font-weight: 600;
        font-size: 0.95rem;
        text-align: left;
        box-shadow: 0 2px 8px rgba(233, 30, 99, 0.3);
    }
    
    [data-testid="stSidebar"] .stButton>button:hover {
        background: linear-gradient(135deg, #c2185b 0%, #f093fb 100%);
        transform: translateX(5px);
        box-shadow: 0 4px 12px rgba(233, 30, 99, 0.5);
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
    <div style='background: linear-gradient(90deg, #880e4f, #c2185b, #e91e63, #c2185b, #880e4f); 
                background-size: 200% auto;
                animation: shimmer 4s linear infinite;
                padding: 1.5rem; border-radius: 10px; text-align: center; 
                margin-bottom: 1rem; color: white;
                box-shadow: 0 4px 15px rgba(233, 30, 99, 0.4);'>
        <h2 style='margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);'>🎯 Select Tool</h2>
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
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2rem; border-radius: 15px; text-align: center; color: white;'>
        <p style='font-size: 1.3rem; font-weight: 700; margin: 0;'>
            🏗️ PWD Tools Suite v2.0
        </p>
        <p style='font-size: 1rem; margin: 1rem 0;'>
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
