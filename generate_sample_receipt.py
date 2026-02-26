"""
Generate a sample EMD Refund Receipt in PDF format
Creates a Hand Receipt (RPWA 28) document
"""

from datetime import datetime

def number_to_words(num):
    """Convert number to Indian words format"""
    if num == 0:
        return "Zero"
    
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
             "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    
    def convert_below_thousand(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
        else:
            result = ones[n // 100] + " Hundred"
            remainder = n % 100
            if remainder != 0:
                result += " " + convert_below_thousand(remainder)
            return result
    
    words = ""
    
    # Crores
    if num >= 10000000:
        crore_part = num // 10000000
        words += convert_below_thousand(crore_part) + " Crore "
        num %= 10000000
    
    # Lakhs
    if num >= 100000:
        lakh_part = num // 100000
        words += convert_below_thousand(lakh_part) + " Lakh "
        num %= 100000
    
    # Thousands
    if num >= 1000:
        thousand_part = num // 1000
        words += convert_below_thousand(thousand_part) + " Thousand "
        num %= 1000
    
    # Remaining
    if num > 0:
        if words:
            words += "and "
        words += convert_below_thousand(num)
    
    return words.strip()

def generate_receipt_html(payee_name, amount, work_name):
    """Generate HTML for the receipt"""
    
    amount_words = number_to_words(int(amount))
    current_date = datetime.now().strftime("%d/%m/%Y")
    
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=210mm, height=297mm">
    <title>Hand Receipt (RPWA 28) - EMD Refund</title>
    <style>
        @page {{
            size: A4;
            margin: 20mm;
        }}
        
        body {{
            font-family: 'Times New Roman', serif;
            margin: 0;
            padding: 20mm;
            font-size: 14pt;
            line-height: 1.6;
        }}
        
        .container {{
            width: 100%;
            max-width: 170mm;
            margin: 0 auto;
            border: 2px solid #000;
            padding: 15mm;
            box-sizing: border-box;
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 20px;
            border-bottom: 2px solid #000;
            padding-bottom: 10px;
        }}
        
        .header h1 {{
            margin: 0;
            font-size: 20pt;
            font-weight: bold;
            text-decoration: underline;
        }}
        
        .header h2 {{
            margin: 5px 0 0 0;
            font-size: 16pt;
            font-weight: normal;
        }}
        
        .receipt-number {{
            text-align: right;
            margin-bottom: 15px;
            font-weight: bold;
        }}
        
        .content {{
            margin: 20px 0;
        }}
        
        .field {{
            margin: 15px 0;
            display: flex;
            align-items: baseline;
        }}
        
        .field-label {{
            font-weight: bold;
            min-width: 150px;
        }}
        
        .field-value {{
            flex: 1;
            border-bottom: 1px dotted #000;
            padding: 0 10px;
        }}
        
        .amount-section {{
            margin: 20px 0;
            padding: 10px;
            background-color: #f9f9f9;
            border: 1px solid #000;
        }}
        
        .signature-section {{
            margin-top: 40px;
            display: flex;
            justify-content: space-between;
        }}
        
        .signature-box {{
            width: 45%;
            text-align: center;
        }}
        
        .signature-line {{
            border-top: 1px solid #000;
            margin-top: 50px;
            padding-top: 5px;
        }}
        
        .footer {{
            margin-top: 30px;
            text-align: center;
            font-size: 10pt;
            color: #666;
        }}
        
        .stamp-area {{
            position: absolute;
            bottom: 30mm;
            left: 30mm;
            width: 60mm;
            height: 40mm;
            border: 2px dashed #999;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #999;
            font-size: 12pt;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>HAND RECEIPT</h1>
            <h2>(RPWA 28)</h2>
        </div>
        
        <div class="receipt-number">
            Receipt No: EMD/{datetime.now().strftime("%Y%m%d")}/001
        </div>
        
        <div class="content">
            <div class="field">
                <span class="field-label">Date:</span>
                <span class="field-value">{current_date}</span>
            </div>
            
            <div class="field">
                <span class="field-label">Received from:</span>
                <span class="field-value">{payee_name}</span>
            </div>
            
            <div class="amount-section">
                <div class="field">
                    <span class="field-label">Amount (₹):</span>
                    <span class="field-value" style="font-weight: bold; font-size: 16pt;">₹ {amount:,.2f}</span>
                </div>
                
                <div class="field">
                    <span class="field-label">In Words:</span>
                    <span class="field-value" style="font-style: italic;">{amount_words} Rupees Only</span>
                </div>
            </div>
            
            <div class="field">
                <span class="field-label">Purpose:</span>
                <span class="field-value">Refund of Earnest Money Deposit (EMD)</span>
            </div>
            
            <div class="field">
                <span class="field-label">Name of Work:</span>
                <span class="field-value">{work_name}</span>
            </div>
            
            <div class="field">
                <span class="field-label">Mode of Payment:</span>
                <span class="field-value">Cheque / NEFT / RTGS</span>
            </div>
        </div>
        
        <div class="signature-section">
            <div class="signature-box">
                <div class="signature-line">
                    Receiver's Signature
                </div>
            </div>
            
            <div class="signature-box">
                <div class="signature-line">
                    Authorized Signatory<br>
                    PWD Department
                </div>
            </div>
        </div>
        
        <div class="stamp-area">
            OFFICE SEAL
        </div>
        
        <div class="footer">
            <p>Public Works Department, Udaipur, Rajasthan</p>
            <p>Prepared on Initiative of Mrs. Premlata Jain, AAO</p>
        </div>
    </div>
</body>
</html>
"""
    return html

def main():
    """Generate sample receipts"""
    
    print("=" * 70)
    print("EMD REFUND RECEIPT GENERATOR")
    print("=" * 70)
    print()
    
    # Sample receipts
    samples = [
        {
            "payee": "M/s ABC Construction Company",
            "amount": 50000,
            "work": "Construction of Road from Village A to Village B"
        },
        {
            "payee": "M/s XYZ Builders Pvt. Ltd.",
            "amount": 125000,
            "work": "Building Construction at Government School, Udaipur"
        },
        {
            "payee": "Shri Rajesh Kumar",
            "amount": 25000,
            "work": "Repair and Maintenance of PWD Office Building"
        }
    ]
    
    for i, sample in enumerate(samples, 1):
        print(f"Sample Receipt {i}:")
        print(f"  Payee: {sample['payee']}")
        print(f"  Amount: ₹{sample['amount']:,}")
        print(f"  Amount in Words: {number_to_words(sample['amount'])} Rupees Only")
        print(f"  Work: {sample['work']}")
        
        # Generate HTML
        html_content = generate_receipt_html(
            sample['payee'],
            sample['amount'],
            sample['work']
        )
        
        # Save to file
        filename = f"EMD_Receipt_Sample_{i}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"  ✓ Generated: {filename}")
        print()
    
    print("=" * 70)
    print("INSTRUCTIONS:")
    print("=" * 70)
    print()
    print("To convert HTML to PDF:")
    print()
    print("Option 1: Open in Browser")
    print("  1. Open the HTML file in your browser")
    print("  2. Press Ctrl+P (or Cmd+P on Mac)")
    print("  3. Select 'Save as PDF'")
    print("  4. Click 'Save'")
    print()
    print("Option 2: Use the Streamlit App")
    print("  1. Run: streamlit run app.py")
    print("  2. Navigate to: EMD Refund")
    print("  3. Fill in the form")
    print("  4. Click 'Generate Receipt'")
    print("  5. Use the PDF download button")
    print()
    print("=" * 70)
    print()
    print("Files created:")
    for i in range(1, len(samples) + 1):
        print(f"  - EMD_Receipt_Sample_{i}.html")
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()
