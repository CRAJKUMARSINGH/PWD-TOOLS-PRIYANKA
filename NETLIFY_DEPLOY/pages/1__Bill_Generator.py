"""
Bill Generator Enterprise - Full Featured Bill Generation System
Integrated from BillGeneratorUnified
Standalone deployable tool
Run: streamlit run tools/bill_generator_enterprise.py
"""

import os
import sys
from pathlib import Path
import streamlit as st
import shutil

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import utilities
try:
    from core.utils.cache_cleaner import CacheCleaner
    from core.utils.output_manager import get_output_manager
    from core.config.config_loader import ConfigLoader
    has_core = True
except ImportError:
    has_core = False
    st.error("Core modules not found. Please ensure BillGeneratorUnified core is integrated.")

# Page config
st.set_page_config(
    page_title="Bill Generator Enterprise",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Clean cache on startup
if has_core:
    CacheCleaner.clean_cache(verbose=False)

# Load configuration
if has_core:
    config = ConfigLoader.load_from_env('BILL_CONFIG', 'config/v01.json')
else:
    config = None

# Custom CSS with Beautiful Gradient Styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .main-header {
        background: linear-gradient(to right, #667eea, #764ba2, #f093fb);
        padding: 2.5rem 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3rem;
        font-weight: 600;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #764ba2 0%, #f093fb 100%);
    }
</style>
""", unsafe_allow_html=True)

# Header
if config:
    st.markdown(f"""
    <div class="main-header">
        <h1>🏗️ Bill Generator Enterprise</h1>
        <p>✨ Professional Bill Generation System | Version {config.version} | Mode: {config.mode}</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="main-header">
        <h1>🏗️ Bill Generator Enterprise</h1>
        <p>✨ Professional Bill Generation System</p>
    </div>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #00b894 0%, #00cec9 100%); 
                padding: 1.5rem; 
                border-radius: 10px; 
                text-align: center; 
                margin-bottom: 1rem;
                box-shadow: 0 2px 8px rgba(0, 184, 148, 0.3);'>
        <h2 style='color: white; margin: 0; font-size: 1.5rem;'>
            🏗️ Bill Generator
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    # Mode selection
    modes = ["📊 Excel Upload", "💻 Online Entry"]
    
    if config and config.features.is_enabled('batch_processing'):
        modes.append("📦 Batch Processing")
    modes.append("📥 Download Center")
    modes.append("📖 User Manual")
    
    if config and config.features.is_enabled('analytics'):
        modes.append("📈 Analytics")
    
    selected_mode = st.radio("Select Mode", modes)
    
    st.markdown("---")
    
    # Cache cleaning feature
    if has_core:
        st.markdown("### 🧹 Maintenance")
        
        output_mgr = get_output_manager()
        output_size = output_mgr.get_folder_size()
        output_files = len(output_mgr.get_all_files())
        
        if output_size > 0:
            st.info(f"📦 OUTPUT folder: {output_files} files ({output_mgr.format_size(output_size)})")
        
        if st.button("🧹 Clean Cache & Temp Files"):
            with st.spinner("Cleaning cache..."):
                cleaned_dirs, cleaned_files = CacheCleaner.clean_cache(verbose=False)
                if cleaned_dirs or cleaned_files > 0:
                    st.success(f"✅ Cleaned {cleaned_dirs} directories, {cleaned_files} files")
                else:
                    st.info("ℹ️ No cache files found")
        
        if st.button("🗑️ Clean Old Output Files"):
            with st.spinner("Cleaning old files..."):
                files_deleted, space_freed = output_mgr.clean_old_files(keep_latest=10)
                if files_deleted > 0:
                    st.success(f"✅ Deleted {files_deleted} files ({output_mgr.format_size(space_freed)} freed)")
                else:
                    st.info("ℹ️ No old files to clean")
        
        st.markdown("---")
    
    # Feature status
    if config:
        st.markdown("### ✨ Features")
        features_status = {
            "Excel Upload": config.features.excel_upload,
            "Online Entry": config.features.online_entry,
            "Batch Processing": config.features.batch_processing,
            "Advanced PDF": config.features.advanced_pdf,
            "Analytics": config.features.analytics
        }
        
        for feature, enabled in features_status.items():
            if enabled:
                st.markdown(f"""
                <div style='background: linear-gradient(90deg, #d4edda 0%, #c3e6cb 100%); 
                            padding: 0.5rem 1rem; 
                            border-radius: 8px; 
                            margin: 0.3rem 0;
                            border-left: 3px solid #00b894;'>
                    <span style='color: #155724; font-weight: 600;'>✅ {feature}</span>
                </div>
                """, unsafe_allow_html=True)

# Main content
if "📊 Excel Upload" in selected_mode:
    if has_core:
        try:
            from core.ui.excel_mode_fixed import show_excel_mode
            show_excel_mode(config)
        except ImportError as e:
            st.error(f"❌ Excel mode not available: {e}")
    else:
        st.error("Core modules not available")

elif "💻 Online Entry" in selected_mode:
    if has_core:
        try:
            from core.ui.online_mode import show_online_mode
            show_online_mode(config)
        except ImportError:
            st.info("💻 Online entry mode coming soon!")
    else:
        st.error("Core modules not available")

elif "📦 Batch Processing" in selected_mode:
    if has_core:
        try:
            from core.processors.batch_processor_fixed import show_batch_mode
            show_batch_mode(config)
        except ImportError:
            st.error("❌ Batch processing not available")
    else:
        st.error("Core modules not available")

elif "📥 Download Center" in selected_mode:
    if has_core:
        try:
            from core.utils.download_manager import EnhancedDownloadManager
            from core.ui.enhanced_download_center import create_enhanced_download_center
            
            if 'download_manager' not in st.session_state:
                st.session_state.download_manager = EnhancedDownloadManager()
            
            download_center = create_enhanced_download_center(st.session_state.download_manager)
            download_center.render_download_center()
        except ImportError:
            st.error("❌ Download center not available")
    else:
        st.error("Core modules not available")

elif "📈 Analytics" in selected_mode:
    st.markdown("## 📈 Analytics Dashboard")
    st.info("Analytics dashboard coming soon!")

elif "📖 User Manual" in selected_mode:
    st.markdown("## 📖 User Manual / उपयोगकर्ता मैनुअल")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        language = st.radio(
            "Select Language / भाषा चुनें",
            ["🇬🇧 English", "🇮🇳 हिंदी"],
            horizontal=True
        )
    
    st.markdown("---")
    
    st.markdown("""
    ## Bill Generator Enterprise - User Manual
    
    ### Features
    
    1. **Excel Upload Mode**
       - Upload Excel files with bill data
       - Automatic data extraction
       - Generate multiple documents
       - Batch processing support
    
    2. **Online Entry Mode**
       - Manual data entry
       - Real-time validation
       - Step-by-step guidance
    
    3. **Batch Processing**
       - Process multiple bills at once
       - Bulk document generation
       - ZIP download support
    
    4. **Download Center**
       - Access all generated documents
       - Organized by date
       - Easy file management
    
    ### How to Use
    
    #### Excel Upload:
    1. Select "Excel Upload" mode
    2. Upload your Excel file
    3. Map columns if needed
    4. Click "Generate Documents"
    5. Download from Download Center
    
    #### Online Entry:
    1. Select "Online Entry" mode
    2. Fill in project details
    3. Add bill items
    4. Review and generate
    5. Download documents
    
    ### Document Types Generated
    
    - First Page Summary
    - Deviation Statement
    - Bill Scrutiny Sheet (Note Sheet)
    - Certificate II
    - PDF versions of all documents
    
    ### Support
    
    For questions or issues:
    - Mrs. Premlata Jain, AAO
    - PWD Udaipur, Rajasthan
    """)

# Footer
st.markdown("---")
if config:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                padding: 2rem;
                border-radius: 10px;
                text-align: center;
                margin-top: 2rem;
                border-top: 3px solid #00b894;'>
        <p style='font-size: 1.2rem; font-weight: 700; color: #2d3436; margin: 0.5rem 0;'>
            🎯 Bill Generator Enterprise v{config.version}
        </p>
        <p style='color: #636e72; margin: 0.3rem 0; font-size: 0.95rem;'>
            <strong>Prepared on Initiative of:</strong><br>
            <span style='color: #00b894; font-weight: 600;'>Mrs. Premlata Jain, AAO</span><br>
            <span style='font-size: 0.9rem;'>PWD Udaipur</span>
        </p>
        <div style='margin-top: 1rem;'>
            <p style='color: #636e72; font-size: 0.95rem; margin: 0.3rem 0;'>
                <strong>🤖 AI Development Partner:</strong> Kiro AI Assistant
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Main function for Bill Generator Enterprise"""
    # This function is called when the script is run directly
    # All the Streamlit code above executes on import
    pass

if __name__ == "__main__":
    main()


