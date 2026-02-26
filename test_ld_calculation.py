"""
Test LD Calculation in Updated Bill Note Sheet
"""
from datetime import datetime

# Import the calculation function
import sys
sys.path.insert(0, 'PWD-Tools')
from pages.Bill_Note_Sheet_Enhanced import calculate_liquidated_damages

# Test Case 1: 5 days delay, 100% complete
print("=" * 60)
print("Test Case 1: 5 Days Delay, 100% Complete")
print("=" * 60)

work_order = 1000000
progress = 1000000
start = datetime(2024, 1, 1)
scheduled = datetime(2024, 12, 31)
actual = datetime(2025, 1, 5)

ld = calculate_liquidated_damages(work_order, progress, start, scheduled, actual)
print(f"Work Order: Rs.{work_order:,}")
print(f"Progress: Rs.{progress:,} (100%)")
print(f"Delay: {(actual - scheduled).days} days")
print(f"LD Amount: Rs.{ld:,}")
print(f"Expected: Rs.4,167")
print(f"Match: {'✅ YES' if abs(ld - 4167) < 10 else '❌ NO'}")

# Test Case 2: No delay
print("\n" + "=" * 60)
print("Test Case 2: No Delay")
print("=" * 60)

actual_ontime = datetime(2024, 12, 31)
ld2 = calculate_liquidated_damages(work_order, progress, start, scheduled, actual_ontime)
print(f"Work Order: Rs.{work_order:,}")
print(f"Progress: Rs.{progress:,} (100%)")
print(f"Delay: 0 days")
print(f"LD Amount: Rs.{ld2:,}")
print(f"Expected: Rs.0")
print(f"Match: {'✅ YES' if ld2 == 0 else '❌ NO'}")

print("\n" + "=" * 60)
print("✅ LD Calculation Test Complete!")
print("=" * 60)
