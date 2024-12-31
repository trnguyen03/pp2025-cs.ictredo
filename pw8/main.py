import os
import zipfile
import pickle
import threading

from domains.management import StudentMarkManagement
from input import input_students, input_courses, input_marks
from output import curses_display

PICKLE_FILE = "students.pkl"
ZIP_FILE = "students.dat"


def main():
    management = StudentMarkManagement()

    if os.path.exists(ZIP_FILE):
        print("[INFO] Found existing data file. Decompressing and loading...")
        decompress_data(ZIP_FILE, PICKLE_FILE)
        management = load_management_data(PICKLE_FILE)
        print("[INFO] Data loaded successfully.")
    else:
        print("[INFO] No existing data file found. Please input data.")
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
            print("[INFO] Exiting program. Saving in background...")
            save_thread = threading.Thread(
                target=background_save, 
                args=(management, PICKLE_FILE, ZIP_FILE),
                daemon=False  
            )
            save_thread.start()

            save_thread.join()

            print("[INFO] Data saved. byeeee!")
            break

        else:
            print("Invalid choice. Please try again.")


def background_save(management, pickle_file, zip_file):
    print("[BACKGROUND] Saving data to pickle file...")
    save_management_data(management, pickle_file)
    print("[BACKGROUND] Compressing pickle file into zip...")
    compress_data(pickle_file, zip_file)
    print("[BACKGROUND] Done!")


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
