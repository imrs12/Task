
# 5 - Create a Student class with attributes for name, age, and grades. Include methods to display details and calculate the average grade.

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


student1 = Student("Asad", 20, [85, 90, 92])
student1.display_details()
print(f"Average Grade: {student1.calculate_average_grade()}")

student2 = Student("Roshan", 22, [78, 81, 85])
student2.display_details()
print(f"Average Grade: {student2.calculate_average_grade()}")