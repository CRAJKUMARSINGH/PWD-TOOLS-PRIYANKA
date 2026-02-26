"""
Bill Note Sheet Generator with LD Calculation
Standalone deployable tool
Run: streamlit run tools/bill_note_sheet.py
"""

import streamlit as st
from datetime import datetime
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from utils.branding import apply_custom_css
    from utils.navigation import create_breadcrumb, create_back_button
    has_utils = True
except ImportError:
    has_utils = False

# Page configuration
st.set_page_config(
    page_title="Bill Note Sheet Generator",
    page_icon="📝",
    layout="wide"
)

# Apply branding if available
if has_utils:
    apply_custom_css()
    create_breadcrumb("Bill Note Sheet Generator")

def calculate_liquidated_damages(work_order_amount, actual_progress, start_date, scheduled_date, actual_date):
    """
    Calculate liquidated damages using PWD Quarterly Distribution Method
    """
    try:
        if not (start_date and scheduled_date and actual_date):
            return 0
        
        total_duration = (scheduled_date - start_date).days
        elapsed_days = (actual_date - start_date).days
        
        if total_duration <= 0 or elapsed_days <= total_duration:
            return 0
        
        # Quarterly distribution
        q1_percent, q2_percent, q3_percent, q4_percent = 0.125, 0.25, 0.25, 0.375
        
        # Quarter boundaries
        q1_end = int(total_duration * 0.25)
        q2_end = int(total_duration * 0.50)
        q3_end = int(total_duration * 0.75)
        q4_end = total_duration
        
        # Quarter lengths
        q1_length = q1_end
        q2_length = q2_end - q1_end
        q3_length = q3_end - q2_end
        q4_length = q4_end - q3_end
        
        # Work distribution
        q1_work = work_order_amount * q1_percent
        q2_work = work_order_amount * q2_percent
        q3_work = work_order_amount * q3_percent
        q4_work = work_order_amount * q4_percent
        
        # Daily progress rates
        q1_daily = q1_work / q1_length if q1_length > 0 else 0
        q2_daily = q2_work / q2_length if q2_length > 0 else 0
        q3_daily = q3_work / q3_length if q3_length > 0 else 0
        q4_daily = q4_work / q4_length if q4_length > 0 else 0
        
        # Calculate required progress
        required_progress = 0
        
        if elapsed_days <= q1_end:
            required_progress = elapsed_days * q1_daily
            penalty_rate = 0.025
        elif elapsed_days <= q2_end:
            days_in_q2 = elapsed_days - q1_end
            required_progress = q1_work + (days_in_q2 * q2_daily)
            penalty_rate = 0.05
        elif elapsed_days <= q3_end:
            days_in_q3 = elapsed_days - q2_end
            required_progress = q1_work + q2_work + (days_in_q3 * q3_daily)
            penalty_rate = 0.075
        else:
            days_in_q4 = min(elapsed_days - q3_end, q4_length)
            required_progress = q1_work + q2_work + q3_work + (days_in_q4 * q4_daily)
            penalty_rate = 0.10
        
        # Calculate unexecuted work
        unexecuted_work = max(0, required_progress - actual_progress)
        
        # Special case: 100% complete but delayed
        if unexecuted_work <= 0 and elapsed_days > total_duration:
            delay_beyond_completion = elapsed_days - total_duration
            unexecuted_work = q4_daily * delay_beyond_completion
            penalty_rate = 0.10
        elif unexecuted_work <= 0:
            return 0
        
        ld_amount = penalty_rate * unexecuted_work
        return int(round(ld_amount))
        
    except Exception as e:
        st.error(f"Error calculating LD: {e}")
        return 0

def main():
    st.markdown("## 📝 Bill Note Sheet Generator")
    st.markdown("### With Full LD Calculation (PWD Quarterly Method)")
    
    # Input columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Project Details")
        work_order_amount = st.number_input("Work Order Amount (₹)", min_value=0.0, value=1000000.0, step=10000.0)
        actual_progress = st.number_input("Actual Progress Amount (₹)", min_value=0.0, value=1000000.0, step=10000.0)
        progress_percentage = (actual_progress / work_order_amount * 100) if work_order_amount > 0 else 0
        st.metric("Progress", f"{progress_percentage:.2f}%")
    
    with col2:
        st.markdown("### 📅 Project Timeline")
        start_date = st.date_input("Start Date", value=datetime(2024, 1, 1))
        scheduled_date = st.date_input("Scheduled Completion", value=datetime(2024, 12, 31))
        actual_date = st.date_input("Actual Completion", value=datetime(2025, 1, 5))
        delay_days = (actual_date - scheduled_date).days if actual_date > scheduled_date else 0
        
        if delay_days > 0:
            st.warning(f"⚠️ Delay: {delay_days} days")
        else:
            st.success("✅ On time")
    
    # Calculate button
    if st.button("🧮 Calculate Liquidated Damages", type="primary", use_container_width=True):
        start_dt = datetime.combine(start_date, datetime.min.time())
        scheduled_dt = datetime.combine(scheduled_date, datetime.min.time())
        actual_dt = datetime.combine(actual_date, datetime.min.time())
        
        ld_amount = calculate_liquidated_damages(work_order_amount, actual_progress, start_dt, scheduled_dt, actual_dt)
        
        st.markdown("---")
        st.markdown("## 📋 Results")
        
        res_col1, res_col2, res_col3 = st.columns(3)
        with res_col1:
            st.metric("Work Order", f"₹{work_order_amount:,.2f}")
        with res_col2:
            st.metric("Progress", f"₹{actual_progress:,.2f}", f"{progress_percentage:.2f}%")
        with res_col3:
            st.metric("Delay", f"{delay_days} days")
        
        # Note sheet text
        st.markdown("---")
        st.markdown("### 📄 Note Sheet (Hindi)")
        
        note_text = f"कार्य {progress_percentage:.2f}% पूर्ण हुआ है।\n\n"
        
        if delay_days > 0:
            note_text += f"कार्य में {delay_days} दिन की देरी हुई है।\n\n"
            if ld_amount > 0:
                note_text += f"Agreement clause 2 के अनुसार Liquidated Damages की गणना रुपया {ld_amount:,} है। वसूली योग्य LD हेतु विनिर्णय का स्पष्ट अंकन अपेक्षित है।\n\n"
        else:
            note_text += "कार्य समय पर संपादित हुआ है।\n\n"
        
        note_text += "उपरोक्त विवरण के सन्दर्भ में समुचित निर्णय हेतु प्रस्तुत है।"
        
        st.text_area("Note Content", value=note_text, height=250)
        
        if ld_amount > 0:
            st.error(f"### ⚠️ LD Amount: ₹{ld_amount:,}")
        else:
            st.success("### ✅ No LD Applicable")
    
    # Back button
    if has_utils:
        st.markdown("---")
        create_back_button()

if __name__ == "__main__":
    main()
