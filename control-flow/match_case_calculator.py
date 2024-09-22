
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    num1 = get_number("Enter the first number:  ")
    num2 = get_number("Enter the second number: ")
    operation = input("Choose the operation (+, -, *, /): ")

    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero."
        case _:
            result = "Invalid operation."

    print(f"The result is {result}")

if __name__ == "__main__":
    main()
