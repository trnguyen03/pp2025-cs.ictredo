from domains.student import Student
from domains.course import Course
import os

def input_students(management, num_students):
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (DD/MM/YYYY): ")
        students = Student((student_id, name, dob))
        management.add_student(student)

    write_students_to_file(management.get_students())


def input_courses(management, num_courses):
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credit = int(input("Enter course credit: "))
        course = Course(course_id, name, credit))
        management.add_course(course)

    write_courses_to_file(management.get_courses())


def input_marks(management):
    for course in management.get_courses():
        print(f"\nEntering marks for course: {course_name}")
        for student in management.get_students():
            while True:
                try:
                    mark = float(input(f"Enter marks for {student.get_name()} (ID: {student.get_id()}): "))
                    student.add_mark(course.get_id(), mark)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
    write_marks_to_file(management.get_students())

def write_students_to_file(students, filename="students.txt")

    with open(filename, "w", encoding="utf-8") as f:
        for student in students:
            f.write("f{student.get_id()},{student.get_name()},{student.get_dob()}\n")

def wrỉte_courses_to_file(courses, filenam="courses.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for course in courses:
            f.write(f"{course.get_id()},{course.get_name()},{course.get_credit()}\n")

def write_marks_to_file(students, filename="marks.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for student in students:
            marks_dict = student.get_marks()
            for course_id, mark in marks_dict.items():
                f.write(f"{student.get_id()},{course_id},{mark}\n")
