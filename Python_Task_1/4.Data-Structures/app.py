# 4 -  Write a program that stores student data (name, age, grades) in a dictionary and performs CRUD operations.

students = {}

def create_student(name, age, grades):
    students[name] = {'age': age, 'grades': grades}
    print(f"Student {name} added successfully.")

def read_student(name):
    if name in students:
        print(f"Name: {name}, Age: {students[name]['age']}, Grades: {students[name]['grades']}")
    else:
        print(f"Student {name} not found.")

def update_student(name, age=None, grades=None):
    if name in students:
        if age is not None:
            students[name]['age'] = age
        if grades is not None:
            students[name]['grades'] = grades
        print(f"Student {name} updated successfully.")
    else:
        print(f"Student {name} not found.")

def delete_student(name):
    if name in students:
        del students[name]
        print(f"Student {name} deleted successfully.")
    else:
        print(f"Student {name} not found.")

# Example usage
create_student("Asad", 20, [85, 90, 92])
create_student("Pratham", 22, [78, 81, 85])
read_student("Asad")
update_student("Asad", grades=[88, 91, 95])
read_student("Asad")
delete_student("Pratham")
read_student("Pratham")