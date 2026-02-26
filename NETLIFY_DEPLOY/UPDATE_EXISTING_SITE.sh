#!/bin/bash

echo "========================================"
echo "Update Existing Netlify Site"
echo "https://pwd-tools-priyanka.netlify.app"
echo "========================================"
echo ""

echo "Checking Netlify CLI..."
if ! command -v netlify &> /dev/null; then
    echo "ERROR: Netlify CLI not found!"
    echo ""
    echo "Please install it first:"
    echo "  npm install -g netlify-cli"
    echo ""
    exit 1
fi

echo "Netlify CLI found!"
echo ""

echo "Logging in to Netlify..."
netlify login

echo ""
echo "Linking to existing site: pwd-tools-priyanka"
netlify link --name pwd-tools-priyanka

echo ""
echo "Deploying updates to production..."
netlify deploy --prod --dir=.

echo ""
echo "========================================"
echo "Update Complete!"
echo "========================================"
echo ""
echo "Your site has been updated at:"
echo "https://pwd-tools-priyanka.netlify.app"
echo ""
