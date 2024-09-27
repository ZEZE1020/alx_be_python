# Function to get the list of fruits from the user
num_fruits = int(input("How many fruits do you like? "))
    
fruits = []
def get_fruits():
    
    for i in range(num_fruits):
        fruit = input(f"Enter the name of fruit {i+1}: ")
        fruits.append(fruit)
    
    return fruits

fruits_list = get_fruits()


def fruits():
    # Get the list of fruits from the user
    
    # Print the list of fruits
    print("You like the following fruits:")
    for fruit in fruits_list:
        print(fruit)

# Run the main function
if len(fruits_list) > 1:
      print(f"The second fruit you like is: {fruits_list[1]}")
else:
    print(f"It's wonderful that you only like {fruits_list[0]}.")

fruits()
