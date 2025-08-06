students = {
    "Mizan": {"IT": 86, "Science": 69},
    "Ram": {"IT": 75, "Science": 46},
    "John": {"IT": 35, "Science": 50},
    "Ann": {"IT": 55, "Science": 76},
    "Chris": {"IT": 45, "Science": 65}
}

def total_marks(data):
    for student, subjects in data.items():
        print(student, "Total:", sum(subjects.values()))

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

total_marks(students)
calculate_grades(students)
search_student("Ram")