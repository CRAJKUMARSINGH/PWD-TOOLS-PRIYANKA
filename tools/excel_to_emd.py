import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from io import BytesIO
import zipfile
import re
from utils.branding import apply_custom_css
from utils.navigation import create_breadcrumb, create_back_button
################

# Page configuration
st.set_page_config(
    page_title="Excel se EMD | PWD Tools Hub",
    page_icon="📊",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Excel se EMD")

def sanitize_filename(name: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", name.strip())
    return safe[:80] or "receipt"

def build_receipt_html(payee: str, amount_value: float, work: str) -> str:
    # Convert amount to float to ensure it's a number
    try:
        amount_float = float(amount_value)
        amount_str = f"{amount_float:,.2f}"  # Format with 2 decimal places
    except (ValueError, TypeError):
        amount_float = 0.0
        amount_str = "0.00"
    
    # Escape single quotes in strings for JavaScript
    payee_js = payee.replace("'", r"\'")
    work_js = work.replace("'", r"\'")
    
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Hand Receipt (RPWA 28)</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 0; }}
    .container {{ width: 100%; max-width: 900px; margin: 20px auto; border: 1px solid #e1e8e3; padding: 24px; box-sizing: border-box; background: #fff; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.08); }}
    .header {{ text-align: center; margin-bottom: 10px; color: #2E8B57; }}
    .details {{ margin-bottom: 1px; }}
    .amount-words {{ font-style: italic; }}
    .signature-area, .offices {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
    .signature-area td, .signature-area th, .offices td, .offices th {{ border: 1px solid #ccc; padding: 5px; text-align: left; }}
    .offices td, .offices th {{ border-color: #000; word-wrap: break-word; }}
    .input-field {{ border-bottom: 1px dotted #ccc; padding: 3px; width: calc(100% - 10px); display: inline-block; }}
    .bottom-left-box {{ position: relative; border: 2px solid black; padding: 10px; width: 300px; text-align: left; margin-top: 12px; }}
    .bottom-left-box p {{ margin: 3px 0; }}
    .blue-text {{ color: blue; }}
    @media print {{
      @page {{ size: A4 portrait; margin: 0; }}
      body {{ margin: 0; padding: 0; }}
      .container {{ border: none; width: 210mm; min-height: 297mm; margin: 0; padding: 20mm; box-sizing: border-box; }}
      .input-field {{ border: none; }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <div id="receipt-content">
      <div class="header">
        <h2>Payable to: - {payee} (Electric Contractor)</h2>
        <h2>HAND RECEIPT (RPWA 28)</h2>
        <p>(Referred to in PWF&A Rules 418,424,436 & 438)</p>
        <p>Division - PWD Electric Division, Udaipur</p>
      </div>
      <div class="details">
        <p>(1)Cash Book Voucher No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <p>(2)Cheque No. and Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <p>(3) Pay for ECS Rs. {amount_str}/- (Rupees <span id="amount-words" class="amount-words"></span>)</p>
        <p>(4) Paid by me</p>
        <p>(5) Received from The Executive Engineer PWD Electric Division, Udaipur the sum of Rs. {amount_str}/- (Rupees <span id="amount-words-2" class="amount-words"></span>)</p>
        <p>Name of work for which payment is made: <span id="work-name" class="input-field">{work}</span></p>
        <p>Chargeable to Head:- 8443 [EMD-Refund]</p>
        <table class="signature-area">
          <tr><td>Witness</td><td>Stamp</td><td>Signature of payee</td></tr>
          <tr><td>Cash Book No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Page No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td></td></tr>
        </table>
        <table class="offices">
          <tr><td>For use in the Divisional Office</td><td>For use in the Accountant General's office</td></tr>
          <tr><td>Checked</td><td>Audited/Reviewed</td></tr>
          <tr><td>Accounts Clerk</td><td>DA &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Auditor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Supdt. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G.O.</td></tr>
        </table>
      </div>
      <div class="bottom-left-box">
        <p class="blue-text">Passed for Rs. {amount_str}</p>
        <p class="blue-text" id="amount-words-3">In Words Rupees: </p>
        <p class="blue-text">Chargeable to Head:- 8443 [EMD-Refund]</p>
        <div class="seal">
          <p>Ar.</p>
          <p>D.A.</p>
          <p>E.E.</p>
        </div>
      </div>
    </div>
  </div>
  <script>
    function convertNumberToWords(num) {{
      const ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
      const tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"];
      const teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
      const crore = " Crore ";
      const lakh = " Lakh ";
      const thousand = " Thousand ";
      const hundred = " Hundred ";
      const andWord = " and ";
      
      if (!num || isNaN(num)) return "Zero";
      
      // Remove any commas and convert to number
      num = parseFloat(num.toString().replace(/,/g, ''));
      if (isNaN(num)) return "Zero";
      
      // Round to 2 decimal places and get the integer part
      const rupees = Math.floor(num);
      const paise = Math.round((num - rupees) * 100);
      
      let words = "";
      
      // Process rupees part
      if (rupees > 0) {{
        let r = rupees;
        if (Math.floor(r / 10000000)) {{ words += convertNumberToWords(Math.floor(r / 10000000)) + crore; r %= 10000000; }}
        if (Math.floor(r / 100000)) {{ words += convertNumberToWords(Math.floor(r / 100000)) + lakh; r %= 100000; }}
        if (Math.floor(r / 1000)) {{ words += convertNumberToWords(Math.floor(r / 1000)) + thousand; r %= 1000; }}
        if (Math.floor(r / 100)) {{ words += convertNumberToWords(Math.floor(r / 100)) + hundred; r %= 100; }}
        if (r > 0) {{
          if (words !== "") words += andWord;
          if (r < 10) words += ones[r];
          else if (r < 20) words += teens[r - 10];
          else {{ 
            words += tens[Math.floor(r / 10)]; 
            if (r % 10 > 0) words += " " + ones[r % 10]; 
          }}
        }}
        words += " Rupees";
      }}
      
      // Process paise part
      if (paise > 0) {{
        if (words !== "") words += " and ";
        if (paise < 10) words += ones[paise];
        else if (paise < 20) words += teens[paise - 10];
        else {{ 
          words += tens[Math.floor(paise / 10)]; 
          if (paise % 10 > 0) words += " " + ones[paise % 10]; 
        }}
        words += " Paise";
      }}
      
      return words || "Zero Rupees";
    }}
    
    // Format the amount with commas
    function formatAmount(amount) {{
      return amount.toString().replace(/\B(?=(\d{{3}})+(?!\d))/g, ",");
    }}
    
    // Update all amount in words placeholders
    document.addEventListener('DOMContentLoaded', function() {{
      const amount = {amount_float};
      const amountInWords = convertNumberToWords(amount);
      document.querySelectorAll('.amount-words').forEach(el => {{
        el.textContent = amountInWords + ' only';
      }});
      document.getElementById('amount-words-3').textContent = 'In Words Rupees: ' + amountInWords + ' Only';
    }});
  </script>
</body>
</html>
""".format(
        payee=payee_js,
        work=work_js,
        amount_float=amount_float,
        amount_str=amount_str
    )
    
    return html

def main():
    st.markdown("#### Generate Hand Receipts (RPWA 28) from Excel")
    st.info("Upload an Excel (.xlsx) or CSV, map columns, and download receipts. No external dependency.")

    uploaded = st.file_uploader("Upload .xlsx or .csv", type=["xlsx", "csv"], accept_multiple_files=False)

    if not uploaded:
        create_back_button()
        return

    # Read data
    df = None
    sheet_name = None
    try:
        name_lower = uploaded.name.lower()
        if name_lower.endswith(".xlsx"):
            try:
                # First try with openpyxl
                try:
                    xls = pd.ExcelFile(uploaded, engine="openpyxl")
                except ImportError:
                    # Fall back to xlrd
                    xls = pd.ExcelFile(uploaded, engine="xlrd")
                
                if len(xls.sheet_names) > 1:
                    sheet_name = st.selectbox("Select sheet", xls.sheet_names)
                else:
                    sheet_name = xls.sheet_names[0]
                    
                df = pd.read_excel(uploaded, sheet_name=sheet_name, engine=xls.engine)
                
            except Exception as e:
                st.error(f"Error reading Excel file: {str(e)}\n\n"
                        "Please ensure your Excel file is not password protected and is a valid .xlsx file.")
                st.info("If the problem persists, try saving your file as a .csv and uploading that instead.")
                create_back_button()
                return
        elif name_lower.endswith(".csv"):
            df = pd.read_csv(uploaded)
        else:
            st.error("Unsupported file type. Please upload .xlsx or .csv. Legacy .xls is not supported; convert to .xlsx or CSV.")
            create_back_button()
            return
    except Exception as e:
        st.error(f"Failed to read file: {e}")
        create_back_button()
        return

    if df is None or df.empty:
        st.warning("No data found in the file.")
        create_back_button()
        return

    # Debug: Show sheet names and first few rows
    st.write("### Debug - Excel File Structure")
    try:
        xls = pd.ExcelFile(uploaded, engine="openpyxl")
        st.write(f"Sheet names: {xls.sheet_names}")
        
        # Show first sheet data
        df_debug = pd.read_excel(uploaded, sheet_name=0, nrows=5)
        st.write("First 5 rows of first sheet:")
        st.dataframe(df_debug)
        
        # Show column data types
        st.write("Column data types:")
        st.dataframe(df_debug.dtypes.rename('Data Type').to_frame())
        
    except Exception as e:
        st.error(f"Error analyzing Excel file: {e}")

    st.markdown("##### Preview")
    st.dataframe(df.head(20), use_container_width=True)

    # Guess columns
    cols = list(df.columns.astype(str))
    def guess(patterns):
        for c in cols:
            lc = c.lower()
            if any(p in lc for p in patterns):
                return c
        return None
    default_payee = guess(["payee", "contractor", "name"]) or cols[0]
    default_amount = guess(["amount", "amt", "emd", "value"]) or cols[min(1, len(cols)-1)]
    default_work = guess(["work", "name of work", "work name"]) or cols[min(2, len(cols)-1)]

    st.markdown("##### Map Columns")
    col1, col2, col3 = st.columns(3)
    with col1:
        payee_col = st.selectbox("Payee column", cols, index=cols.index(default_payee) if default_payee in cols else 0)
    with col2:
        amount_col = st.selectbox("Amount column", cols, index=cols.index(default_amount) if default_amount in cols else (1 if len(cols) > 1 else 0))
    with col3:
        work_col = st.selectbox("Work column", cols, index=cols.index(default_work) if default_work in cols else (2 if len(cols) > 2 else 0))

    run = st.button("Generate Receipts", type="primary")

    if not run:
        create_back_button()
        return

    # Build receipt HTMLs
    records = []
    invalid_rows = []
    for idx, row in df.iterrows():
        # Initialize amount_raw to ensure it's always defined
        amount_raw = None
        try:
            payee = str(row[payee_col]).strip()
            work = str(row[work_col]).strip()
            amount_raw = row[amount_col]
            
            # Skip rows that contain formatting information or are clearly not data rows
            # Check if any field contains HTML/CSS formatting indicators
            if any(indicator in payee.lower() or indicator in work.lower() 
                   for indicator in ['font-family', 'font-size', 'color:', 'style=', 'class=']):
                continue  # Skip this row as it contains formatting, not data
            
            # Check for missing values
            if pd.isna(payee) or pd.isna(work) or pd.isna(amount_raw):
                invalid_rows.append((idx + 2, "Missing required values"))  # +2 for 1-based index and header row
                continue
                
            # Additional check for empty or whitespace-only values
            if not payee or not work or str(amount_raw).strip() == '':
                invalid_rows.append((idx + 2, "Empty or whitespace-only values"))
                continue
                
            # Try to convert amount to float
            try:
                amount = float(amount_raw)
                # Check for invalid amounts
                if amount <= 0:
                    invalid_rows.append((idx + 2, f"Invalid amount value (must be positive): {amount_raw}"))
                    continue
            except (ValueError, TypeError) as e:
                invalid_rows.append((idx + 2, f"Invalid amount value: {amount_raw} (Error: {str(e)})"))
                continue
                
            # Now we can safely use 'amount' variable
            html = build_receipt_html(payee, amount, work)
            filename = f"hand_receipt_{sanitize_filename(payee)}_{idx}.html"
            records.append((idx, payee, amount, work, html, filename))
            
        except Exception as e:
            # Only reference variables that are guaranteed to exist
            error_msg = str(e)
            # Check if amount_raw exists and has a value before using it
            if amount_raw is not None:
                error_msg = f"Error processing amount: {amount_raw} - {error_msg}"
            invalid_rows.append((idx + 2, error_msg))
            continue

    if not records:
        st.error("❌ No valid rows to generate receipts. Please check your data.")
        
        if invalid_rows:
            st.warning("Found the following issues in your data:")
            for row_num, error in invalid_rows[:10]:  # Show first 10 errors to avoid overwhelming
                st.write(f"- Row {row_num}: {error}")
            if len(invalid_rows) > 10:
                st.write(f"... and {len(invalid_rows) - 10} more issues")
        
        st.info("💡 Tips:")
        st.write("- Make sure all required columns (Payee, Work, Amount) have values")
        st.write("- Check that the Amount column contains only numbers")
        st.write("- Verify there are no empty rows in your data")
        
        # Show sample of the data with selected columns
        st.subheader("Data Preview (with selected columns)")
        preview_cols = [payee_col, work_col, amount_col]
        st.dataframe(df[preview_cols].head(), use_container_width=True)
        
        create_back_button()
        return

    st.success(f"Generated {len(records)} receipt(s).")

    # Preview first
    preview_idx = st.selectbox("Preview row", [r[0] for r in records], format_func=lambda i: f"Row {i}")
    preview = next(r for r in records if r[0] == preview_idx)
    components.html(preview[4], height=850, scrolling=True)

    # Downloads
    st.markdown("##### Download")
    col_a, col_b = st.columns([1,1])
    with col_a:
        for idx, payee, amount, work, html, filename in records[:20]:
            st.download_button(
                label=f"Download {filename}",
                data=html,
                file_name=filename,
                mime="text/html",
                use_container_width=True,
                key=f"dl_{idx}"
            )
        if len(records) > 20:
            st.caption(f"Showing first 20 downloads. Use ZIP for all {len(records)} receipts.")

    with col_b:
        buf = BytesIO()
        with zipfile.ZipFile(buf, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
            for _, _, _, _, html, filename in records:
                zf.writestr(filename, html)
        buf.seek(0)
        st.download_button(
            label=f"Download all as ZIP ({len(records)} files)",
            data=buf.getvalue(),
            file_name="hand_receipts.zip",
            mime="application/zip",
            use_container_width=True,
            key="dl_zip"
        )

    # Navigation
    create_back_button()


if __name__ == "__main__":
    main()
