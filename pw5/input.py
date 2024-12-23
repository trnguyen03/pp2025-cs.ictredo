def input_students():
    students = []
    num_students = int(input("Enter number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (DD/MM/YYYY): ")
        students.append((student_id, name, dob))
    return students


def input_courses():
    courses = []
    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credit = int(input("Enter course credit: "))
        courses.append((course_id, name, credit))
    return courses


def input_marks(students, courses):
    marks = {}
    for course_id, course_name, _ in courses:
        marks[course_id] = {}
        print(f"\nEntering marks for course: {course_name}")
        for student_id, student_name, _ in students:
            while True:
                try:
                    mark = float(input(f"Enter marks for {student_name} (ID: {student_id}): "))
                    if 0 <= mark <= 20:
                        marks[course_id][student_id] = mark
                        break
                    else:
                        print("Marks must be between 0 and 20.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
    return marks
