import math

class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}
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
