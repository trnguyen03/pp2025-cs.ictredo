class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def add_students(self, students):
        self.students = students

    def add_courses(self, courses):
        self.courses = courses

    def add_marks(self, marks):
        self.marks = marks

    def calculate_gpas(self):
        for student in self.students:
            student.calculate_gpa(self.courses)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda x: x.get_gpa(), reverse=True)
