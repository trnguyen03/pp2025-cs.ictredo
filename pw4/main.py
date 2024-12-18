from input import input_students, input_courses, input_marks
from output import display_students_curses
from domains.student import Student
from domains.course import Course
from domains.management import StudentMarkManagement

def main():
    management = StudentMarkManagement()

    raw_students = input_students()
    students = [Student(s_id, name, dob) for s_id, name, dob in raw_students]
    management.add_students(students)

    raw_courses = input_courses()
    courses = [Course(c_id, name, credit) for c_id, name, credit in raw_courses]
    management.add_courses(courses)

    marks = input_marks(raw_students, raw_courses)
    management.add_marks(marks)

    management.calculate_gpas()
    management.sort_students_by_gpa()

    display_students_curses(management.students)

if __name__ == "__main__":
    main()
