from .student import Student
from .course import Course

class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_students(self, student: Student):
       self.students.append(student)

    def get_students(self):
        return self.students

    def add_courses(self, course: Course):
        self.courses.append(course)

    def get_courses(self):
        return self.courses

    def calculate_gpas(self):
        for student in self.students:
            student.calculate_gpa(self.courses)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda x: x.get_gpa(), reverse=True)
