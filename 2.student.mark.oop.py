class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self,course_id, name):
        self.course_id = course_id
        self.name = name
    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}"

class Mark:
    def __init__(self, course, student, mark):
        self.course = course
        self.student = student
        self.mark = mark

class StudentMarkManagement:
  def __init__(self):
    self.students = []
    self.courses = []
    self.mark = []

