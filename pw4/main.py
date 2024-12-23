from input import input_students, input_courses, input_marks
from output import curses_
from domains.management import StudentMarkManagement

def main():
    management = StudentMarkManagement()

    num_students = int(input("Enter number of students: "))
    input_students(management, num_students)

    num_courses = int(input("\nEnter number of courses: "))
    input_courses(management, num_courses)
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
            for course in management.get_courses():
                print(course)

        elif choice == "2":
            print("\nList of Students:")
            for student in management.get_students():
                print(student)

        elif choice == "3":
            input_marks(management)

        elif choice == "4":
            curses_display(management)

        elif choice == "5":
            print("Goodbyeee !")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
