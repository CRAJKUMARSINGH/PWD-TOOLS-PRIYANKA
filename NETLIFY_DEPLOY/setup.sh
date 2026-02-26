#!/bin/bash

# Netlify Setup Script for PWD Tools Suite
# This script prepares the environment for Streamlit deployment on Netlify

echo "Setting up PWD Tools Suite for Netlify..."

# Create necessary directories
mkdir -p ~/.streamlit/

# Create Streamlit config
echo "\
[general]\n\
email = \"\"\n\
\n\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = 8501\n\
\n\
[theme]\n\
primaryColor = \"#FF00FF\"\n\
backgroundColor = \"#FFFFFF\"\n\
secondaryBackgroundColor = \"#F0F2F6\"\n\
textColor = \"#262730\"\n\
font = \"sans serif\"\n\
" > ~/.streamlit/config.toml

echo "Setup complete!"
