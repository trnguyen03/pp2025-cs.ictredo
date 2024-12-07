def input_students(num_students):
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (DD/MM/YYYY): ")
        students.append((student_id, name, dob))
    return students

def input_courses(num_courses):
    courses = []
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))
    return courses

def input_marks(courses, students):
    marks = {}
    for course_id, course_name in courses:
        print(f"\nEntering marks for course: {course_name}")
        marks[course_id] = {}
        for student_id, student_name, _ in students:
            while True:
                try:
                    mark = float(input(f"Enter marks for {student_name} (ID: {student_id}): "))
                    marks[course_id][student_id] = mark
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value for marks.")
    return marks

def list_courses(courses):
    print("\nList of Courses:")
    for course_id, course_name in courses:
        print(f"Course ID: {course_id}, Name: {course_name}")

def list_students(students):
    print("\nList of Students:")
    for student_id, name, dob in students:
        print(f"Student ID: {student_id}, Name: {name}, Date of Birth: {dob}")

def show_student_marks(marks, students, courses):
    course_id = input("\nEnter the course ID to show marks: ")
    course_name = next((name for id, name in courses if id == course_id), None)
    if not course_name:
        print("Course not found.")
        return

    print(f"\nMarks for Course: {course_name}")
    for student_id, student_name, _ in students:
        mark = marks.get(course_id, {}).get(student_id, "No marks available")
        print(f"Student: {student_name} (ID: {student_id}), Marks: {mark}")

def main():
    num_students = int(input("Enter number of students: "))
    students = input_students(num_students)

    num_courses = int(input("\nEnter number of courses: "))
    courses = input_courses(num_courses)

    marks = input_marks(courses, students)

    while True:
        print("\nMenu:")
        print("1. List Courses")
        print("2. List Students")
        print("3. Show Marks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            list_courses(courses)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            show_student_marks(marks, students, courses)
        elif choice == "4":
            print("Goodbye my love!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
