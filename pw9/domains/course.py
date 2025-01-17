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
