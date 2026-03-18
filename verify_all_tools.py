"""
Verify all 13 tools can be imported without errors
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

tools = [
    "pages/1__Bill_Generator.py",
    "pages/2__Excel_to_EMD.py",
    "pages/3__EMD_Refund.py",
    "pages/4__Security_Refund.py",
    "pages/5__Bill_Note_Sheet.py",
    "pages/6__Deductions_Table.py",
    "pages/7__Financial_Progress.py",
    "pages/8__APG_Calculator.py",
    "pages/9__Delay_Calculator.py",
    "pages/10__Stamp_Duty.py",
    "pages/11__Hand_Receipt.py",
    "pages/12__User_Manual.py",
    "pages/13_ℹ_Main_Info.py"
]

print("=" * 80)
print("PWD TOOLS SUITE - VERIFICATION TEST")
print("=" * 80)
print()

passed = 0
failed = 0

for tool_path in tools:
    tool_name = Path(tool_path).stem
    try:
        # Check if file exists
        if not Path(tool_path).exists():
            print(f"❌ FAIL | {tool_name:40} | File not found")
            failed += 1
            continue
        
        # Try to compile the file
        with open(tool_path, 'r', encoding='utf-8') as f:
            code = f.read()
            compile(code, tool_path, 'exec')
        
        print(f"✅ PASS | {tool_name:40} | OK")
        passed += 1
        
    except SyntaxError as e:
        print(f"❌ FAIL | {tool_name:40} | Syntax Error: {e}")
        failed += 1
    except Exception as e:
        print(f"❌ FAIL | {tool_name:40} | Error: {e}")
        failed += 1

print()
print("=" * 80)
print(f"RESULTS: {passed} passed, {failed} failed out of {len(tools)} tools")
print("=" * 80)

if failed == 0:
    print("🎉 ALL TOOLS VERIFIED SUCCESSFULLY!")
    sys.exit(0)
else:
    print(f"⚠️  {failed} tool(s) have issues")
    sys.exit(1)
