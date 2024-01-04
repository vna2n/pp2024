# Establish a dictionary to hold data about students
student_records = {}

# Establish a dictionary to hold data about course
courses = {}

# Establish a dictionary to hold academic scores
grades = {}

# Establish a function to collect data about students
def gather_student_data():
    quantity_of_students = int(input("Enter total student count: "))
    for _ in range(quantity_of_students):
        id_number = input("Enter student ID: ")
        full_name = input("Enter student full name: ")
        birth_date = input("Enter student's birth date: ")
        student_records[id_number] = {"full_name": full_name, "birth_date": birth_date}

# Establish a function to collect data about academic courses
def gather_course_data():
    quantity_of_courses = int(input("Enter total course count: "))
    for _ in range(quantity_of_courses):
        course_ID = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses[course_ID] = {"name": course_name}

# Establish a function to record grades for students in a specific course
def record_grades():
    course_ID = input("Enter the course ID for grade entry: ")
    if course_ID not in courses:
        print("This course ID does not exist.")
        return
    for id_number in student_records:
        score = float(input(f"Enter {student_records[id_number]['full_name']}'s score: "))
        if id_number not in grades:
            grades[id_number] = {}
        grades[id_number][course_ID] = score

# Establish a function to display all courses
def display_courses():
    for course_ID in courses:
        print(f"{course_ID}: {courses[course_ID]['name']}")

# Establish a function to display all student records
def display_students():
    for id_number in student_records:
        print(f"{id_number}: {student_records[id_number]['full_name']} - {student_records[id_number]['birth_date']}")

# Establish a function to reveal grades for a chosen course
def reveal_grades():
    course_ID = input("Enter the course ID to view grades: ")
    if course_ID not in courses:
        print("This course ID is invalid.")
        return
    for id_number in student_records:
        if id_number in grades and course_ID in grades[id_number]:
            print(f"{student_records[id_number]['full_name']}: {grades[id_number][course_ID]}")
        else:
            print(f"{student_records[id_number]['full_name']}: No grade recorded")

# Execution flow of the program
gather_student_data()
gather_course_data()

while True:
    print("Choose an action:")
    print("1. Enter grades for a course")
    print("2. Display all courses")
    print("3. Display all students")
    print("4. View grades for a course")
    print("5. Exit the program")
    user_choice = input("Pick one: ")
    if user_choice == "1":
        record_grades()
    elif user_choice == "2":
        display_courses()
    elif user_choice == "3":
        display_students()
    elif user_choice == "4":
        reveal_grades()
    elif user_choice == "5":
        break
    else:
        print("That's not a valid option, try again!")
