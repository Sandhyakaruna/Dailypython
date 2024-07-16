def are_anagrams(num1, num2):
    """Check if two integers are anagrams."""
    # Convert the integers to strings
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Sort the characters of the strings
    sorted_num1 = ''.join(sorted(str_num1))
    sorted_num2 = ''.join(sorted(str_num2))
    
    # Compare the sorted strings
    return sorted_num1 == sorted_num2

# Test cases
num1 = 12345
num2 = 54321

if are_anagrams(num1, num2):
    print(f"{num1} and {num2} are anagrams.")
else:
    print(f"{num1} and {num2} are not anagrams.")

num1 = 12345
num2 = 54320

if are_anagrams(num1, num2):
    print(f"{num1} and {num2} are anagrams.")
else:
    print(f"{num1} and {num2} are not anagrams.")
