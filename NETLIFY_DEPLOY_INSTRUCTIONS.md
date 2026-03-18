# 🚀 Netlify Deployment Instructions

## Your Netlify Site
**URL:** https://pwd-tools-priyanka.netlify.app

## Quick Deploy to Update Your Site

### Option 1: Using Netlify CLI (Recommended)

1. **Install Netlify CLI** (one-time setup):
```bash
npm install -g netlify-cli
```

2. **Login to Netlify**:
```bash
netlify login
```

3. **Deploy from NETLIFY_DEPLOY folder**:
```bash
cd NETLIFY_DEPLOY
netlify deploy --prod
```

### Option 2: Using Netlify Web Interface

1. Go to https://app.netlify.com
2. Login to your account
3. Find your site: **pwd-tools-priyanka**
4. Click **Deploys** tab
5. Drag and drop the **NETLIFY_DEPLOY** folder
6. Wait for deployment to complete

### Option 3: Using Git (If connected to GitHub)

1. Commit your changes:
```bash
git add .
git commit -m "Updated PWD Tools Suite"
git push
```

2. Netlify will auto-deploy from your repository

## What's Included in NETLIFY_DEPLOY

✅ **app.py** - Main application with all 13 tools
✅ **tools/** - All 13 tool files
✅ **core/** - All core modules and utilities
✅ **config/** - Configuration files
✅ **templates/** - HTML templates
✅ **static/** - Static HTML files
✅ **requirements.txt** - Python dependencies
✅ **runtime.txt** - Python version
✅ **packages.txt** - System packages
✅ **setup.sh** - Setup script
✅ **netlify.toml** - Netlify configuration
✅ **Procfile** - Process configuration
✅ **index.html** - Landing page

## All 13 Tools Available

1. 🏗️ Bill Generator Enterprise
2. 📊 Excel to EMD
3. 💸 EMD Refund Calculator
4. 🔒 Security Refund
5. 📝 Bill Note Sheet
6. ➖ Deductions Table
7. 📈 Financial Progress
8. 🧮 APG Calculator
9. ⏱️ Delay Calculator
10. ⚖️ Stamp Duty
11. 🧾 Hand Receipt (RPWA 28)
12. 📖 User Manual
13. ℹ️ Main BAT Info

## How Tools Work on Netlify

Each tool runs independently. Users can:
- Access the main app at your Netlify URL
- Each tool is a separate page/section
- All tools share the same deployment
- No need to run multiple servers

## Testing Locally Before Deploy

```bash
cd NETLIFY_DEPLOY
streamlit run app.py
```

Open http://localhost:8501 to test

## Troubleshooting

**Issue:** Site not loading
- Check Netlify deploy logs
- Verify all files are in NETLIFY_DEPLOY folder
- Check requirements.txt has all dependencies

**Issue:** Tools not working
- Verify Python version in runtime.txt (3.9)
- Check system packages in packages.txt
- Review setup.sh execution logs

## Support

For issues with:
- **Netlify deployment:** Check https://docs.netlify.com
- **Streamlit apps:** Check https://docs.streamlit.io
- **This project:** Review logs in Netlify dashboard

---

**Status:** ✅ Ready for deployment
**Last Updated:** 2026-02-27
**Version:** 2.0
