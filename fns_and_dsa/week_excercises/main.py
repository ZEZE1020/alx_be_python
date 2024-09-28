# main.py

import calculator

def main():
    num1 = float(input("Enter your first number:) "))
    num2 = float(input("Enter your second number:) "))

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

if __name__ == "__main__":
    main()
