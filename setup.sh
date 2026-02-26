#!/bin/bash

# PWD Tools Suite - Setup Script for Streamlit Cloud

# Create necessary directories
mkdir -p ~/.streamlit/

# Create Streamlit config
echo "\
[general]\n\
email = \"premlata.jain@pwd.rajasthan.gov.in\"\n\
\n\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = \$PORT\n\
\n\
[theme]\n\
primaryColor = \"#667eea\"\n\
backgroundColor = \"#f5f7fa\"\n\
secondaryBackgroundColor = \"#e8ecf1\"\n\
textColor = \"#2d3436\"\n\
font = \"sans serif\"\n\
" > ~/.streamlit/config.toml

# Create credentials file (if needed)
echo "\
[general]\n\
email = \"premlata.jain@pwd.rajasthan.gov.in\"\n\
" > ~/.streamlit/credentials.toml
