def divide_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            if num1 == 0:
                raise ZeroDivisionError("Error: The first number cannot be zero.")
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                raise ZeroDivisionError("Error: The second number cannot be zero.")
            result = num1 / num2
        except ZeroDivisionError as e:
            print(e)
            continue  # Restart the loop to allow re-entry of numbers
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue  # Restart the loop to allow re-entry of numbers
        else:
            print(f"The result of {num1} divided by {num2} is {result}")
            break  # Exit the loop if no exceptions are raised

# Run the function
divide_numbers()
