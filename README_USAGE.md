# 🏗️ PWD Tools Suite - Usage Guide

## 🌐 Online Access

**Visit:** https://pwd-tools-priyanka.netlify.app

Beautiful landing page with information about all tools.

## 💻 Local Usage (Windows)

### Option 1: Launch Single Tool (Recommended)

Double-click: **LAUNCH_SINGLE_TOOL.bat**

- Shows menu with all 13 tools
- Select tool number (1-13)
- Tool opens in browser
- Simple and easy!

### Option 2: Launch All Tools at Once

Double-click: **LAUNCH_ALL_TOOLS.bat**

- Opens all 13 tools simultaneously
- Each tool in separate browser tab
- Each tool on different port (8501-8513)
- Requires more system resources

### Option 3: Run Individual Tool Manually

Open Command Prompt and run:

```bash
streamlit run tools/bill_generator_enterprise.py
```

Replace with any tool filename from the `tools/` folder.

## 📋 All 13 Tools

1. **Bill Generator Enterprise** - Complete bill packages
2. **Excel to EMD** - Batch EMD receipt generation
3. **EMD Refund Calculator** - Calculate refunds with penalties
4. **Security Refund** - Security deposit calculations
5. **Bill Note Sheet** - Note sheets with LD calculation
6. **Deductions Table** - TDS and security deductions
7. **Financial Progress** - Project progress tracking
8. **APG Calculator** - 50% savings calculation
9. **Delay Calculator** - Project delay calculations
10. **Stamp Duty** - Stamp duty calculator
11. **Hand Receipt (RPWA 28)** - RPWA 28 receipts
12. **User Manual** - Bilingual manual (English/Hindi)
13. **Main BAT Info** - Launcher information

## 🚀 For Deployment

### Streamlit Cloud (Recommended)

1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Connect repository
4. Deploy individual tools or main app

### Netlify (Static Landing Page Only)

- Already deployed at https://pwd-tools-priyanka.netlify.app
- Shows information and links
- Cannot run Streamlit apps (needs Python server)

## 🛠️ Requirements

- Python 3.9+
- Streamlit installed: `pip install streamlit`
- All dependencies: `pip install -r requirements.txt`

## 📞 Support

**Prepared on Initiative of:**
Mrs. Premlata Jain, AAO
PWD Udaipur, Rajasthan

**AI Development Partner:** Kiro AI Assistant

---

**Version:** 2.0
**Status:** ✅ Production Ready
**Total Tools:** 13
