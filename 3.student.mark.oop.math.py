import math
import numpy as np
import curses


class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}  # Marks per course
        self.__gpa = 0.0

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def add_mark(self, course_id, mark):
        rounded_mark = math.floor(mark * 10) / 10 
        self.__marks[course_id] = rounded_mark

    def get_marks(self):
        return self.__marks

    def calculate_gpa(self, courses):
        total_weighted_sum = 0
        total_credits = 0
        for course in courses:
            if course.get_id() in self.__marks:
                credit = course.get_credit()
                mark = self.__marks[course.get_id()]
                total_weighted_sum += credit * mark
                total_credits += credit
        self.__gpa = total_weighted_sum / total_credits if total_credits > 0 else 0
        return self.__gpa

    def get_gpa(self):
        return self.__gpa

    def __str__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, GPA: {self.__gpa:.2f}"


class Course:
    def __init__(self, course_id, name, credit):
        self.__course_id = course_id
        self.__name = name
        self.__credit = credit

    def get_id(self):
        return self.__course_id

    def get_name(self):
        return self.__name

    def get_credit(self):
        return self.__credit

    def __str__(self):
        return f"Course ID: {self.__course_id}, Name: {self.__name}, Credit: {self.__credit}"


class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self, num_students):
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (DD/MM/YYYY): ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self, num_courses):
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credit = int(input("Enter course credit: "))
            self.courses.append(Course(course_id, name, credit))

    def input_marks(self):
        for course in self.courses:
            print(f"\nEntering marks for course: {course.get_name()}")
            for student in self.students:
                while True:
                    try:
                        mark = float(input(f"Enter marks for {student.get_name()} (ID: {student.get_id()}): "))
                        student.add_mark(course.get_id(), mark)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

    def calculate_gpas(self):
        for student in self.students:
            student.calculate_gpa(self.courses)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda x: x.get_gpa(), reverse=True)

    def curses_display(self):
        def draw_menu(stdscr):
            stdscr.clear()
            self.calculate_gpas()
            self.sort_students_by_gpa()
            stdscr.addstr(0, 0, "Student List (Sorted by GPA):")
            for idx, student in enumerate(self.students, start=1):
                stdscr.addstr(idx, 0, str(student))
            stdscr.addstr(len(self.students) + 2, 0, "Press any key to exit...")
            stdscr.refresh()
            stdscr.getch()

        curses.wrapper(draw_menu)

    def main_menu(self):
        while True:
            print("\nMenu:")
            print("1. List Courses")
            print("2. List Students")
            print("3. Input Marks")
            print("4. Show GPA (Curses UI)")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                print("\nList of Courses:")
                for course in self.courses:
                    print(course)
            elif choice == "2":
                print("\nList of Students:")
                for student in self.students:
                    print(student)
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.curses_display()
            elif choice == "5":
                print("byeeeeeeeee!")
                break
            else:
                print("oops. Please try again.")


if __name__ == "__main__":
    management = StudentMarkManagement()
    num_students = int(input("Enter number of students: "))
    management.input_students(num_students)

    num_courses = int(input("\nEnter number of courses: "))
    management.input_courses(num_courses)

    management.main_menu()
