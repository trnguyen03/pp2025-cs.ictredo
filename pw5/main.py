import os
import zipfile
from input import input_students, input_courses, input_marks
from output import curses_display
from domains.management import StudentMarkManagement

def main():
    management = StudentMarkManagement()
    if os.path.exists("students.dat"):
        print("[INFO] Detected existing data file 'students.dat'. Decompressing...")
        decompress_data("students.dat")
        load_data_from_files(management)
        print("[INFO] Data loaded from 'students.dat'.")
    else:
        print("[INFO] No existing data file found. You will be prompted for input.")
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
            print("[INFO] Exiting program. Compressing data into 'students.dat' ...")
            compress_data("students.dat")
            print("[INFO] Data compressed successfully. Goodbye tinh iu!")
            break

        else:
            print("Invalid choice. Please try again.")

def load_data_from_files(management):
    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                student_id, name, dob = line.split(",")
                marks_data.append((student_id, course_id, mark))
                
        for sid, cid, mk in marks_data:
            for student in management.get_students():
                if student.get_id() == sid:
                    student.add_mark(cid, mk)

def compress_data(zip_filename):
     with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zf:
         for txt_file in ["students.txt", "courses.txt", "marks.txt"]:
            if os.path.exists(txt_file):
                zf.write(txt_file)

def decompress_data(zip_filename):
    with zipfile.ZipFile(zip_filename, "r") as zf:
        zf.extractall()

if __name__ == "__main__":
    main()
