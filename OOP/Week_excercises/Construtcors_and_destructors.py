class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name} has been created.")

    def __del__(self):
        print(f"Person {self.name} has been deleted.")

# Creating an instance of Person
p = Person("Alice", 30)

# Deleting the instance
del p
