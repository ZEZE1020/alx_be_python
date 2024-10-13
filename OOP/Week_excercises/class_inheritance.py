class Animal:
    def eat(self):
        return "Eating..."

    def sleep(self):
        return "Sleeping..."

class Dog(Animal):
    def bark(self):
        return "Woof!"

# Creating an instance of Animal
generic_animal = Animal()

# Creating an instance of Dog
my_dog = Dog()

# Demonstrating method inheritance
print(generic_animal.eat())     # Output: Eating...
print(generic_animal.sleep())   # Output: Sleeping...
print(my_dog.eat())             # Output: Eating... (inherited from Animal)
print(my_dog.sleep())           # Output: Sleeping... (inherited from Animal)
print(my_dog.bark())            # Output: Woof! (specific to Dog)
