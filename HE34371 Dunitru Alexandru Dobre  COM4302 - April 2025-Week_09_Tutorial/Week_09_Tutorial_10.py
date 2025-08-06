students = {
    "Mizan": {"IT": 86, "Science": 69},
    "Ram": {"IT": 75, "Science": 46},
    "John": {"IT": 35, "Science": 50},
    "Ann": {"IT": 55, "Science": 76},
    "Chris": {"IT": 45, "Science": 65}
}

def calculate_grades(data):
    for student, subjects in data.items():
        avg = sum(subjects.values()) / len(subjects)
        if avg >= 70:
            grade = "Distinction"
        elif avg >= 60:
            grade = "Merit"
        elif avg >= 40:
            grade = "Pass"
        else:
            grade = "Fail"
        print(student, "Grade:", grade)

def search_student(name):
    print(students.get(name, "Student not found"))

def student_menu():
    while True:
        print("\n1. Display All\n2. Display Grades\n3. Search Student\n4. Quit")
        option = input("Choose option: ")
        if option == "1":
            print(students)
        elif option == "2":
            calculate_grades(students)
        elif option == "3":
            name = input("Enter student name: ")
            search_student(name)
        elif option == "4":
            break
        else:
            print("Invalid option")

student_menu()