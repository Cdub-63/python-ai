from functions.run_python_file import run_python_file

# Test cases
print("Test 1 - Run calculator main.py without args:")
result = run_python_file("calculator", "main.py")
print(f"Result: {result}")
print()

print("Test 2 - Run calculator main.py with args ['3 + 5']:")
result = run_python_file("calculator", "main.py", ["3 + 5"])
print(f"Result: {result}")
print()

print("Test 3 - Run calculator tests.py:")
result = run_python_file("calculator", "tests.py")
print(f"Result: {result}")
print()

print("Test 4 - Run outside directory (../main.py):")
result = run_python_file("calculator", "../main.py")
print(f"Result: {result}")
print()

print("Test 5 - Run nonexistent file (nonexistent.py):")
result = run_python_file("calculator", "nonexistent.py")
print(f"Result: {result}")
print()

print("Test 6 - Run non-Python file (lorem.txt):")
result = run_python_file("calculator", "lorem.txt")
print(f"Result: {result}")
print()