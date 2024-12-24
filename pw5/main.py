import os
import zipfile
from input import input_students, input_courses, input_marks
from output import curses_display
from domains.management import StudentMarkManagement
import pickle

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

def save_management_data(management, pickle_file):
    with open(pickle_file, "wb") as f:
        pickle.dump(management, f)

def load_management_data(pickle_file):
    with open(pickle_file, "rb") as f:
        management_obj = pickle.load(f)
    return management_obj

def compress_data(input_file, archive_file):
    with zipfile.ZipFile(archive_file, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(input_file)
        
def decompress_data(archive_file, output_file):
 with zipfile.ZipFile(archive_file, "r") as zf:
        zf.extractall()
    
if __name__ == "__main__":
    main()
