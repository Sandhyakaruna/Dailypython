def sum_of_proper_divisors(n):
    """Returns the sum of proper divisors of a number."""
    if n < 1:
        return 0
    divisors_sum = 1  # 1 is a proper divisor for all n > 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def are_amicable(num1, num2):
    """Checks if two numbers are an amicable pair."""
    return sum_of_proper_divisors(num1) == num2 and sum_of_proper_divisors(num2) == num1

# Test cases
num1 = 220
num2 = 284

if are_amicable(num1, num2):
    print(f"{num1} and {num2} are an amicable pair.")
else:
    print(f"{num1} and {num2} are not an amicable pair.")

num1 = 1184
num2 = 1210

if are_amicable(num1, num2):
    print(f"{num1} and {num2} are an amicable pair.")
else:
    print(f"{num1} and {num2} are not an amicable pair.")
