# 🏗️ PWD Tools Suite v2.0

**Professional Infrastructure Management Tools for Public Works Department**

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://pwd-tools-priyanka.streamlit.app)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)]()
[![Tools](https://img.shields.io/badge/Tools-13-blue)]()
[![Version](https://img.shields.io/badge/Version-2.0.1-orange)]()

## 🌟 Quick Access

**🚀 Live App:** https://pwd-tools-priyanka.streamlit.app  
**📄 Landing Page:** https://pwd-tools-priyanka.netlify.app

## ✨ Features

- 🎨 **Beautiful UI** - Gradient cards with smooth animations
- 🚀 **13 Professional Tools** - All in one unified interface
- ⚡ **Fast & Responsive** - Optimized performance
- 📱 **Mobile Friendly** - Works on all devices
- 🎈 **Interactive** - Welcome balloons and celebrations
- 🔧 **Production Ready** - Fully tested and stable

## 📋 All 13 Tools

| Tool | Description |
|------|-------------|
| 🏗️ **Bill Generator** | Complete bill package with all documents and PDFs |
| 📊 **Excel to EMD** | Generate EMD receipts from Excel (batch processing) |
| 💸 **EMD Refund** | Calculate EMD refunds with penalties |
| 🔒 **Security Refund** | Security deposit refund calculator |
| 📝 **Bill Note Sheet** | Generate bill note sheets with LD calculation |
| ➖ **Deductions Table** | Calculate TDS and security deductions |
| 📈 **Financial Progress** | Track financial progress of projects |
| 🧮 **APG Calculator** | Calculate APG values (50% savings beyond -15%) |
| ⏱️ **Delay Calculator** | Calculate project delays and extensions |
| ⚖️ **Stamp Duty** | Calculate stamp duty for documents |
| 🧾 **Hand Receipt** | Generate RPWA 28 compliant hand receipts |
| 📖 **User Manual** | Bilingual user manual (English/Hindi) |
| ℹ️ **Main Info** | Information about the application |

## 🚀 Quick Start

### Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Opens at: http://localhost:8501

### Deploy to Streamlit Cloud (FREE)

1. Fork this repository
2. Go to https://share.streamlit.io
3. Connect your GitHub account
4. Select this repository
5. Set main file: `app.py`
6. Click Deploy!

Your app will be live at: `https://your-username-pwd-tools.streamlit.app`

## 🛠️ Installation

### Requirements
- Python 3.11+
- pip (Python package manager)

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Main Dependencies
- streamlit - Web framework
- pandas - Data processing
- openpyxl - Excel handling
- python-docx - Word documents
- reportlab - PDF generation
- jinja2 - Templating
- Pillow - Image processing

## 📁 Project Structure

```
PWD-Tools-Suite/
├── app.py                  # Main application
├── Home.py                 # Alternative entry point
├── pages/                  # All 13 tool pages
│   ├── 1__Bill_Generator.py
│   ├── 2__Excel_to_EMD.py
│   └── ... (11 more tools)
├── tools/                  # Standalone tool files
├── core/                   # Core modules
├── templates/              # HTML templates
├── static/                 # Static files
├── .streamlit/             # Streamlit config
│   └── config.toml
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## 📖 How to Use

### Online (Recommended)
1. Visit https://pwd-tools-priyanka.streamlit.app
2. Click any tool from the beautiful landing page
3. Use the tool - each has its own intuitive interface
4. Download generated files

### Locally
1. Run `streamlit run app.py`
2. Browser opens automatically
3. Navigate using sidebar or main page buttons
4. All outputs saved in OUTPUT folder

## 🎨 UI Features

- 🎈 **Welcome Balloons** - Automatic on first visit
- 🌈 **Gradient Cards** - Beautiful colorful tool cards
- ✨ **Smooth Animations** - Hover effects and transitions
- 📊 **Quick Stats** - 13 Tools, Production Ready, Fast Performance
- 🎯 **Easy Navigation** - Sidebar + main page buttons
- 💫 **Elegant Buttons** - White with purple gradient on hover

## 🌐 Deployment Options

### 1. Streamlit Cloud (Recommended - FREE)
- ✅ Best for Streamlit apps
- ✅ Automatic HTTPS
- ✅ Auto-updates from GitHub
- ✅ Free forever
- 📍 Deploy at: https://share.streamlit.io

### 2. Local Server
- Run on your computer
- Access on local network
- Full control

### 3. Docker
```bash
docker build -t pwd-tools .
docker run -p 8501:8501 pwd-tools
```

## 📊 Test Results

- ✅ **100% Test Pass Rate**
- ✅ **Real Data Tested** - 811 rows from actual Excel files
- ✅ **All Tools Verified** - Working perfectly
- ✅ **Production Ready** - Stable and reliable

## 🤝 Credits

**Prepared on Initiative of:**
- **Mrs. Premlata Jain, AAO**
- Public Works Department
- Udaipur, Rajasthan

**AI Development Partner:**
- Kiro AI Assistant

**Technology Stack:**
- Python 3.11+
- Streamlit (Web Framework)
- Pandas (Data Processing)
- ReportLab (PDF Generation)
- Jinja2 (Templating)

## 📄 License

Proprietary - Public Works Department, Udaipur, Rajasthan

## 🔄 Version History

### v2.0.1 (March 18, 2026)
- ✅ Beautiful landing page with gradient cards
- ✅ Elegant sidebar navigation
- ✅ Welcome balloons and celebrations
- ✅ Quick stats display
- ✅ Smooth animations and hover effects
- ✅ Deployed to Streamlit Cloud
- ✅ Production ready

### v2.0
- Unified multipage application
- All 13 tools integrated
- Professional UI design

### v1.0
- Individual standalone tools
- Basic functionality

---

**Status:** ✅ Production Ready | **Version:** 2.0.1 | **Tools:** 13

**Live Demo:** https://pwd-tools-priyanka.streamlit.app

Made with ❤️ for PWD Udaipur
