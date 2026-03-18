# 🏗️ PWD Tools Suite v2.0

**Professional Infrastructure Management Tools for Public Works Department**

![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Tools](https://img.shields.io/badge/Tools-13-blue)
![Version](https://img.shields.io/badge/Version-2.0-orange)

## 🌟 Features

✨ **Unified Interface** - All 13 tools in one seamless application
🎨 **Beautiful Design** - Colorful gradient cards with smooth animations
🚀 **Fast & Responsive** - Optimized performance
📱 **Mobile Friendly** - Works on all devices
🔧 **Production Ready** - Fully tested and stable
⚡ **Easy to Use** - Intuitive navigation

## 🚀 Quick Start

### Run Locally

**Windows:**
```bash
# Double-click
START_APP.bat

# Or run manually
streamlit run Home.py
```

**Mac/Linux:**
```bash
streamlit run Home.py
```

Opens at: http://localhost:8501

### Deploy to Cloud (FREE)

1. Push to GitHub
2. Go to https://share.streamlit.io
3. Connect repository and deploy `Home.py`
4. Get your live URL!

## 📋 All 13 Tools

| Icon | Tool | Description |
|------|------|-------------|
| 🏗️ | **Bill Generator Enterprise** | Complete bill package with all documents and PDFs |
| 📊 | **Excel to EMD** | Generate EMD receipts from Excel (batch processing) |
| 💸 | **EMD Refund Calculator** | Calculate EMD refunds with penalties |
| 🔒 | **Security Refund** | Security deposit refund calculator |
| 📝 | **Bill Note Sheet** | Hindi Bill Note Sheet Generator - Pure HTML/CSS/JS (Better than React!) |
| ➖ | **Deductions Table** | Calculate TDS and security deductions |
| 📈 | **Financial Progress** | Track financial progress of projects |
| 🧮 | **APG Calculator** | 50% of savings beyond -15% below G-Schedule |
| ⏱️ | **Delay Calculator** | Calculate project delays and extensions |
| ⚖️ | **Stamp Duty** | Calculate stamp duty for documents |
| 🧾 | **Hand Receipt** | Generate RPWA 28 compliant hand receipts |
| 📖 | **User Manual** | Bilingual user manual (English/Hindi) |
| ℹ️ | **Main Info** | Information about the application |

## 🎨 Screenshots

**Home Page:**
- Beautiful colorful gradient cards for each tool
- Professional header with gradient background
- Statistics dashboard
- Easy navigation

**Tool Pages:**
- Clean, intuitive interface
- Sidebar navigation to switch between tools
- Consistent design across all tools

## 🛠️ Installation

### Requirements
- Python 3.9 or higher
- pip (Python package manager)

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Main Dependencies
- streamlit
- pandas
- openpyxl
- python-docx
- reportlab
- jinja2
- Pillow

## 📁 Project Structure

```
PWD-Tools-Suite/
├── Home.py                 # Main application entry point
├── pages/                  # All 13 tool pages
│   ├── 1_🏗️_Bill_Generator.py
│   ├── 2_📊_Excel_to_EMD.py
│   ├── 3_💸_EMD_Refund.py
│   ├── 4_🔒_Security_Refund.py
│   ├── 5_📝_Bill_Note_Sheet.py
│   ├── 6_➖_Deductions_Table.py
│   ├── 7_📈_Financial_Progress.py
│   ├── 8_🧮_APG_Calculator.py
│   ├── 9_⏱️_Delay_Calculator.py
│   ├── 10_⚖️_Stamp_Duty.py
│   ├── 11_🧾_Hand_Receipt.py
│   ├── 12_📖_User_Manual.py
│   └── 13_ℹ️_Main_Info.py
├── tools/                  # Original standalone tool files
├── core/                   # Core modules and utilities
├── config/                 # Configuration files
├── templates/              # HTML templates
├── static/                 # Static files
├── OUTPUT/                 # Generated output files
├── requirements.txt        # Python dependencies
├── START_APP.bat          # Windows launcher
└── README.md              # This file
```

## 🌐 Deployment Options

### 1. Streamlit Cloud (Recommended - FREE)
- Push to GitHub
- Deploy at https://share.streamlit.io
- Automatic HTTPS and updates
- Perfect for Streamlit apps

### 2. Local Server
- Run `streamlit run Home.py`
- Access on local network
- Full control

### 3. Docker
- Use provided Dockerfile
- Deploy anywhere
- Containerized solution

## 📖 Usage Guide

1. **Launch the app** using `START_APP.bat` or `streamlit run Home.py`
2. **Home page** displays all 13 tools with colorful cards
3. **Click any tool** in the sidebar to access it
4. **Use the tool** - each has its own interface
5. **Navigate easily** between tools using sidebar
6. **Download outputs** from the OUTPUT folder

## 🎯 Key Improvements in v2.0

✅ Unified interface - all tools in one app
✅ Beautiful colorful design with gradients
✅ Streamlit multipage architecture
✅ Smooth animations and hover effects
✅ Professional statistics dashboard
✅ Easy sidebar navigation
✅ Production-ready deployment
✅ Clean code structure
✅ Comprehensive documentation

## 🔧 Configuration

Configuration files are in the `config/` directory:
- `v01.json` - Main configuration file
- Modify as needed for your requirements

## 📊 Output Files

Generated files are saved in the `OUTPUT/` folder:
- Bills (HTML, PDF, DOCX)
- Receipts
- Certificates
- Reports
- All downloadable from the app

## 🤝 Contributing

This is a production application for PWD Udaipur. For modifications or enhancements, please contact the development team.

## 📞 Support & Credits

**Prepared on Initiative of:**
- **Mrs. Premlata Jain, AAO**
- Public Works Department
- Udaipur, Rajasthan

**AI Development Partner:**
- Kiro AI Assistant

**Technology Stack:**
- Python 3.9+
- Streamlit (Web Framework)
- Pandas (Data Processing)
- ReportLab (PDF Generation)
- Jinja2 (Templating)

## 📄 License

Proprietary - Public Works Department, Udaipur, Rajasthan

## 🔄 Version History

### v2.0.1 (March 18, 2026 - Morning Update)
- ✅ **Hindi Bill Note Sheet** - Complete rewrite in pure HTML/CSS/JavaScript
- ✅ Better than React version - faster, simpler, more beautiful
- ✅ M/s. auto-prefix for contractor names
- ✅ Conditional extra item amount field (only shows when needed)
- ✅ Simplified UI for semi-literate users (removed confusing messages)
- ✅ Only Dep-V shown in deductions input (all others auto-calculated)
- ✅ Floating balloons animation
- ✅ Live preview with exact formatting
- ✅ Auto-generated Hindi notes (10 points)
- ✅ Print function with A4 margins

### v2.0 (Current)
- Unified multipage application
- Beautiful colorful interface
- All 13 tools integrated
- Production-ready deployment
- Enhanced user experience

### v1.0
- Individual standalone tools
- Basic functionality
- Command-line launchers

---

**Status:** ✅ Production Ready | **Version:** 2.0 | **Tools:** 13 | **Architecture:** Streamlit Multipage App

**Live Demo:** Coming soon on Streamlit Cloud
**Landing Page:** https://pwd-tools-priyanka.netlify.app

Made with ❤️ for PWD Udaipur
