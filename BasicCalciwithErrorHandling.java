def main():
    try:
        # Input from the user
        num1 = float(input("Enter the First Number: "))
        num2 = float(input("Enter the Second Number: "))
        operator = input("Enter the Operator (+ - * /): ")

        # Perform the operation based on the operator
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Sorry! Division By Zero is not possible")
            result = num1 / num2
        else:
            raise ValueError("Sorry. You have entered invalid operator")

        print(f"The answer is: {result}")

    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
