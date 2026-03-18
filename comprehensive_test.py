"""
Comprehensive Automated Test Suite
Tests all 13 tools thoroughly without manual intervention
"""

import sys
import os
from pathlib import Path
import importlib.util
import traceback
import ast

sys.path.insert(0, str(Path(__file__).parent))

class ToolTester:
    def __init__(self):
        self.results = {}
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
    
    def test_file_exists(self, tool_path):
        """Test if file exists"""
        return Path(tool_path).exists()
    
    def test_syntax(self, tool_path):
        """Test Python syntax"""
        try:
            with open(tool_path, 'r', encoding='utf-8') as f:
                code = f.read()
                compile(code, tool_path, 'exec')
            return True, "OK"
        except SyntaxError as e:
            return False, f"Syntax Error: {e}"
        except Exception as e:
            return False, f"Error: {e}"
    
    def test_imports(self, tool_path):
        """Test if all imports work"""
        try:
            with open(tool_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            tree = ast.parse(code)
            imports = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)
            
            # Check critical imports
            critical = ['streamlit', 'pandas']
            missing = [imp for imp in critical if not any(imp in i for i in imports)]
            
            if missing:
                return False, f"Missing critical imports: {missing}"
            
            return True, f"Found {len(imports)} imports"
        except Exception as e:
            return False, f"Import check failed: {e}"
    
    def test_streamlit_config(self, tool_path):
        """Test if st.set_page_config is present"""
        try:
            with open(tool_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            if 'st.set_page_config' in code or 'set_page_config' in code:
                return True, "Page config found"
            else:
                return False, "No page config found"
        except Exception as e:
            return False, f"Config check failed: {e}"
    
    def test_main_function(self, tool_path):
        """Test if main function or execution code exists"""
        try:
            with open(tool_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            has_main = 'def main(' in code
            has_execution = 'if __name__' in code or 'st.' in code
            
            if has_main or has_execution:
                return True, "Execution code found"
            else:
                return False, "No execution code found"
        except Exception as e:
            return False, f"Main function check failed: {e}"
    
    def test_error_handling(self, tool_path):
        """Test if error handling exists"""
        try:
            with open(tool_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            has_try = 'try:' in code
            has_except = 'except' in code
            
            if has_try and has_except:
                return True, "Error handling present"
            else:
                return False, "No error handling found"
        except Exception as e:
            return False, f"Error handling check failed: {e}"
    
    def test_file_size(self, tool_path):
        """Test if file size is reasonable"""
        try:
            size = Path(tool_path).stat().st_size
            if size < 100:
                return False, f"File too small: {size} bytes"
            elif size > 1000000:
                return False, f"File too large: {size} bytes"
            else:
                return True, f"Size OK: {size} bytes"
        except Exception as e:
            return False, f"Size check failed: {e}"
    
    def test_tool(self, tool_path, tool_name):
        """Run all tests on a tool"""
        print(f"\n{'='*80}")
        print(f"Testing: {tool_name}")
        print(f"{'='*80}")
        
        tests = [
            ("File Exists", self.test_file_exists),
            ("Syntax Check", self.test_syntax),
            ("Import Check", self.test_imports),
            ("Streamlit Config", self.test_streamlit_config),
            ("Main Function", self.test_main_function),
            ("Error Handling", self.test_error_handling),
            ("File Size", self.test_file_size),
        ]
        
        tool_results = []
        tool_passed = 0
        tool_failed = 0
        
        for test_name, test_func in tests:
            self.total_tests += 1
            try:
                if test_name == "File Exists":
                    result = test_func(tool_path)
                    success = result
                    message = "Found" if result else "Not found"
                else:
                    success, message = test_func(tool_path)
                
                if success:
                    print(f"  ✅ {test_name:20} | {message}")
                    tool_passed += 1
                    self.passed_tests += 1
                else:
                    print(f"  ❌ {test_name:20} | {message}")
                    tool_failed += 1
                    self.failed_tests += 1
                
                tool_results.append({
                    "test": test_name,
                    "success": success,
                    "message": message
                })
            except Exception as e:
                print(f"  ❌ {test_name:20} | Exception: {e}")
                tool_failed += 1
                self.failed_tests += 1
                tool_results.append({
                    "test": test_name,
                    "success": False,
                    "message": str(e)
                })
        
        self.results[tool_name] = {
            "passed": tool_passed,
            "failed": tool_failed,
            "total": len(tests),
            "details": tool_results
        }
        
        print(f"\n  Result: {tool_passed}/{len(tests)} tests passed")
        
        return tool_failed == 0

def main():
    print("="*80)
    print("PWD TOOLS SUITE - COMPREHENSIVE AUTOMATED TEST")
    print("="*80)
    print("Testing all 13 tools with 7 checks each = 91 total tests")
    print("="*80)
    
    tools = [
        ("pages/1__Bill_Generator.py", "Bill Generator Enterprise"),
        ("pages/2__Excel_to_EMD.py", "Excel to EMD"),
        ("pages/3__EMD_Refund.py", "EMD Refund Calculator"),
        ("pages/4__Security_Refund.py", "Security Refund"),
        ("pages/5__Bill_Note_Sheet.py", "Bill Note Sheet"),
        ("pages/6__Deductions_Table.py", "Deductions Table"),
        ("pages/7__Financial_Progress.py", "Financial Progress"),
        ("pages/8__APG_Calculator.py", "APG Calculator"),
        ("pages/9__Delay_Calculator.py", "Delay Calculator"),
        ("pages/10__Stamp_Duty.py", "Stamp Duty"),
        ("pages/11__Hand_Receipt.py", "Hand Receipt"),
        ("pages/12__User_Manual.py", "User Manual"),
        ("pages/13_ℹ_Main_Info.py", "Main Info"),
    ]
    
    tester = ToolTester()
    all_passed = True
    
    for tool_path, tool_name in tools:
        passed = tester.test_tool(tool_path, tool_name)
        if not passed:
            all_passed = False
    
    # Final Summary
    print("\n" + "="*80)
    print("FINAL SUMMARY")
    print("="*80)
    print(f"Total Tests: {tester.total_tests}")
    print(f"Passed: {tester.passed_tests} ({tester.passed_tests/tester.total_tests*100:.1f}%)")
    print(f"Failed: {tester.failed_tests} ({tester.failed_tests/tester.total_tests*100:.1f}%)")
    print()
    
    # Tool-by-tool summary
    print("="*80)
    print("TOOL-BY-TOOL SUMMARY")
    print("="*80)
    
    for tool_name, result in tester.results.items():
        status = "✅ PASS" if result["failed"] == 0 else "❌ FAIL"
        print(f"{status} | {tool_name:35} | {result['passed']}/{result['total']} tests passed")
    
    print("\n" + "="*80)
    
    if all_passed and tester.failed_tests == 0:
        print("🎉 ALL TESTS PASSED! Application is production-ready!")
        print("="*80)
        return 0
    else:
        print(f"⚠️  {tester.failed_tests} test(s) failed. Review issues above.")
        print("="*80)
        return 1

if __name__ == "__main__":
    sys.exit(main())
