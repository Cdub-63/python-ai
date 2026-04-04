from config import MAX_CHARS
from functions.get_file_content import get_file_content

if __name__ == "__main__":
    result = get_file_content("calculator", "lorem.txt")
    print("Result for lorem.txt:")
    print(f"  length={len(result)}")
    print(f"  truncation message present={result.endswith(f'[...File \"lorem.txt\" truncated at {MAX_CHARS} characters]')}")
    print(f"  last 80 chars: {result[-80:]}")
    print()

    test_cases = [
        ("main.py", "Result for main.py:"),
        ("pkg/calculator.py", "Result for pkg/calculator.py:"),
        ("/bin/cat", "Result for '/bin/cat' file:"),
        ("pkg/does_not_exist.py", "Result for pkg/does_not_exist.py:"),
    ]

    for file_path, title in test_cases:
        result = get_file_content("calculator", file_path)
        print(title)
        for line in result.splitlines():
            print(f"  {line}")
        if not result:
            print("  <empty>")
        print()