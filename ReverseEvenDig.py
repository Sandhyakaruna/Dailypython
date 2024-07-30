def reverse_number(number):
    # Function to check if the number is valid
    def is_valid(number):
        # Check if the number is negative or less than 2 digits
        if number < 10:
            return False
        # Check if the number contains only 0's
        if all(digit == '0' for digit in str(number)):
            return False
        return True
    
    # Generator to yield even digits in reverse order
    def even_digits_reversed(number):
        for digit in reversed(str(number)):
            if int(digit) % 2 == 0:
                yield digit

    # Check if the number is valid
    if not is_valid(number):
        return "Invalid input"

    # Use the generator to get the reversed even digits
    reversed_even_digits = ''.join(even_digits_reversed(number))
    
    # If no even digits are found, return "Invalid input"
    if not reversed_even_digits:
        return "Invalid input"
    
    # Return the reversed even digits as the new password
    return f"Your new password is: {reversed_even_digits}"

# Sample Input 1
input_number = int(input("Enter the number: "))
print(reverse_number(input_number))
