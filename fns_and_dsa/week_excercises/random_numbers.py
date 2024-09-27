import random

# Function to generate a random set of numbers
def generate_random_numbers(n):
    numbers = [random.randint(1, 10) for _ in range(n)]
    return numbers

# Function to remove duplicates and display unique numbers
def display_unique_numbers(numbers):
    unique_numbers = set(numbers)
    print("Unique numbers:", unique_numbers)

# Main function
def main():
    # Generate a random set of numbers
    random_numbers = generate_random_numbers(10)
    
    # Display the generated numbers
    print("Generated numbers:", random_numbers)
    
    # Display the unique numbers
    display_unique_numbers(random_numbers)

# Run the main function
if __name__ == "__main__":
    main()
