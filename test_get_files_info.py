from functions.get_files_info import get_files_info

# Test case 1: current directory
result = get_files_info("calculator", ".")
print("Result for current directory:")
for line in result.split('\n'):
    print("  " + line)

print()

# Test case 2: pkg directory
result = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:")
for line in result.split('\n'):
    print("  " + line)

print()

# Test case 3: /bin (outside)
result = get_files_info("calculator", "/bin")
print("Result for '/bin' directory:")
print("    " + result)

print()

# Test case 4: ../ (outside)
result = get_files_info("calculator", "../")
print("Result for '../' directory:")
print("    " + result)