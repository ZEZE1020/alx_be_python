class ValueTooHighError(Exception):
    """Exception raised for errors in the input value.

    Attributes:
        value -- input value which caused the error
        message -- explanation of the error
    """
    def __init__(self, value, message="Value is too high"):
        self.value = value
        self.message = message
        super().__init__(self.message)

def check_value(number):
    if number > 100:
        raise ValueTooHighError(number)

def main():
    try:
        number = float(input("Enter a number: "))
        check_value(number)
        print(f"The number {number} is within the acceptable range.")
    except ValueTooHighError as e:
        print(f"Error: {e.message}. The value entered was {e.value}.")
      
    except ValueError:
        print("Error: Please enter a valid number.")
# Run the main function
main()
