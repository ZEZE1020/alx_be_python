def read_file():
    while True:
        try:
            file_name = input("Enter the file name to read: ")
            with open(file_name, 'r') as file:
                data = file.read()
                print("File content:")
                print(data)
            break  # Exit the loop if the file is successfully read
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' does not exist. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the function
read_file()
