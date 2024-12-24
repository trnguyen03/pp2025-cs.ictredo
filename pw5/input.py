from domains.student import Student
from domains.course import Course

def input_students(management, num_students):
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (DD/MM/YYYY): ")
        students = Student((student_id, name, dob))
        management.add_student(student)



def input_courses(management, num_courses):
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credit = int(input("Enter course credit: "))
        course = Course(course_id, name, credit))
        management.add_course(course)



def input_marks(management):
    for course in management.get_courses():
        print(f"\nEntering marks for course: {course.get_name()}")
        for student in management.get_students():
            while True:
                try:
                    mark = float(input(f"Enter marks for {student.get_name()} (ID: {student.get_id()}): "))
                    student.add_mark(course.get_id(), mark)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")


