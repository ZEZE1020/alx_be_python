class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")

def collect_student_data():
    students = []
    while True:
        name = input("Enter student name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        age = int(input("Enter student age: "))
        students.append(Student(name, age))
    return students

def display_all_students(students):
    for student in students:
        student.display_info()

# Collect and display student data
students = collect_student_data()
display_all_students(students)
