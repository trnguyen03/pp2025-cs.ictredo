class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        
    def get_id(self):
        return self.__student_id
        
    def get_name(self):
        return self.__name
        
    def get_dob(self):
        return self.__dob

    def __str__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, DoB: {self.__dob}"

class Course:
    def __init__(self,course_id, name):
        self.__course_id = course_id
        self.__name = name
        self.__mark = {}
    def get_id(self):
        return self.__course_id

    def get_name(self):
        return self.__name
        
    def add_mark(self, student_id, mark):
        self.__marks[student_id] = mark

    def get_mark(self, student_id):
        return self.__marks.get(student_id, None)

    def __str__(self):
        return f"Course ID: {self.__course_id}, Name: {self.__name}"
  
    def display_marks(self, students):
        print(f"\n Marks for course: {self.__name}")
        for student in students:
            mark = self.__marks.get(student.get_id(), "No marks available")
            print(f"(student.get_name()} (ID: {student.get_id()}): {mark}")
            
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
            self.courses.append(Course(course_id, name))

    def input_marks(self):
        for course in self.courses:
            print(f"\nEntering marks for course: {course.get_name()}")
            for student in self.students:
                while True:
                    try:
                        mark = float(input(f"Enter marks for {student.get_name()} (ID: {student.get_id()}): "))
                        course.add_mark(student.get_id(), mark)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(course)

    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(student)

    def show_student_marks(self):
        course_id = input("\nEnter the course ID to show marks: ")
        course = next((c for c in self.courses if c.get_id() == course_id), None)
        if not course:
            print("Course not found.")
            return
        course.display_marks(self.students)

    def main_menu(self):
        while True:
            print("\nMenu:")
            print("1. List Courses")
            print("2. List Students")
            print("3. Input Marks")
            print("4. Show Marks")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.list_courses()
            elif choice == "2":
                self.list_students()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.show_student_marks()
            elif choice == "5":
                print("Goodbye hihi!")
                break
            else:
                print("Nope. Please try again.")


if __name__ == "__main__":
    management = StudentMarkManagement()
    num_students = int(input("Enter number of students: "))
    management.input_students(num_students)

    num_courses = int(input("\nEnter number of courses: "))
    management.input_courses(num_courses)

    management.main_menu()
