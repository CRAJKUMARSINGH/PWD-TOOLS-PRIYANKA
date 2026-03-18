# Original Hindi Bill Note Sheet App - Complete Specification

## From: https://hindibillnote.netlify.app/

## Layout Structure

### Header
- **Background:** Animated gradient (pink shades: #880e4f → #c2185b → #e91e63)
- **Text:** "🌸 हिंदी बिल नोट शीट जनरेटर | Hindi Bill Note Sheet Generator - Full App Test 🌸"
- **Animation:** Shimmer effect moving left to right

### Main Container (Two Columns)

#### LEFT COLUMN - Form Panel

**1. Test Controls Section (Green Box)**
- Background: #e8f5e8
- Border: 2px solid #4caf50
- Contains:
  - Heading: "🧪 Automated Testing Controls"
  - Button 1: "🚀 Run All Tests (Form + Calculations + PDF)" - Green background
  - Button 2: "📝 Load Sample Bill Data" - Blue background (#2196f3)
  - Button 3: "🔍 Test Edge Cases" - Orange background (#ff9800)
  - Test Results Display Area (shows pass/fail messages)

**2. Basic Information Section (White Box)**
- Heading: "मूल जानकारी / Basic Information"
- Fields:
  1. बिल शीर्षक / Bill Title (full width text input)
  2. Row 1:
     - 1. बजट शीर्ष / Budget Head
     - 2. अनुबंध संख्या / Agreement No.
  3. Row 2:
     - 3. एम.बी. संख्या व पृष्ठ / MB No. & Page
     - 4. उप-खंड का नाम / Sub Division Name
  4. 5. कार्य का नाम / Name of Work (textarea, 2 rows)
  5. Row 3:
     - 6. ठेकेदार का नाम / Contractor Name
     - 7. मूल / जमा / Original / Deposit (dropdown)

**3. Dates & Amounts Section (White Box)**
- Heading: "तिथियाँ व राशि / Dates & Amounts"
- Fields:
  1. Row 1:
     - 8. प्रारंभ तिथि / Date of Commencement (date picker)
     - 9. पूर्णता तिथि / Date of Completion (date picker)
  2. Row 2:
     - 11. कुल कार्यादेश राशि / Total Work Order Amount (₹) (number input)
     - 12B. इस बिल की राशि / Amount of This Bill (₹) (number input)
  3. **Live Calculations Display (Pink Box)**
     - Background: #fce4ec
     - Border: 1px solid #f48fb1
     - Shows:
       - SD @ 10%: ₹ [calculated]
       - IT @ 2%: ₹ [calculated]
       - GST @ 2% (Higher Even): ₹ [calculated]
       - LC @ 1%: ₹ [calculated]
       - Net Amount: ₹ [calculated] (green color)

**4. Other Details Section (White Box)**
- Heading: "अन्य विवरण / Other Details"
- Field:
  - हस्ताक्षरकर्ता नाम / Signatory Name (text input)

**5. Generate PDF Button**
- Text: "🖨️ Generate PDF (10mm margins, centered signature)"
- Background: Pink gradient (#880e4f → #c2185b)
- Full width

#### RIGHT COLUMN - Preview Panel

**1. Preview Header Section (White Box)**
- Heading: "👁 Live Preview — Note Sheet Output"
- Subtext: "Exactly what will print on A4 with 10mm margins" (pink color)

**2. Preview Area (White Box with Pink Border)**
- Border: 2px solid #f48fb1
- Contains:
  - **Table with borders:**
    - Header row: Bill Title (centered, pink background #fce4ec)
    - Data rows (all with borders):
      - 1. Budget Head | [value]
      - 2. Agreement No. | [value]
      - 3. MB No. & Page | [value]
      - 4. Name of Sub Division | [value]
      - 5. Name of Work | [value]
      - 6. Name of Contractor | [value]
      - 7. Original / Deposit | [value]
      - 8. Date of Commencement | [value]
      - 9. Date of Completion | [value]
      - 11. Total Work Order Amount | Rs. [value]
      - 12B. Amount of This Bill | Rs. [value]
    - Deduction header row: "Deductions:- Rs." (gray background)
    - Deduction rows (indented):
      - SD @ 10% | Rs. [value]
      - IT @ 2% | Rs. [value]
      - GST @ 2% | Rs. [value]
      - LC @ 1% | Rs. [value]
  - **Note Section (bordered box below table):**
    - Text: "उपरोक्त विवरण के सन्दर्भ में समुचित निर्णय हेतु प्रस्तुत है।"
    - Signature (centered): [Signatory Name]

## Colors Used
- Pink gradient background: #fce4ec → #f8bbd0
- Deep pink: #880e4f
- Medium pink: #c2185b
- Light pink: #e91e63
- Pink border: #f48fb1
- Pink background: #fce4ec
- Green (tests): #4caf50, #e8f5e8
- Blue (button): #2196f3
- Orange (button): #ff9800
- Gray (deductions): #ebebeb

## Fonts
- Primary: 'Noto Sans Devanagari', sans-serif
- All Hindi text uses Devanagari font

## Sample Data (When "Load Sample Data" clicked)
- Bill Title: RUNNING ACCOUNT BILL NO. 01
- Budget Head: 4059-01-800-0-31
- Agreement No: 62/2024-25
- MB No & Page: 813/Page 84-85
- Sub Division: Udaipur
- Name of Work: Construction of 33/11 KV Sub Station at Village Khempur
- Contractor Name: M/s. ABC Electrical Works
- Date Commencement: 2024-04-01
- Date Completion: 2025-03-31
- Total Amount: 500000
- Bill Amount: 125000
- Signatory: Er. Rajkumar Singh

## Calculations
- SD (Security Deposit): 10% of Bill Amount
- IT (Income Tax): 2% of Bill Amount
- GST: 2% of Bill Amount, rounded to NEXT HIGHER EVEN number
- LC (Labour Cess): 1% of Bill Amount
- Net Amount: Bill Amount - (SD + IT + GST + LC)

## Key Features
1. Live preview updates as you type
2. Live calculations update automatically
3. GST rounds to higher even number (e.g., 175 → 176)
4. Test suite with comprehensive tests
5. PDF generation opens in new window
6. All bilingual labels (Hindi/English)
7. Responsive layout
8. Professional government document formatting
