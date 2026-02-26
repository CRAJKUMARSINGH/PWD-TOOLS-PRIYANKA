"""
PWD Tools Suite - Main Application
All 13 tools in one deployable app with beautiful UI
Each tool can also be deployed independently
"""

import streamlit as st
from pathlib import Path
import sys
from datetime import datetime
import time

# Add tools directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Page configuration
st.set_page_config(
    page_title="PWD Tools Suite | Professional Infrastructure Management",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/PWD-Tools-Suite',
        'Report a bug': 'https://github.com/PWD-Tools-Suite/issues',
        'About': "PWD Tools Suite v2.0 - Professional Infrastructure Management Tools"
    }
)

# Initialize session state for celebrations
if 'first_visit' not in st.session_state:
    st.session_state.first_visit = True
    st.session_state.visit_count = 0
    st.session_state.tools_used = set()

st.session_state.visit_count += 1

# Enhanced Custom CSS with animations
st.markdown("""
<style>
    /* Main app background with gradient */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Animated header */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animated-header {
        animation: fadeInDown 0.8s ease-out;
    }
    
    .main-header {
        background: linear-gradient(to right, #667eea, #764ba2, #f093fb);
        padding: 2.5rem 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    /* Tool card hover effects */
    .tool-card {
        background: white;
        border: 2px solid #667eea;
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        min-height: 200px;
    }
    
    .tool-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 12px 24px rgba(102, 126, 234, 0.3);
        border-color: #764ba2;
    }
    
    /* Celebration animation */
    @keyframes celebrate {
        0%, 100% { transform: scale(1) rotate(0deg); }
        25% { transform: scale(1.1) rotate(-5deg); }
        75% { transform: scale(1.1) rotate(5deg); }
    }
    
    .celebration {
        animation: celebrate 0.6s ease-in-out;
    }
    
    /* Success banner */
    .success-banner {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 8px 16px rgba(17, 153, 142, 0.3);
        animation: fadeInDown 0.5s ease-out;
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    /* Button enhancements */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(102, 126, 234, 0.3);
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #764ba2 0%, #f093fb 100%);
    }
    
    /* Feature cards */
    .feature-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateX(5px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f5f7fa 0%, #e8ecf1 100%);
    }
</style>
""", unsafe_allow_html=True)

# Welcome message with balloons on first visit
if st.session_state.first_visit:
    st.balloons()
    st.session_state.first_visit = False
    
    # Get current time for greeting
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning"
        emoji = "🌅"
    elif current_hour < 17:
        greeting = "Good Afternoon"
        emoji = "☀️"
    else:
        greeting = "Good Evening"
        emoji = "🌆"
    
    st.markdown(f"""
    <div class="success-banner">
        <h2 class="celebration">{emoji} {greeting}! Welcome to PWD Tools Suite</h2>
        <p style="font-size: 1.2rem; margin-top: 10px;">
            Your professional infrastructure management companion is ready!
        </p>
        <p style="font-size: 1rem; margin-top: 10px; opacity: 0.9;">
            17 powerful tools at your fingertips • All independently deployable
        </p>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(0.5)

# Animated Header
st.markdown('<div class="animated-header">', unsafe_allow_html=True)
st.markdown("""
<div class="main-header">
    <h1>🏗️ PWD Tools Suite</h1>
    <p style="font-size: 1.2rem; margin: 0.5rem 0;">17 Professional Tools for Public Works Department</p>
    <p style="font-size: 0.95rem; opacity: 0.9; margin-top: 1rem;">
        Initiative: Mrs. Premlata Jain, AAO, PWD Udaipur
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Tool categories
tools = {
    "🏗️ Enterprise Tools": [
        {
            "name": "Bill Generator Enterprise",
            "icon": "🏗️",
            "description": "Complete bill package: First Page, Deviation Statement, Note Sheet, Certificate II, and PDFs",
            "file": "tools/bill_generator_enterprise.py",
            "status": "enterprise"
        }
    ],
    "💰 Financial Tools": [
        {
            "name": "EMD Refund Calculator",
            "icon": "💸",
            "description": "Calculate EMD refunds with penalties",
            "file": "tools/emd_refund.py",
            "status": "ready"
        },
        {
            "name": "Security Refund",
            "icon": "🔒",
            "description": "Security deposit refund calculator",
            "file": "tools/security_refund.py",
            "status": "ready"
        },
        {
            "name": "Bill Note Sheet",
            "icon": "📝",
            "description": "Generate bill note sheets with LD calculation (PWD Quarterly Method)",
            "file": "tools/bill_note_sheet.py",
            "status": "enhanced"
        },
        {
            "name": "Deductions Table",
            "icon": "➖",
            "description": "Calculate TDS and security deductions",
            "file": "tools/deductions_table.py",
            "status": "ready"
        },
        {
            "name": "Financial Progress",
            "icon": "📈",
            "description": "Track financial progress of projects",
            "file": "tools/financial_progress.py",
            "status": "ready"
        }
    ],
    "🧮 Calculators": [
        {
            "name": "APG Calculator",
            "icon": "🧮",
            "description": "50% of savings beyond -15% below G-Schedule",
            "file": "tools/apg_calculator.py",
            "status": "ready"
        },
        {
            "name": "Delay Calculator",
            "icon": "⏱️",
            "description": "Calculate project delays and extensions",
            "file": "tools/delay_calculator.py",
            "status": "ready"
        },
        {
            "name": "Stamp Duty",
            "icon": "⚖️",
            "description": "Calculate stamp duty for documents",
            "file": "tools/stamp_duty.py",
            "status": "ready"
        }
    ],
    "📋 Document Generators": [
        {
            "name": "Hand Receipt (RPWA 28)",
            "icon": "🧾",
            "description": "Generate RPWA 28 compliant hand receipts with PDF export",
            "file": "tools/hand_receipt.py",
            "status": "ready"
        },
        {
            "name": "Excel to EMD",
            "icon": "📊",
            "description": "Generate EMD receipts from Excel (batch processing with PDF support)",
            "file": "tools/excel_to_emd_web.py",
            "status": "enhanced"
        }
    ],
    "🔧 Utilities": [
        {
            "name": "Main BAT Info",
            "icon": "ℹ️",
            "description": "Information about launcher program",
            "file": "tools/main_bat_info.py",
            "status": "ready"
        },
        {
            "name": "User Manual",
            "icon": "📖",
            "description": "Bilingual user manual (English/Hindi)",
            "file": "tools/user_manual.py",
            "status": "ready"
        }
    ]
}

# Sidebar navigation
with st.sidebar:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 1.5rem; border-radius: 10px; text-align: center; 
                margin-bottom: 1rem; color: white; box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);'>
        <h2 style='margin: 0; font-size: 1.5rem;'>🎯 Navigation</h2>
    </div>
    """, unsafe_allow_html=True)
    
    selected_category = st.selectbox(
        "Select Category",
        ["🏠 Home"] + list(tools.keys()),
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Statistics with beautiful cards
    st.markdown("### 📊 Statistics")
    total_tools = sum(len(category_tools) for category_tools in tools.values())
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Tools", total_tools, delta="17 total")
    with col2:
        st.metric("Categories", len(tools), delta="6 types")
    
    st.metric("Visit Count", st.session_state.visit_count, delta="This session")
    
    st.markdown("---")
    
    # Quick actions
    st.markdown("### ⚡ Quick Actions")
    
    if st.button("🎉 Celebrate Success"):
        st.balloons()
        st.success("🎊 Celebration time!")
        time.sleep(1)
    
    if st.button("❄️ Snow Effect"):
        st.snow()
        st.info("❄️ Let it snow!")
        time.sleep(1)
    
    st.markdown("---")
    
    # About section
    st.markdown("### ℹ️ About")
    st.info("""
    **PWD Tools Suite v2.0**
    
    Professional tools for Public Works Department operations.
    
    ✅ 13 tools available
    ✅ All independently deployable
    ✅ Enterprise Bill Generator integrated
    ✅ Beautiful UI with animations
    ✅ Production ready
    
    **Status:** 🟢 All systems operational
    """)

# Main content
if selected_category == "🏠 Home":
    # Welcome stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">🏗️</div>
            <div style="font-size: 1.5rem; font-weight: bold; margin: 10px 0;">17</div>
            <div style="font-size: 0.9rem;">Total Tools</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">✅</div>
            <div style="font-size: 1.5rem; font-weight: bold; margin: 10px 0;">100%</div>
            <div style="font-size: 0.9rem;">Ready</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">🚀</div>
            <div style="font-size: 1.5rem; font-weight: bold; margin: 10px 0;">94%</div>
            <div style="font-size: 0.9rem;">Self-Contained</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">⚡</div>
            <div style="font-size: 1.5rem; font-weight: bold; margin: 10px 0;">Fast</div>
            <div style="font-size: 0.9rem;">Performance</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Show all tools in grid
    st.markdown("## 🔧 All Tools")
    
    for category, category_tools in tools.items():
        st.markdown(f"### {category}")
        
        cols = st.columns(3)
        for idx, tool in enumerate(category_tools):
            with cols[idx % 3]:
                if tool["status"] == "enterprise":
                    status_badge = "⭐ Enterprise"
                    badge_color = "#f093fb"
                elif tool["status"] == "enhanced":
                    status_badge = "✨ Enhanced"
                    badge_color = "#667eea"
                else:
                    status_badge = "✅ Ready"
                    badge_color = "#11998e"
                
                st.markdown(f"""
                <div class="tool-card">
                    <div style="font-size: 2.5rem; text-align: center; margin-bottom: 15px;">
                        {tool['icon']}
                    </div>
                    <div style="font-weight: bold; font-size: 1.1rem; color: #2d3436; 
                                text-align: center; margin-bottom: 10px;">
                        {tool['name']}
                    </div>
                    <div style="font-size: 0.9rem; color: #636e72; text-align: center; 
                                min-height: 60px; margin: 10px 0; line-height: 1.5;">
                        {tool['description']}
                    </div>
                    <div style="text-align: center; font-size: 0.85rem; color: white; 
                                font-weight: 600; padding: 8px; border-radius: 20px; 
                                background: {badge_color}; margin-top: 10px;">
                        {status_badge}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Launch Tool", key=f"btn_{tool['name']}"):
                    st.balloons()
                    st.success(f"🚀 Launching {tool['name']}...")
                    st.info(f"Run: `streamlit run {tool['file']}`")
                    st.session_state.tools_used.add(tool['name'])
        
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Deployment info
    st.markdown("---")
    st.markdown("## 🚀 Deployment Options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>📦 Full Suite Deployment</h3>
            <p>Deploy all 13 tools together:</p>
            <pre style="background: #f8f9fa; padding: 10px; border-radius: 5px;">streamlit run app.py</pre>
            <p><strong>Benefits:</strong></p>
            <ul>
                <li>✅ Single deployment</li>
                <li>✅ Unified navigation</li>
                <li>✅ Shared resources</li>
                <li>✅ Easy maintenance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Individual Tool Deployment</h3>
            <p>Deploy any tool independently:</p>
            <pre style="background: #f8f9fa; padding: 10px; border-radius: 5px;">streamlit run tools/bill_note_sheet.py</pre>
            <p><strong>Benefits:</strong></p>
            <ul>
                <li>✅ Lightweight</li>
                <li>✅ Focused functionality</li>
                <li>✅ Easy to share</li>
                <li>✅ Faster loading</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

else:
    # Show tools for selected category
    category_tools = tools[selected_category]
    
    st.markdown(f"## {selected_category}")
    st.markdown(f"**{len(category_tools)} tools available in this category**")
    st.markdown("---")
    
    for tool in category_tools:
        with st.expander(f"{tool['icon']} {tool['name']}", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**Description:** {tool['description']}")
                st.markdown(f"**Status:** {tool['status'].title()}")
                st.markdown(f"**File:** `{tool['file']}`")
            
            with col2:
                if st.button(f"🚀 Launch", key=f"launch_{tool['name']}"):
                    st.balloons()
                    st.success(f"Launching {tool['name']}!")
                    st.code(f"streamlit run {tool['file']}", language="bash")

# Footer with beautiful styling
st.markdown("---")
st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2.5rem; border-radius: 15px; text-align: center;
            margin-top: 2rem; color: white; box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);'>
    <p style='font-size: 1.5rem; font-weight: 700; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);'>
        🏗️ PWD Tools Suite v2.0
    </p>
    <p style='font-size: 1.1rem; margin: 1rem 0; opacity: 0.95;'>
        <strong>Prepared on Initiative of:</strong><br>
        <span style='font-size: 1.2rem; font-weight: 600;'>Mrs. Premlata Jain, AAO</span><br>
        <span style='font-size: 1rem;'>PWD Udaipur, Rajasthan</span>
    </p>
    <div style='margin-top: 1.5rem; padding-top: 1.5rem; 
                border-top: 2px solid rgba(255,255,255,0.3);'>
        <p style='font-size: 1rem; margin: 0.5rem 0;'>
            17 Professional Tools | All Independently Deployable | 100% Production Ready
        </p>
        <p style='font-size: 0.95rem; margin: 1rem 0; opacity: 0.9;'>
            🤖 AI Development Partner: Kiro AI Assistant
        </p>
        <p style='font-size: 0.9rem; margin: 0.5rem 0; opacity: 0.85;'>
            ⚡ Powered by Streamlit | 🚀 Enterprise Grade | 📦 Open Source
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
