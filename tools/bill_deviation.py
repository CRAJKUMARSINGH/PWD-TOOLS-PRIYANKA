"""
Bill Deviation Statement Generator
Standalone deployable tool with full functionality
Run: streamlit run tools/bill_deviation.py
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from utils.branding import apply_custom_css
    from utils.navigation import create_breadcrumb, create_back_button
    has_utils = True
except ImportError:
    has_utils = False

st.set_page_config(
    page_title="Bill Deviation Statement Generator",
    page_icon="📊",
    layout="wide"
)

if has_utils:
    apply_custom_css()
    create_breadcrumb("Bill Deviation Statement")

def calculate_deviation(qty_wo, rate, qty_executed, premium_percent=0):
    """Calculate deviation for a single item"""
    amt_wo = qty_wo * rate
    amt_bill = qty_executed * rate
    
    excess_qty = max(0, qty_executed - qty_wo)
    saving_qty = max(0, qty_wo - qty_executed)
    
    excess_amt = excess_qty * rate
    saving_amt = saving_qty * rate
    
    # Apply premium
    premium_multiplier = 1 + (premium_percent / 100)
    amt_wo_premium = amt_wo * premium_multiplier
    amt_bill_premium = amt_bill * premium_multiplier
    excess_amt_premium = excess_amt * premium_multiplier
    saving_amt_premium = saving_amt * premium_multiplier
    
    return {
        'amt_wo': amt_wo,
        'amt_bill': amt_bill,
        'excess_qty': excess_qty,
        'excess_amt': excess_amt,
        'saving_qty': saving_qty,
        'saving_amt': saving_amt,
        'amt_wo_premium': amt_wo_premium,
        'amt_bill_premium': amt_bill_premium,
        'excess_amt_premium': excess_amt_premium,
        'saving_amt_premium': saving_amt_premium
    }

def generate_deviation_html(items_data, header_data, premium_percent):
    """Generate HTML for deviation statement"""
    
    # Calculate totals
    total_wo = sum(item['amt_wo'] for item in items_data)
    total_bill = sum(item['amt_bill'] for item in items_data)
    total_excess = sum(item['excess_amt'] for item in items_data)
    total_saving = sum(item['saving_amt'] for item in items_data)
    
    # Apply premium
    premium_multiplier = 1 + (premium_percent / 100)
    total_wo_premium = total_wo * premium_multiplier
    total_bill_premium = total_bill * premium_multiplier
    total_excess_premium = total_excess * premium_multiplier
    total_saving_premium = total_saving * premium_multiplier
    
    # Calculate net difference
    net_difference = abs(total_bill_premium - total_wo_premium)
    is_saving = total_bill_premium < total_wo_premium
    percentage_deviation = (net_difference / total_wo_premium * 100) if total_wo_premium > 0 else 0
    
    # Generate HTML
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Deviation Statement</title>
    <style>
        @page {{ size: A4 landscape; margin: 10mm; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: Calibri, sans-serif; font-size: 9pt; }}
        .container {{ width: 100%; padding: 10px; }}
        .header {{ margin-bottom: 15px; }}
        .header h2 {{ text-align: center; font-size: 16pt; border: 2px solid #000; padding: 10px; }}
        .header-item {{ margin: 5px 0; }}
        table {{ width: 100%; border-collapse: collapse; font-size: 8pt; }}
        th, td {{ border: 1px solid black; padding: 4px 2px; text-align: left; }}
        th {{ background-color: #f0f0f0; text-align: center; font-weight: bold; }}
        .number {{ text-align: right; }}
        .total-row {{ font-weight: bold; background-color: #f8f8f8; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h2>DEVIATION STATEMENT</h2>
            <div class="header-item"><strong>Name of Work:</strong> {header_data.get('work_name', 'N/A')}</div>
            <div class="header-item"><strong>Name of Contractor:</strong> {header_data.get('contractor_name', 'N/A')}</div>
            <div class="header-item"><strong>Bill Serial No.:</strong> {header_data.get('bill_no', 'N/A')}</div>
            <div class="header-item"><strong>Agreement No.:</strong> {header_data.get('agreement_no', 'N/A')}</div>
        </div>
        <table>
            <thead>
                <tr>
                    <th style="width: 5%;">Item No.</th>
                    <th style="width: 30%;">Description</th>
                    <th style="width: 5%;">Unit</th>
                    <th style="width: 7%;">Qty WO</th>
                    <th style="width: 7%;">Rate</th>
                    <th style="width: 8%;">Amt WO</th>
                    <th style="width: 7%;">Qty Exec</th>
                    <th style="width: 8%;">Amt Exec</th>
                    <th style="width: 7%;">Excess Qty</th>
                    <th style="width: 8%;">Excess Amt</th>
                    <th style="width: 7%;">Saving Qty</th>
                    <th style="width: 8%;">Saving Amt</th>
                    <th style="width: 10%;">Remarks</th>
                </tr>
            </thead>
            <tbody>
"""
    
    # Add items
    for item in items_data:
        html += f"""
                <tr>
                    <td>{item['serial_no']}</td>
                    <td>{item['description']}</td>
                    <td>{item['unit']}</td>
                    <td class="number">{item['qty_wo']:.2f}</td>
                    <td class="number">{item['rate']:.2f}</td>
                    <td class="number">{item['amt_wo']:.2f}</td>
                    <td class="number">{item['qty_executed']:.2f}</td>
                    <td class="number">{item['amt_bill']:.2f}</td>
                    <td class="number">{item['excess_qty']:.2f if item['excess_qty'] > 0 else ''}</td>
                    <td class="number">{item['excess_amt']:.2f if item['excess_amt'] > 0 else ''}</td>
                    <td class="number">{item['saving_qty']:.2f if item['saving_qty'] > 0 else ''}</td>
                    <td class="number">{item['saving_amt']:.2f if item['saving_amt'] > 0 else ''}</td>
                    <td>{item.get('remark', '')}</td>
                </tr>
"""
    
    # Add totals
    html += f"""
                <tr class="total-row">
                    <td colspan="5">Grand Total Rs.</td>
                    <td class="number">{total_wo:.2f}</td>
                    <td></td>
                    <td class="number">{total_bill:.2f}</td>
                    <td></td>
                    <td class="number">{total_excess:.2f}</td>
                    <td></td>
                    <td class="number">{total_saving:.2f}</td>
                    <td></td>
                </tr>
                <tr>
                    <td colspan="5">Add Tender Premium ({premium_percent:.2f}%)</td>
                    <td class="number">{total_wo * (premium_percent/100):.2f}</td>
                    <td></td>
                    <td class="number">{total_bill * (premium_percent/100):.2f}</td>
                    <td></td>
                    <td class="number">{total_excess * (premium_percent/100):.2f}</td>
                    <td></td>
                    <td class="number">{total_saving * (premium_percent/100):.2f}</td>
                    <td></td>
                </tr>
                <tr class="total-row">
                    <td colspan="5">Grand Total including Premium Rs.</td>
                    <td class="number">{total_wo_premium:.2f}</td>
                    <td></td>
                    <td class="number">{total_bill_premium:.2f}</td>
                    <td></td>
                    <td class="number">{total_excess_premium:.2f}</td>
                    <td></td>
                    <td class="number">{total_saving_premium:.2f}</td>
                    <td></td>
                </tr>
                <tr class="total-row">
                    <td colspan="8">Overall {'Saving' if is_saving else 'Excess'} With Respect to Work Order Amount Rs.</td>
                    <td colspan="2" class="number">{'':'' if is_saving else net_difference:.2f}</td>
                    <td colspan="2" class="number">{net_difference:.2f if is_saving else ''}</td>
                    <td></td>
                </tr>
                <tr class="total-row">
                    <td colspan="8">Percentage of {'Saving' if is_saving else 'Excess'} %</td>
                    <td colspan="2" class="number">{'':'' if is_saving else percentage_deviation:.2f}%</td>
                    <td colspan="2" class="number">{percentage_deviation:.2f if is_saving else ''}%</td>
                    <td></td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
"""
    return html

def main():
    st.markdown("## 📊 Bill Deviation Statement Generator")
    st.markdown("### Generate professional deviation statements with excess/saving calculations")
    
    # Header information
    st.markdown("### 📋 Project Information")
    col1, col2 = st.columns(2)
    
    with col1:
        work_name = st.text_input("Name of Work", value="Construction of Road")
        contractor_name = st.text_input("Name of Contractor", value="ABC Contractors")
    
    with col2:
        bill_no = st.text_input("Bill Serial No.", value="01")
        agreement_no = st.text_input("Agreement No.", value="AGR/2024/001")
    
    premium_percent = st.number_input("Tender Premium (%)", min_value=-50.0, max_value=50.0, value=0.0, step=0.1)
    
    # Items input
    st.markdown("---")
    st.markdown("### 📝 Items Entry")
    
    # Option to upload Excel or manual entry
    input_method = st.radio("Input Method", ["Manual Entry", "Upload Excel"], horizontal=True)
    
    items_data = []
    
    if input_method == "Manual Entry":
        num_items = st.number_input("Number of Items", min_value=1, max_value=50, value=3)
        
        for i in range(int(num_items)):
            with st.expander(f"Item {i+1}", expanded=(i==0)):
                col1, col2, col3, col4, col5 = st.columns(5)
                
                with col1:
                    serial_no = st.text_input(f"Serial No.", value=str(i+1), key=f"serial_{i}")
                    description = st.text_input(f"Description", value=f"Item {i+1}", key=f"desc_{i}")
                
                with col2:
                    unit = st.text_input(f"Unit", value="Cum", key=f"unit_{i}")
                    qty_wo = st.number_input(f"Qty WO", min_value=0.0, value=100.0, key=f"qty_wo_{i}")
                
                with col3:
                    rate = st.number_input(f"Rate", min_value=0.0, value=1000.0, key=f"rate_{i}")
                
                with col4:
                    qty_executed = st.number_input(f"Qty Executed", min_value=0.0, value=95.0, key=f"qty_exec_{i}")
                
                with col5:
                    remark = st.text_input(f"Remark", value="", key=f"remark_{i}")
                
                # Calculate deviation
                dev = calculate_deviation(qty_wo, rate, qty_executed, premium_percent)
                
                items_data.append({
                    'serial_no': serial_no,
                    'description': description,
                    'unit': unit,
                    'qty_wo': qty_wo,
                    'rate': rate,
                    'qty_executed': qty_executed,
                    'remark': remark,
                    **dev
                })
    
    else:  # Upload Excel
        uploaded_file = st.file_uploader("Upload Excel file with items", type=['xlsx', 'xls'])
        
        if uploaded_file:
            try:
                df = pd.read_excel(uploaded_file)
                st.dataframe(df.head())
                
                # Map columns
                st.markdown("#### Map Columns")
                col1, col2, col3, col4, col5 = st.columns(5)
                
                with col1:
                    serial_col = st.selectbox("Serial No.", df.columns, index=0)
                    desc_col = st.selectbox("Description", df.columns, index=1)
                
                with col2:
                    unit_col = st.selectbox("Unit", df.columns, index=2)
                    qty_wo_col = st.selectbox("Qty WO", df.columns, index=3)
                
                with col3:
                    rate_col = st.selectbox("Rate", df.columns, index=4)
                
                with col4:
                    qty_exec_col = st.selectbox("Qty Executed", df.columns, index=5)
                
                with col5:
                    remark_col = st.selectbox("Remark", df.columns, index=min(6, len(df.columns)-1))
                
                # Process data
                for _, row in df.iterrows():
                    qty_wo = float(row[qty_wo_col])
                    rate = float(row[rate_col])
                    qty_executed = float(row[qty_exec_col])
                    
                    dev = calculate_deviation(qty_wo, rate, qty_executed, premium_percent)
                    
                    items_data.append({
                        'serial_no': str(row[serial_col]),
                        'description': str(row[desc_col]),
                        'unit': str(row[unit_col]),
                        'qty_wo': qty_wo,
                        'rate': rate,
                        'qty_executed': qty_executed,
                        'remark': str(row[remark_col]) if remark_col in df.columns else '',
                        **dev
                    })
                
            except Exception as e:
                st.error(f"Error reading Excel file: {e}")
    
    # Generate button
    if st.button("🎯 Generate Deviation Statement", type="primary", use_container_width=True):
        if items_data:
            header_data = {
                'work_name': work_name,
                'contractor_name': contractor_name,
                'bill_no': bill_no,
                'agreement_no': agreement_no
            }
            
            html_content = generate_deviation_html(items_data, header_data, premium_percent)
            
            # Display summary
            st.markdown("---")
            st.markdown("## 📊 Summary")
            
            total_wo = sum(item['amt_wo'] for item in items_data)
            total_bill = sum(item['amt_bill'] for item in items_data)
            total_excess = sum(item['excess_amt'] for item in items_data)
            total_saving = sum(item['saving_amt'] for item in items_data)
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Work Order Total", f"₹{total_wo:,.2f}")
            with col2:
                st.metric("Executed Total", f"₹{total_bill:,.2f}")
            with col3:
                st.metric("Total Excess", f"₹{total_excess:,.2f}")
            with col4:
                st.metric("Total Saving", f"₹{total_saving:,.2f}")
            
            # Download button
            st.markdown("---")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"deviation_statement_{timestamp}.html"
            
            st.download_button(
                label="📥 Download Deviation Statement (HTML)",
                data=html_content,
                file_name=filename,
                mime="text/html",
                use_container_width=True
            )
            
            # Preview
            with st.expander("👁️ Preview Deviation Statement"):
                st.components.v1.html(html_content, height=800, scrolling=True)
        
        else:
            st.warning("Please add at least one item")
    
    # Back button
    if has_utils:
        st.markdown("---")
        create_back_button()

if __name__ == "__main__":
    main()
