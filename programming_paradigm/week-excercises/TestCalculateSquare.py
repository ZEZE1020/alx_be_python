def calculate_square(number):
    # Intentional bug: using addition instead of multiplication
    return number + number

# Example usage
num = input("Please enter a number: ")
result = calculate_square(num)
print(f"The square of {num} is {result}")
