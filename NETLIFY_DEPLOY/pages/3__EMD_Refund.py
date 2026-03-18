import streamlit as st
import streamlit.components.v1 as components
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button

# Page configuration
st.set_page_config(
    page_title="EMD Refund | PWD Tools Hub",
    page_icon="💰",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("EMD Refund")

def main():
    # Custom CSS for magenta buttons
    st.markdown("""
    <style>
    .magenta-btn {
        background-color: #FF00FF !important;
        color: white !important;
        border: none !important;
        padding: 10px 20px !important;
        text-align: center !important;
        text-decoration: none !important;
        display: inline-block !important;
        font-size: 16px !important;
        margin: 4px 2px !important;
        cursor: pointer !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
        transition: all 0.3s !important;
    }
    
    .magenta-btn:hover {
        background-color: #CC00CC !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(0,0,0,0.3) !important;
    }
    
    .info-box {
        background-color: #f8f0fa;
        border-left: 5px solid #FF00FF;
        padding: 15px;
        border-radius: 5px;
        margin: 20px 0;
    }
    
    .page-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    
    @media print {
        /* Hide all Streamlit elements when printing */
        .stApp > header, .stApp > .stToolbar, .stApp > .stDeployButton, 
        .stMarkdown, .stButton, .stHorizontalBlock, hr, .info-box {
            display: none !important;
        }
        
        /* Only show the receipt content */
        iframe {
            width: 100% !important;
            height: 100% !important;
            border: none !important;
        }
        
        body, html {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        /* Ensure iframe content is visible for printing */
        iframe {
            display: block !important;
        }
    }
    
    /* Additional print CSS to ensure content visibility */
    @media print {
        .stApp {
            visibility: hidden;
        }
        
        .stApp > div[data-baseweb="modal"] {
            visibility: visible;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
    }
    
    /* Ensure proper PDF download experience */
    .download-notification {
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: #4CAF50;
        color: white;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        z-index: 9999;
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Notification for PDF download
    st.markdown('<div class="download-notification" id="download-notification">PDF downloaded successfully!</div>', unsafe_allow_html=True)
    
    # Read and display the HTML content at full width
    try:
        with open("static/html/EmdRefund.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Display the HTML content centered with wide width
        col_left, col_center, col_right = st.columns([1, 10, 1])
        with col_center:
            receipt_component = components.html(html_content, height=800, scrolling=True, width=1200)

    except FileNotFoundError:
        st.error("Tool not available")

    # Add instructions for the user with magenta buttons
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="info-box"><h3>💡 How to Use This Tool</h3>', unsafe_allow_html=True)
        st.markdown("""
        <ol>
            <li>Fill in the payee name, amount, and work name in the form</li>
            <li>Click <strong>Generate Receipt</strong> to create the receipt</li>
            <li>PDF will be automatically downloaded to your default download folder</li>
            <li>Use the <strong>Print Receipt</strong> button in the form to print</li>
            <li>Only the first page (the receipt) will be printed</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        
        # Add magenta button for printing
        if st.button("🖨️ Print Receipt", key="print_receipt", help="Print the generated receipt"):
            st.markdown("""
            <script>
            // Find the iframe containing the receipt and trigger its print function
            setTimeout(function() {
                const iframes = document.getElementsByTagName('iframe');
                for (let i = 0; i < iframes.length; i++) {
                    try {
                        if (iframes[i].contentWindow.document.getElementById('receipt-content')) {
                            // Click the print button inside the iframe
                            const printButton = iframes[i].contentWindow.document.getElementById('print-button');
                            if (printButton) {
                                printButton.click();
                            } else {
                                // Fallback to window.print if button not found
                                iframes[i].contentWindow.print();
                            }
                            break;
                        }
                    } catch (e) {
                        // Cross-origin restrictions, fall back to window print
                        window.print();
                        break;
                    }
                }
            }, 1500);
            </script>
            """, unsafe_allow_html=True)
            
        # Add magenta button for downloading PDF
        if st.button("💾 Download PDF", key="download_pdf", help="Download the receipt as PDF to your download folder"):
            st.markdown("""
            <script>
            // Find the iframe containing the receipt and trigger its PDF download function
            setTimeout(function() {
                const iframes = document.getElementsByTagName('iframe');
                for (let i = 0; i < iframes.length; i++) {
                    try {
                        if (iframes[i].contentWindow.document.getElementById('receipt-content')) {
                            // Trigger the download button in the iframe
                            const downloadButton = iframes[i].contentWindow.document.getElementById('download-button');
                            if (downloadButton) {
                                downloadButton.click();
                                
                                // Show notification
                                const notification = document.getElementById('download-notification');
                                if (notification) {
                                    notification.style.display = 'block';
                                    setTimeout(function() {
                                        notification.style.display = 'none';
                                    }, 3000);
                                }
                            }
                            break;
                        }
                    } catch (e) {
                        // Cross-origin restrictions
                        alert("Unable to automatically download PDF. Please use the download button in the receipt form.");
                        break;
                    }
                }
            }, 1000);
            </script>
            """, unsafe_allow_html=True)
            
        # Add magenta button for opening HTML file directly
        if st.button("📄 Open Receipt Generator", key="open_html", help="Open the HTML receipt generator in a new tab"):
            st.markdown("""
            <script>
            window.open('./static/html/EmdRefund.html', '_blank');
            </script>
            """, unsafe_allow_html=True)

# Navigation with magenta button
def create_back_button():
    """Create a back to home button with magenta color"""
    st.markdown('<div style="text-align: center; margin: 20px 0;">', unsafe_allow_html=True)
    if st.button("🏠 Back to Home", key="back_home", type="secondary"):
        st.switch_page("app.py")
    st.markdown('</div>', unsafe_allow_html=True)

# Create navigation
create_back_button()

# Run main function
if __name__ == "__main__":
    main()