"""
Generate Test Bill in All 6 Formats
Creates: First Page, Deviation Statement, Note Sheet, Certificate II, Certificate III, Extra Items
Outputs: HTML, PDF, ZIP, DOC
"""

import os
from datetime import datetime
from pathlib import Path

def create_output_folder():
    """Create OUTPUT folder if it doesn't exist"""
    output_dir = Path("OUTPUT")
    output_dir.mkdir(exist_ok=True)
    return output_dir

def generate_first_page_html():
    """Generate First Page Summary"""
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First Page - Bill Summary</title>
    <style>
        @page { size: A4; margin: 20mm; }
        body { font-family: 'Times New Roman', serif; margin: 0; padding: 20mm; font-size: 12pt; }
        .header { text-align: center; margin-bottom: 20px; border-bottom: 2px solid #000; padding-bottom: 10px; }
        .header h1 { margin: 0; font-size: 18pt; }
        .header h2 { margin: 5px 0; font-size: 14pt; }
        .section { margin: 20px 0; }
        .field { margin: 10px 0; display: flex; }
        .field-label { font-weight: bold; min-width: 200px; }
        .field-value { flex: 1; border-bottom: 1px dotted #000; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { border: 1px solid #000; padding: 8px; text-align: left; }
        th { background-color: #f0f0f0; font-weight: bold; }
        .amount { text-align: right; font-family: 'Courier New', monospace; }
        .total-row { font-weight: bold; background-color: #e8f4fd; }
        .footer { margin-top: 40px; text-align: center; font-size: 10pt; color: #666; }
    </style>
</head>
<body>
    <div class="header">
        <h1>PUBLIC WORKS DEPARTMENT</h1>
        <h2>FIRST PAGE - BILL SUMMARY</h2>
        <p>Division: PWD Electric Division, Udaipur</p>
    </div>
    
    <div class="section">
        <h3>Project Information</h3>
        <div class="field">
            <span class="field-label">Name of Work:</span>
            <span class="field-value">Construction of Road from Village A to Village B</span>
        </div>
        <div class="field">
            <span class="field-label">Contractor Name:</span>
            <span class="field-value">M/s ABC Construction Company</span>
        </div>
        <div class="field">
            <span class="field-label">Agreement No:</span>
            <span class="field-value">AGR/2024/001</span>
        </div>
        <div class="field">
            <span class="field-label">Bill Serial No:</span>
            <span class="field-value">01</span>
        </div>
        <div class="field">
            <span class="field-label">Bill Type:</span>
            <span class="field-value">Running Bill</span>
        </div>
        <div class="field">
            <span class="field-label">Date:</span>
            <span class="field-value">26/02/2026</span>
        </div>
    </div>
    
    <div class="section">
        <h3>Financial Summary</h3>
        <table>
            <tr>
                <th>S.No.</th>
                <th>Description</th>
                <th>Amount (₹)</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Work Order Amount</td>
                <td class="amount">10,00,000.00</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Work Done Till Date</td>
                <td class="amount">5,00,000.00</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Previous Payments</td>
                <td class="amount">2,00,000.00</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Current Bill Amount</td>
                <td class="amount">3,00,000.00</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Less: Deductions</td>
                <td class="amount">45,000.00</td>
            </tr>
            <tr class="total-row">
                <td colspan="2">Net Payable Amount</td>
                <td class="amount">2,55,000.00</td>
            </tr>
        </table>
    </div>
    
    <div class="section">
        <h3>Deductions Breakdown</h3>
        <table>
            <tr>
                <th>S.No.</th>
                <th>Deduction Type</th>
                <th>Rate</th>
                <th>Amount (₹)</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Security Deposit (SD)</td>
                <td>10%</td>
                <td class="amount">30,000.00</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Income Tax (IT)</td>
                <td>2%</td>
                <td class="amount">6,000.00</td>
            </tr>
            <tr>
                <td>3</td>
                <td>GST</td>
                <td>2%</td>
                <td class="amount">6,000.00</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Labour Cess (LC)</td>
                <td>1%</td>
                <td class="amount">3,000.00</td>
            </tr>
            <tr class="total-row">
                <td colspan="3">Total Deductions</td>
                <td class="amount">45,000.00</td>
            </tr>
        </table>
    </div>
    
    <div class="footer">
        <p>Public Works Department, Udaipur, Rajasthan</p>
        <p>Prepared on Initiative of Mrs. Premlata Jain, AAO</p>
        <p>Generated on: 26/02/2026</p>
    </div>
</body>
</html>
"""
    return html

def generate_deviation_statement_html():
    """Generate Deviation Statement"""
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deviation Statement</title>
    <style>
        @page { size: A4 landscape; margin: 15mm; }
        body { font-family: 'Times New Roman', serif; margin: 0; padding: 15mm; font-size: 11pt; }
        .header { text-align: center; margin-bottom: 15px; border-bottom: 2px solid #000; padding-bottom: 10px; }
        .header h1 { margin: 0; font-size: 16pt; }
        .header h2 { margin: 5px 0; font-size: 13pt; }
        table { width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 10pt; }
        th, td { border: 1px solid #000; padding: 6px; text-align: left; }
        th { background-color: #f0f0f0; font-weight: bold; }
        .amount { text-align: right; font-family: 'Courier New', monospace; }
        .total-row { font-weight: bold; background-color: #e8f4fd; }
        .excess { color: #d32f2f; }
        .saving { color: #388e3c; }
    </style>
</head>
<body>
    <div class="header">
        <h1>DEVIATION STATEMENT</h1>
        <h2>Work: Construction of Road from Village A to Village B</h2>
        <p>Contractor: M/s ABC Construction Company | Agreement No: AGR/2024/001</p>
    </div>
    
    <table>
        <tr>
            <th>S.No.</th>
            <th>Description of Item</th>
            <th>Unit</th>
            <th>Qty (WO)</th>
            <th>Rate (₹)</th>
            <th>Amount WO (₹)</th>
            <th>Qty Executed</th>
            <th>Amount Bill (₹)</th>
            <th>Excess (+) / Saving (-)</th>
            <th>Remark</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Earthwork in excavation</td>
            <td>Cum</td>
            <td class="amount">1000</td>
            <td class="amount">500.00</td>
            <td class="amount">5,00,000.00</td>
            <td class="amount">950</td>
            <td class="amount">4,75,000.00</td>
            <td class="amount saving">-25,000.00</td>
            <td>Saving</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Providing and laying cement concrete</td>
            <td>Cum</td>
            <td class="amount">500</td>
            <td class="amount">800.00</td>
            <td class="amount">4,00,000.00</td>
            <td class="amount">520</td>
            <td class="amount">4,16,000.00</td>
            <td class="amount excess">+16,000.00</td>
            <td>Excess</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Steel reinforcement</td>
            <td>Qtl</td>
            <td class="amount">100</td>
            <td class="amount">6000.00</td>
            <td class="amount">6,00,000.00</td>
            <td class="amount">95</td>
            <td class="amount">5,70,000.00</td>
            <td class="amount saving">-30,000.00</td>
            <td>Saving</td>
        </tr>
        <tr class="total-row">
            <td colspan="5">TOTAL</td>
            <td class="amount">15,00,000.00</td>
            <td></td>
            <td class="amount">14,61,000.00</td>
            <td class="amount saving">-39,000.00</td>
            <td>Net Saving</td>
        </tr>
    </table>
    
    <div style="margin-top: 30px;">
        <p><strong>Summary:</strong></p>
        <p>Total Work Order Amount: ₹15,00,000.00</p>
        <p>Total Executed Amount: ₹14,61,000.00</p>
        <p>Total Excess: ₹16,000.00</p>
        <p>Total Saving: ₹55,000.00</p>
        <p><strong>Net Saving: ₹39,000.00</strong></p>
    </div>
</body>
</html>
"""
    return html

def generate_note_sheet_html():
    """Generate Bill Note Sheet"""
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bill Note Sheet</title>
    <style>
        @page { size: A4; margin: 20mm; }
        body { font-family: 'Times New Roman', serif; margin: 0; padding: 20mm; font-size: 12pt; }
        .header { text-align: center; margin-bottom: 20px; border-bottom: 2px solid #000; padding-bottom: 10px; }
        .header h1 { margin: 0; font-size: 18pt; }
        .section { margin: 20px 0; }
        .field { margin: 10px 0; }
        table { width: 100%; border-collapse: collapse; margin: 15px 0; }
        th, td { border: 1px solid #000; padding: 8px; text-align: left; }
        th { background-color: #f0f0f0; font-weight: bold; }
        .amount { text-align: right; font-family: 'Courier New', monospace; }
        .total-row { font-weight: bold; background-color: #e8f4fd; }
        .signature-area { margin-top: 50px; display: flex; justify-content: space-between; }
        .signature-box { width: 45%; text-align: center; }
        .signature-line { border-top: 1px solid #000; margin-top: 60px; padding-top: 5px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>BILL NOTE SHEET</h1>
        <h2>Bill Scrutiny Sheet with LD Calculation</h2>
    </div>
    
    <div class="section">
        <h3>Project Details</h3>
        <div class="field"><strong>Work:</strong> Construction of Road from Village A to Village B</div>
        <div class="field"><strong>Contractor:</strong> M/s ABC Construction Company</div>
        <div class="field"><strong>Agreement No:</strong> AGR/2024/001</div>
        <div class="field"><strong>Bill No:</strong> 01</div>
        <div class="field"><strong>Bill Date:</strong> 26/02/2026</div>
    </div>
    
    <div class="section">
        <h3>Time Schedule</h3>
        <table>
            <tr>
                <th>Description</th>
                <th>Date</th>
            </tr>
            <tr>
                <td>Agreement Date</td>
                <td>01/01/2025</td>
            </tr>
            <tr>
                <td>Scheduled Completion</td>
                <td>31/12/2025</td>
            </tr>
            <tr>
                <td>Actual Completion (Till Date)</td>
                <td>26/02/2026</td>
            </tr>
            <tr class="total-row">
                <td>Delay (Days)</td>
                <td>57 days</td>
            </tr>
        </table>
    </div>
    
    <div class="section">
        <h3>Liquidated Damages (LD) Calculation</h3>
        <table>
            <tr>
                <th>Parameter</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Work Order Amount</td>
                <td class="amount">₹10,00,000.00</td>
            </tr>
            <tr>
                <td>LD Rate (per day)</td>
                <td class="amount">0.05% of WO</td>
            </tr>
            <tr>
                <td>LD per day</td>
                <td class="amount">₹500.00</td>
            </tr>
            <tr>
                <td>Delay Period</td>
                <td class="amount">57 days</td>
            </tr>
            <tr class="total-row">
                <td>Total LD Amount</td>
                <td class="amount">₹28,500.00</td>
            </tr>
        </table>
    </div>
    
    <div class="section">
        <h3>Bill Amount Calculation</h3>
        <table>
            <tr>
                <th>S.No.</th>
                <th>Description</th>
                <th>Amount (₹)</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Gross Bill Amount</td>
                <td class="amount">3,00,000.00</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Less: Liquidated Damages</td>
                <td class="amount">28,500.00</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Less: Other Deductions</td>
                <td class="amount">45,000.00</td>
            </tr>
            <tr class="total-row">
                <td colspan="2">Net Payable Amount</td>
                <td class="amount">2,26,500.00</td>
            </tr>
        </table>
    </div>
    
    <div class="signature-area">
        <div class="signature-box">
            <div class="signature-line">
                Junior Engineer
            </div>
        </div>
        <div class="signature-box">
            <div class="signature-line">
                Executive Engineer<br>
                PWD Division, Udaipur
            </div>
        </div>
    </div>
</body>
</html>
"""
    return html

def generate_certificate_ii_html():
    """Generate Certificate II"""
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Certificate II</title>
    <style>
        @page { size: A4; margin: 25mm; }
        body { font-family: 'Times New Roman', serif; margin: 0; padding: 25mm; font-size: 13pt; line-height: 1.8; }
        .header { text-align: center; margin-bottom: 30px; border: 3px double #000; padding: 15px; }
        .header h1 { margin: 0; font-size: 20pt; text-decoration: underline; }
        .content { margin: 30px 0; text-align: justify; }
        .content p { margin: 15px 0; }
        .amount { font-weight: bold; text-decoration: underline; }
        .signature-area { margin-top: 80px; text-align: right; }
        .signature-line { border-top: 1px solid #000; width: 250px; margin-left: auto; padding-top: 5px; text-align: center; }
    </style>
</head>
<body>
    <div class="header">
        <h1>CERTIFICATE II</h1>
        <p style="margin: 10px 0;">Public Works Department</p>
        <p style="margin: 0;">Udaipur, Rajasthan</p>
    </div>
    
    <div class="content">
        <p>Certified that the work <strong>"Construction of Road from Village A to Village B"</strong> has been executed by <strong>M/s ABC Construction Company</strong> under Agreement No. <strong>AGR/2024/001</strong> dated <strong>01/01/2025</strong>.</p>
        
        <p>The work has been executed as per the specifications and drawings approved by the competent authority.</p>
        
        <p>The measurements have been recorded in the Measurement Book No. <strong>MB-2025-001</strong> and the same have been checked and found correct.</p>
        
        <p>The gross amount of work done is <span class="amount">Rupees Three Lakh Only (₹3,00,000.00)</span>.</p>
        
        <p>After deducting the following amounts:</p>
        <ul>
            <li>Security Deposit: ₹30,000.00</li>
            <li>Income Tax: ₹6,000.00</li>
            <li>GST: ₹6,000.00</li>
            <li>Labour Cess: ₹3,000.00</li>
            <li>Liquidated Damages: ₹28,500.00</li>
        </ul>
        
        <p>The net amount payable to the contractor is <span class="amount">Rupees Two Lakh Twenty Six Thousand Five Hundred Only (₹2,26,500.00)</span>.</p>
        
        <p>This certificate is issued for the purpose of payment to the contractor.</p>
    </div>
    
    <div class="signature-area">
        <p><strong>Date: 26/02/2026</strong></p>
        <div class="signature-line">
            Executive Engineer<br>
            PWD Electric Division<br>
            Udaipur
        </div>
    </div>
</body>
</html>
"""
    return html

def generate_certificate_iii_html():
    """Generate Certificate III"""
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Certificate III</title>
    <style>
        @page { size: A4; margin: 25mm; }
        body { font-family: 'Times New Roman', serif; margin: 0; padding: 25mm; font-size: 13pt; line-height: 1.8; }
        .header { text-align: center; margin-bottom: 30px; border: 3px double #000; padding: 15px; }
        .header h1 { margin: 0; font-size: 20pt; text-decoration: underline; }
        .content { margin: 30px 0; text-align: justify; }
        .content p { margin: 15px 0; }
        .signature-area { margin-top: 80px; display: flex; justify-content: space-between; }
        .signature-box { width: 45%; text-align: center; }
        .signature-line { border-top: 1px solid #000; margin-top: 60px; padding-top: 5px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>CERTIFICATE III</h1>
        <p style="margin: 10px 0;">Completion Certificate</p>
        <p style="margin: 0;">Public Works Department, Udaipur</p>
    </div>
    
    <div class="content">
        <p>This is to certify that the work <strong>"Construction of Road from Village A to Village B"</strong> under Agreement No. <strong>AGR/2024/001</strong> dated <strong>01/01/2025</strong> has been completed by <strong>M/s ABC Construction Company</strong>.</p>
        
        <p>The work was scheduled to be completed by <strong>31/12/2025</strong> and has been actually completed on <strong>26/02/2026</strong>.</p>
        
        <p>The total value of work executed is <strong>₹5,00,000.00</strong> (Rupees Five Lakh Only) against the work order value of <strong>₹10,00,000.00</strong> (Rupees Ten Lakh Only).</p>
        
        <p>The work has been executed as per the approved drawings and specifications and is found satisfactory.</p>
        
        <p>All the materials used in the work are of approved quality and the workmanship is as per the specifications.</p>
        
        <p>The contractor has maintained all the required records and documents during the execution of work.</p>
        
        <p>This certificate is issued for record and further necessary action.</p>
    </div>
    
    <div class="signature-area">
        <div class="signature-box">
            <div class="signature-line">
                Junior Engineer<br>
                Date: 26/02/2026
            </div>
        </div>
        <div class="signature-box">
            <div class="signature-line">
                Executive Engineer<br>
                PWD Division, Udaipur<br>
                Date: 26/02/2026
            </div>
        </div>
    </div>
</body>
</html>
"""
    return html

def generate_extra_items_html():
    """Generate Extra Items Statement"""
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Extra Items Statement</title>
    <style>
        @page { size: A4; margin: 20mm; }
        body { font-family: 'Times New Roman', serif; margin: 0; padding: 20mm; font-size: 12pt; }
        .header { text-align: center; margin-bottom: 20px; border-bottom: 2px solid #000; padding-bottom: 10px; }
        .header h1 { margin: 0; font-size: 18pt; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { border: 1px solid #000; padding: 8px; text-align: left; }
        th { background-color: #f0f0f0; font-weight: bold; }
        .amount { text-align: right; font-family: 'Courier New', monospace; }
        .total-row { font-weight: bold; background-color: #fff8e1; }
    </style>
</head>
<body>
    <div class="header">
        <h1>EXTRA ITEMS STATEMENT</h1>
        <h2>Additional Work Items</h2>
        <p>Work: Construction of Road from Village A to Village B</p>
    </div>
    
    <table>
        <tr>
            <th>S.No.</th>
            <th>Description of Extra Item</th>
            <th>Unit</th>
            <th>Quantity</th>
            <th>Rate (₹)</th>
            <th>Amount (₹)</th>
            <th>Approval Ref.</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Additional earthwork due to site conditions</td>
            <td>Cum</td>
            <td class="amount">50</td>
            <td class="amount">500.00</td>
            <td class="amount">25,000.00</td>
            <td>EE/2026/01</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Extra concrete for foundation strengthening</td>
            <td>Cum</td>
            <td class="amount">20</td>
            <td class="amount">800.00</td>
            <td class="amount">16,000.00</td>
            <td>EE/2026/02</td>
        </tr>
        <tr class="total-row">
            <td colspan="5">TOTAL EXTRA ITEMS</td>
            <td class="amount">41,000.00</td>
            <td></td>
        </tr>
    </table>
    
    <div style="margin-top: 30px;">
        <p><strong>Note:</strong> All extra items have been approved by the competent authority as per the approval references mentioned above.</p>
    </div>
</body>
</html>
"""
    return html

def main():
    """Generate all bill documents"""
    
    print("=" * 70)
    print("TEST BILL GENERATOR - ALL 6 FORMATS")
    print("=" * 70)
    print()
    
    # Create output folder
    output_dir = create_output_folder()
    print(f"✓ Output folder created: {output_dir}")
    print()
    
    # Generate all HTML documents
    documents = {
        "1_First_Page.html": generate_first_page_html(),
        "2_Deviation_Statement.html": generate_deviation_statement_html(),
        "3_Note_Sheet.html": generate_note_sheet_html(),
        "4_Certificate_II.html": generate_certificate_ii_html(),
        "5_Certificate_III.html": generate_certificate_iii_html(),
        "6_Extra_Items.html": generate_extra_items_html()
    }
    
    print("Generating HTML documents...")
    for filename, content in documents.items():
        filepath = output_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ {filename}")
    
    print()
    print("=" * 70)
    print("GENERATION COMPLETE")
    print("=" * 70)
    print()
    print(f"All 6 documents generated in: {output_dir}/")
    print()
    print("Documents created:")
    print("  1. First_Page.html - Bill summary")
    print("  2. Deviation_Statement.html - Excess/Saving analysis")
    print("  3. Note_Sheet.html - Bill scrutiny with LD calculation")
    print("  4. Certificate_II.html - Payment certificate")
    print("  5. Certificate_III.html - Completion certificate")
    print("  6. Extra_Items.html - Additional work items")
    print()
    print("=" * 70)
    print("TO CONVERT TO PDF:")
    print("=" * 70)
    print()
    print("Option 1: Open each HTML file in browser")
    print("  - Press Ctrl+P (or Cmd+P on Mac)")
    print("  - Select 'Save as PDF'")
    print("  - Click 'Save'")
    print()
    print("Option 2: Use the Streamlit App")
    print("  - Run: streamlit run app.py")
    print("  - Navigate to: Bill Generator Enterprise")
    print("  - Upload Excel file or enter data")
    print("  - Generate all documents with PDF option")
    print()
    print("=" * 70)
    print()
    print("Note: For DOC and ZIP formats, use the Bill Generator Enterprise")
    print("tool in the Streamlit app which has full export capabilities.")
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()
