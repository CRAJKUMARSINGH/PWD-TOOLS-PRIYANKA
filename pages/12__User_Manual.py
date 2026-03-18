"""
User Manual - Bilingual Guide
Standalone deployable tool
Run: streamlit run tools/user_manual.py
"""

import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from utils.branding import apply_custom_css
    from utils.navigation import create_breadcrumb, create_back_button
    has_utils = True
except ImportError:
    has_utils = False

st.set_page_config(
    page_title="User Manual | PWD Tools Suite",
    page_icon="📖",
    layout="wide"
)

if has_utils:
    apply_custom_css()
    create_breadcrumb("User Manual")

def main():
    st.markdown("## 📖 PWD Tools Suite - User Manual")
    st.markdown("### उपयोगकर्ता मैनुअल")
    
    # Language selection
    lang = st.radio("Select Language / भाषा चुनें", ["English", "हिंदी"], horizontal=True)
    
    st.markdown("---")
    
    if lang == "English":
        show_english_manual()
    else:
        show_hindi_manual()
    
    if has_utils:
        st.markdown("---")
        create_back_button()

def show_english_manual():
    st.markdown("""
    ## Welcome to PWD Tools Suite
    
    ### 🎯 Overview
    PWD Tools Suite is a comprehensive collection of 15 professional tools designed for Public Works Department operations.
    
    ### 📦 Tool Categories
    
    #### 💰 Financial Tools (6 tools)
    1. **Excel to EMD** - Generate EMD refund receipts from Excel files
    2. **EMD Refund Calculator** - Calculate EMD refunds with penalties
    3. **Security Refund** - Security deposit refund calculator
    4. **Bill Note Sheet** - Generate bill note sheets with LD calculation
    5. **Deductions Table** - Calculate TDS and security deductions
    6. **Financial Progress** - Track financial progress of projects
    
    #### 🧮 Calculators (3 tools)
    7. **APG Calculator** - 50% of savings beyond -15% below G-Schedule
    8. **Delay Calculator** - Calculate project delays and extensions
    9. **Stamp Duty** - Calculate stamp duty for documents
    
    #### 📋 Document Generators (2 tools)
    10. **Hand Receipt (RPWA 28)** - Generate RPWA 28 compliant receipts
    11. **Excel to EMD Web** - Web-based EMD receipt generator
    
    #### 📊 Tracking & Reports (2 tools)
    12. **Bill Deviation** - Track bill deviations
    13. **Tender Processing** - Comprehensive tender management
    
    #### 🔧 Utilities (2 tools)
    14. **Main BAT Info** - Information about launcher program
    15. **User Manual** - This bilingual guide
    
    ### 🚀 How to Use
    
    #### Running the Full Suite
    ```bash
    streamlit run app.py
    ```
    
    #### Running Individual Tools
    ```bash
    streamlit run tools/bill_note_sheet.py
    streamlit run tools/emd_refund.py
    # ... any other tool
    ```
    
    ### 💡 Key Features
    
    - **Independent Deployment**: Each tool can run standalone
    - **Unified Interface**: All tools share consistent design
    - **Bilingual Support**: Hindi and English interfaces
    - **Professional Output**: Print-ready documents
    - **PWD Compliant**: Follows PWD rules and regulations
    
    ### 📝 Bill Note Sheet with LD Calculation
    
    The Bill Note Sheet tool includes full Liquidated Damages calculation using the PWD Quarterly Distribution Method:
    
    - **Q1 (12.5% work)**: 2.5% penalty
    - **Q2 (25% work)**: 5% penalty
    - **Q3 (25% work)**: 7.5% penalty
    - **Q4 (37.5% work)**: 10% penalty
    
    **Formula**: LD = Penalty Rate × Unexecuted Work
    
    ### 🔒 Security & Privacy
    
    - All processing happens locally
    - No data sent to external servers
    - Your files remain on your computer
    
    ### 📞 Support
    
    For questions or issues, contact:
    - **Initiative**: Mrs. Premlata Jain, AAO
    - **Department**: PWD Udaipur, Rajasthan
    
    ### 🤖 Development
    
    Developed with AI assistance from Kiro AI Assistant
    """)

def show_hindi_manual():
    st.markdown("""
    ## PWD टूल्स सूट में आपका स्वागत है
    
    ### 🎯 अवलोकन
    PWD टूल्स सूट लोक निर्माण विभाग के संचालन के लिए डिज़ाइन किए गए 15 पेशेवर उपकरणों का एक व्यापक संग्रह है।
    
    ### 📦 उपकरण श्रेणियां
    
    #### 💰 वित्तीय उपकरण (6 उपकरण)
    1. **Excel से EMD** - Excel फ़ाइलों से EMD रिफंड रसीदें बनाएं
    2. **EMD रिफंड कैलकुलेटर** - जुर्माने के साथ EMD रिफंड की गणना करें
    3. **सुरक्षा रिफंड** - सुरक्षा जमा रिफंड कैलकुलेटर
    4. **बिल नोट शीट** - LD गणना के साथ बिल नोट शीट बनाएं
    5. **कटौती तालिका** - TDS और सुरक्षा कटौती की गणना करें
    6. **वित्तीय प्रगति** - परियोजनाओं की वित्तीय प्रगति ट्रैक करें
    
    #### 🧮 कैलकुलेटर (3 उपकरण)
    7. **APG कैलकुलेटर** - G-Schedule से -15% से अधिक बचत का 50%
    8. **विलंब कैलकुलेटर** - परियोजना विलंब और विस्तार की गणना करें
    9. **स्टाम्प ड्यूटी** - दस्तावेजों के लिए स्टाम्प ड्यूटी की गणना करें
    
    #### 📋 दस्तावेज़ जनरेटर (2 उपकरण)
    10. **हैंड रसीद (RPWA 28)** - RPWA 28 अनुरूप रसीदें बनाएं
    11. **Excel से EMD वेब** - वेब-आधारित EMD रसीद जनरेटर
    
    #### 📊 ट्रैकिंग और रिपोर्ट (2 उपकरण)
    12. **बिल विचलन** - बिल विचलन ट्रैक करें
    13. **टेंडर प्रोसेसिंग** - व्यापक टेंडर प्रबंधन
    
    #### 🔧 उपयोगिताएँ (2 उपकरण)
    14. **Main BAT Info** - लॉन्चर प्रोग्राम के बारे में जानकारी
    15. **उपयोगकर्ता मैनुअल** - यह द्विभाषी गाइड
    
    ### 🚀 उपयोग कैसे करें
    
    #### पूर्ण सूट चलाना
    ```bash
    streamlit run app.py
    ```
    
    #### व्यक्तिगत उपकरण चलाना
    ```bash
    streamlit run tools/bill_note_sheet.py
    streamlit run tools/emd_refund.py
    # ... कोई अन्य उपकरण
    ```
    
    ### 💡 मुख्य विशेषताएं
    
    - **स्वतंत्र तैनाती**: प्रत्येक उपकरण स्वतंत्र रूप से चल सकता है
    - **एकीकृत इंटरफ़ेस**: सभी उपकरण सुसंगत डिज़ाइन साझा करते हैं
    - **द्विभाषी समर्थन**: हिंदी और अंग्रेजी इंटरफेस
    - **पेशेवर आउटपुट**: प्रिंट-तैयार दस्तावेज़
    - **PWD अनुरूप**: PWD नियमों और विनियमों का पालन करता है
    
    ### 📝 LD गणना के साथ बिल नोट शीट
    
    बिल नोट शीट उपकरण में PWD त्रैमासिक वितरण विधि का उपयोग करके पूर्ण Liquidated Damages गणना शामिल है:
    
    - **Q1 (12.5% कार्य)**: 2.5% जुर्माना
    - **Q2 (25% कार्य)**: 5% जुर्माना
    - **Q3 (25% कार्य)**: 7.5% जुर्माना
    - **Q4 (37.5% कार्य)**: 10% जुर्माना
    
    **सूत्र**: LD = जुर्माना दर × अनिष्पादित कार्य
    
    ### 🔒 सुरक्षा और गोपनीयता
    
    - सभी प्रोसेसिंग स्थानीय रूप से होती है
    - बाहरी सर्वर को कोई डेटा नहीं भेजा जाता
    - आपकी फ़ाइलें आपके कंप्यूटर पर रहती हैं
    
    ### 📞 सहायता
    
    प्रश्नों या समस्याओं के लिए संपर्क करें:
    - **पहल**: श्रीमती प्रेमलता जैन, AAO
    - **विभाग**: PWD उदयपुर, राजस्थान
    
    ### 🤖 विकास
    
    Kiro AI Assistant से AI सहायता के साथ विकसित
    """)

if __name__ == "__main__":
    main()
