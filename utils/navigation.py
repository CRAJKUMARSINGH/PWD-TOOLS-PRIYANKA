import streamlit as st

def create_breadcrumb(current_page):
    """Create breadcrumb navigation"""
    st.markdown(f"""
    <div style="background-color: #f0f8f5; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
        <span style="color: #2E8B57;">🏠 <a href="/" style="color: #2E8B57; text-decoration: none;">Home</a></span>
        <span style="color: #666;"> → </span>
        <span style="color: #333; font-weight: bold;">{current_page}</span>
    </div>
    """, unsafe_allow_html=True)

def create_back_button():
    """Create a back to home button"""
    if st.button("🏠 Back to Home", key="back_home", type="primary"):
        st.switch_page("app.py")

def create_tool_navigation():
    """Create navigation between tools"""
    st.sidebar.markdown("### 🧭 Tool Navigation")
    
    tools = {
        "📊 Excel se EMD": "pages/01_Excel_se_EMD.py",
        "💰 Bill & Deviation": "pages/02_Bill_Deviation.py", 
        "📋 Tender Processing": "pages/03_Tender_Processing.py",
        "📝 Bill Note Sheet": "pages/04_Bill_Note_Sheet.py",
        "📋 Deductions Table": "pages/05_Deductions_Table.py",
        "💳 EMD Refund": "pages/07_EMD_Refund.py",
        "📈 Financial Progress": "pages/08_Financial_Progress.py",
        "🛡️ Security Refund": "pages/09_Security_Refund.py",
        ".stamp Duty": "pages/10_Stamp_Duty.py",
        "🧾 Hand Receipt Generator": "pages/11_Hand_Receipt_Generator.py"
    }
    
    for tool_name, tool_page in tools.items():
        if st.sidebar.button(tool_name, key=f"nav_{tool_name}", use_container_width=True):
            st.switch_page(tool_page)

def show_external_link_warning():
    """Show warning for external links"""
    st.warning("""
    🔗 **External Tool Access**
    
    You are being redirected to an external PWD tool. This tool is hosted separately but integrated into our hub.
    
    - All tools maintain the same security standards
    - Your session data is protected
    - Use the browser back button to return here
    """)