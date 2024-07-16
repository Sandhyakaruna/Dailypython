def base_to_decimal(num, base):
    """Convert a number from a given base to decimal."""
    return int(num, base)

def decimal_to_base(n, base):
    """Convert a decimal number to a given base."""
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return ''.join(str(x) for x in digits[::-1])

def add_in_base(num1, num2, base):
    """Add two numbers in the given base."""
    # Convert the numbers to decimal
    decimal_num1 = base_to_decimal(num1, base)
    decimal_num2 = base_to_decimal(num2, base)
    
    # Add the numbers in decimal
    decimal_sum = decimal_num1 + decimal_num2
    
    # Convert the sum back to the given base
    return decimal_to_base(decimal_sum, base)

# Test case
num1 = "1010"
num2 = "11001"
base = 2
result = add_in_base(num1, num2, base)
print(f"The sum of {num1} and {num2} in base {base} is: {result}")
