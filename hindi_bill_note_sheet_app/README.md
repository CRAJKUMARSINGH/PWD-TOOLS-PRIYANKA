# 🌸 Hindi Bill Note Sheet App

## ⚠️ IMPORTANT - DO NOT DELETE THIS FOLDER

This folder contains the complete integrated Hindi Bill Note Sheet React application.

**Used by:** `pages/5__Bill_Note_Sheet.py`

## 📁 Contents

- `index.html` - Main React app entry point
- `assets/index-Co3DCvaa.css` - Complete application styles
- `assets/index-DVx-snOk.js` - Complete React application JavaScript
- `favicon.svg` - App icon
- `opengraph.jpg` - Social media preview image
- `COMPLETE_HINDI_BILL_NOTE_SHEET.html` - Standalone HTML version (backup)
- `_redirects` - Netlify redirects configuration (reference)

## 🎯 Features

- ✅ Bilingual labels (Hindi/English)
- ✅ Live preview with instant updates
- ✅ GST calculation (rounds to higher even number)
- ✅ All deductions (SD 10%, IT 2%, GST 2%, LC 1%)
- ✅ PDF generation with 10mm margins
- ✅ Automated testing suite
- ✅ Sample data loader
- ✅ Beautiful gradient UI
- ✅ React-powered interactive interface

## 🔧 How It Works

The Streamlit page (`pages/5__Bill_Note_Sheet.py`):
1. Reads `index.html`, CSS, and JS files
2. Combines them into one complete standalone HTML
3. Embeds it using `components.html()`
4. Runs the full React app in the browser

## 📝 Source

Built from: `Hindi_Bill_Note_Sheet/artifacts/hindi-bill/dist/`

This is the production build of the React application deployed at:
https://hindibillnote.netlify.app/

## ⚠️ WARNING

**DO NOT DELETE OR RENAME THIS FOLDER**

If you accidentally delete it, you can restore it by running:
```bash
Copy-Item -Path "Hindi_Bill_Note_Sheet/artifacts/hindi-bill/dist/*" -Destination "hindi_bill_note_sheet_app/" -Recurse -Force
```

## 🔄 To Update

If you make changes to the React app and rebuild it:
```bash
# From Hindi_Bill_Note_Sheet/artifacts/hindi-bill/
npm run build

# Then copy the new build
Copy-Item -Path "Hindi_Bill_Note_Sheet/artifacts/hindi-bill/dist/*" -Destination "../../hindi_bill_note_sheet_app/" -Recurse -Force
```

---

**Status:** ✅ Production Ready | **Version:** 2.0.1 | **Integrated:** March 18, 2026
