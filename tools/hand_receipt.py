import streamlit as st
import pandas as pd
import io
from datetime import datetime

def generate_receipt(data, idx):
    """Generate RPWA 28 receipt for a single row of data"""
    receipt = f"""
    <div style='border: 1px solid #000; padding: 15px; margin: 10px 0; font-family: Arial, sans-serif;'>
        <div style='text-align: center; font-weight: bold; font-size: 16px; margin-bottom: 10px;'>
            HAND RECEIPT (RPWA 28)
        </div>
        <div style='margin-bottom: 5px;'><b>Receipt No.:</b> {data.get('Receipt No.', '')}</div>
        <div style='margin-bottom: 5px;'><b>Date:</b> {data.get('Date', datetime.now().strftime('%d/%m/%Y'))}</div>
        <div style='margin-bottom: 5px;'><b>Received from:</b> {data.get('Received From', '')}</div>
        <div style='margin-bottom: 5px;'><b>Department:</b> {data.get('Department', '')}</div>
        <div style='margin-bottom: 5px;'><b>Amount (in words):</b> {data.get('Amount in Words', '')}</div>
        <div style='margin-bottom: 5px;'><b>Amount (in figures):</b> ₹{data.get('Amount', ''):,.2f}</div>
        <div style='margin-bottom: 5px;'><b>Purpose:</b> {data.get('Purpose', '')}</div>
        <div style='margin-top: 20px; display: flex; justify-content: space-between;'>
            <div style='text-align: center;'>
                <div>______________________</div>
                <div>Received By</div>
            </div>
            <div style='text-align: center;'>
                <div>______________________</div>
                <div>Signature & Stamp</div>
            </div>
        </div>
    </div>
    """
    return receipt

def main():
    st.set_page_config(page_title="Hand Receipt Generator", page_icon="📄")
    
    st.title("Generate Hand Receipts (RPWA 28)")
    st.write("Upload an Excel (.xlsx) or CSV file containing receipt data and download generated receipts.")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload .xlsx or .csv", type=["xlsx", "csv"])
    
    if uploaded_file is not None:
        try:
            # Read the file
            if uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file, engine='openpyxl')
            else:
                df = pd.read_csv(uploaded_file)
            
            # Display column mapping UI
            st.subheader("Map Columns")
            st.write("Please verify or update the column mappings:")
            
            # Get all columns from the dataframe
            columns = df.columns.tolist()
            
            # Default mappings for common column names
            default_mappings = {
                'Receipt No.': next((col for col in columns if 'receipt' in col.lower() and 'no' in col.lower()), columns[0] if columns else ''),
                'Date': next((col for col in columns if 'date' in col.lower()), columns[1] if len(columns) > 1 else ''),
                'Received From': next((col for col in columns if 'name' in col.lower() or 'from' in col.lower()), columns[2] if len(columns) > 2 else ''),
                'Department': next((col for col in columns if 'dept' in col.lower() or 'department' in col.lower()), columns[3] if len(columns) > 3 else ''),
                'Amount': next((col for col in columns if 'amount' in col.lower()), columns[4] if len(columns) > 4 else ''),
                'Amount in Words': next((col for col in columns if 'word' in col.lower() or 'text' in col.lower()), columns[5] if len(columns) > 5 else ''),
                'Purpose': next((col for col in columns if 'purpose' in col.lower() or 'description' in col.lower()), columns[6] if len(columns) > 6 else '')
            }
            
            # Create mapping UI
            mappings = {}
            for field, default_col in default_mappings.items():
                mappings[field] = st.selectbox(
                    f"Select column for '{field}':",
                    columns,
                    index=columns.index(default_col) if default_col in columns else 0
                )
            
            # Generate preview
            if st.button("Generate Receipts"):
                st.subheader("Generated Receipts")
                
                # Process each row and generate receipts
                for idx, row in df.iterrows():
                    receipt_data = {field: row[col] for field, col in mappings.items()}
                    st.markdown(generate_receipt(receipt_data, idx), unsafe_allow_html=True)
                
                # Create a single HTML file with all receipts
                all_receipts = "".join([generate_receipt(
                    {field: row[col] for field, col in mappings.items()}, 
                    idx) for idx, row in df.iterrows()])
                
                # Add basic HTML structure
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Hand Receipts (RPWA 28)</title>
                    <meta charset="UTF-8">
                    <style>
                        @media print {{
                            @page {{ margin: 0.5cm; }}
                            div {{ page-break-inside: avoid; }}
                        }}
                        body {{ 
                            font-family: Arial, sans-serif; 
                            margin: 20px;
                        }}
                        .receipt {{
                            border: 1px solid #000; 
                            padding: 15px; 
                            margin: 10px 0;
                        }}
                        .header {{
                            text-align: center; 
                            font-weight: bold; 
                            font-size: 16px; 
                            margin-bottom: 10px;
                        }}
                        .footer {{
                            margin-top: 20px; 
                            display: flex; 
                            justify-content: space-between;
                        }}
                        .field {{ margin-bottom: 5px; }}
                    </style>
                </head>
                <body>
                    <h1>Hand Receipts (RPWA 28)</h1>
                    <p>Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                    {all_receipts}
                </body>
                </html>
                """
                
                # Create download button
                st.download_button(
                    label="Download All Receipts (HTML)",
                    data=html_content,
                    file_name=f"hand_receipts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html",
                    mime="text/html"
                )
                
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()
