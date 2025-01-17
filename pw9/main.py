import os
import pickle
import zipfile
import threading
import tkinter as tk
from tkinter import ttk, messagebox

from domains.management import StudentMarkManagement
from domains.student import Student
from domains.course import Course
TK_SILENCE_DEPRECATION=1

PICKLE_FILE = "students.pkl"
ZIP_FILE = "students.dat"

def main():
    management = StudentMarkManagement()
    if os.path.exists(ZIP_FILE):
        decompress_data(ZIP_FILE, PICKLE_FILE)
        management = load_management_data(PICKLE_FILE)

    root = tk.Tk()
    root.title("Student Mark Management (Tkinter)")

    frm = ttk.Frame(root, padding=10)
    frm.grid(row=0, column=0, sticky="nsew")

    ttk.Button(frm, text="Add Student", command=lambda: open_add_student_window(root, management)).grid(row=0, column=0, pady=5, sticky="ew")
    ttk.Button(frm, text="Add Course", command=lambda: open_add_course_window(root, management)).grid(row=1, column=0, pady=5, sticky="ew")
    ttk.Button(frm, text="Input Marks", command=lambda: open_input_marks_window(root, management)).grid(row=2, column=0, pady=5, sticky="ew")
    ttk.Button(frm, text="View Students", command=lambda: view_students_window(root, management)).grid(row=3, column=0, pady=5, sticky="ew")
    ttk.Button(frm, text="View Courses", command=lambda: view_courses_window(root, management)).grid(row=4, column=0, pady=5, sticky="ew")
    ttk.Button(frm, text="Calculate & View GPA", command=lambda: calculate_gpa_window(root, management)).grid(row=5, column=0, pady=5, sticky="ew")

    ttk.Button(frm, text="Exit & Save", command=lambda: on_exit(root, management)).grid(row=6, column=0, pady=10, sticky="ew")

    root.mainloop()


def open_add_student_window(parent, management):
    win = tk.Toplevel(parent)
    win.title("Add Student")

    tk.Label(win, text="Student ID:").grid(row=0, column=0, padx=5, pady=5)
    entry_id = tk.Entry(win)
    entry_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(win, text="Name:").grid(row=1, column=0, padx=5, pady=5)
    entry_name = tk.Entry(win)
    entry_name.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(win, text="DOB:").grid(row=2, column=0, padx=5, pady=5)
    entry_dob = tk.Entry(win)
    entry_dob.grid(row=2, column=1, padx=5, pady=5)

    def save_student():
        sid = entry_id.get().strip()
        name = entry_name.get().strip()
        dob = entry_dob.get().strip()
        if sid and name and dob:
            management.add_student(Student(sid, name, dob))
            messagebox.showinfo("Info", f"Student {name} added successfully!")
            win.destroy()
        else:
            messagebox.showwarning("Warning", "Please fill all fields.")

    ttk.Button(win, text="Save", command=save_student).grid(row=3, column=0, columnspan=2, pady=10)


def open_add_course_window(parent, management):
    win = tk.Toplevel(parent)
    win.title("Add Course")

    tk.Label(win, text="Course ID:").grid(row=0, column=0, padx=5, pady=5)
    entry_id = tk.Entry(win)
    entry_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(win, text="Name:").grid(row=1, column=0, padx=5, pady=5)
    entry_name = tk.Entry(win)
    entry_name.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(win, text="Credit:").grid(row=2, column=0, padx=5, pady=5)
    entry_credit = tk.Entry(win)
    entry_credit.grid(row=2, column=1, padx=5, pady=5)

    def save_course():
        cid = entry_id.get().strip()
        name = entry_name.get().strip()
        credit_str = entry_credit.get().strip()
        if cid and name and credit_str:
            try:
                credit = int(credit_str)
                management.add_course(Course(cid, name, credit))
                messagebox.showinfo("Info", f"Course {name} added successfully!")
                win.destroy()
            except ValueError:
                messagebox.showwarning("Warning", "Credit must be an integer.")
        else:
            messagebox.showwarning("Warning", "Please fill all fields.")

    ttk.Button(win, text="Save", command=save_course).grid(row=3, column=0, columnspan=2, pady=10)


def open_input_marks_window(parent, management):
    win = tk.Toplevel(parent)
    win.title("Input Marks")

    tk.Label(win, text="Student:").grid(row=0, column=0, padx=5, pady=5)
    student_var = tk.StringVar(win)
    students = management.get_students()
    student_var.set(students[0].get_id() if students else "")
    student_menu = ttk.OptionMenu(win, student_var, *[s.get_id() for s in students])
    student_menu.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(win, text="Course:").grid(row=1, column=0, padx=5, pady=5)
    course_var = tk.StringVar(win)
    courses = management.get_courses()
    course_var.set(courses[0].get_id() if courses else "")
    course_menu = ttk.OptionMenu(win, course_var, *[c.get_id() for c in courses])
    course_menu.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(win, text="Mark:").grid(row=2, column=0, padx=5, pady=5)
    entry_mark = tk.Entry(win)
    entry_mark.grid(row=2, column=1, padx=5, pady=5)

    def save_mark():
        sid = student_var.get()
        cid = course_var.get()
        m_str = entry_mark.get().strip()
        if not sid or not cid:
            messagebox.showerror("Error", "No student/course available or selected.")
            return
        try:
            mark_val = float(m_str)
        except ValueError:
            messagebox.showwarning("Warning", "Mark must be a number.")
            return

        for s in management.get_students():
            if s.get_id() == sid:
                s.add_mark(cid, mark_val)
                messagebox.showinfo("Info", f"Mark {mark_val} added for Student {sid}, Course {cid}.")
                win.destroy()
                return

    ttk.Button(win, text="Save", command=save_mark).grid(row=3, column=0, columnspan=2, pady=10)


def view_students_window(parent, management):
    win = tk.Toplevel(parent)
    win.title("View Students")

    txt = tk.Text(win, width=50, height=10)
    txt.pack(padx=10, pady=10)

    for s in management.get_students():
        txt.insert(tk.END, str(s) + "\n")


def view_courses_window(parent, management):
    win = tk.Toplevel(parent)
    win.title("View Courses")

    txt = tk.Text(win, width=50, height=10)
    txt.pack(padx=10, pady=10)

    for c in management.get_courses():
        txt.insert(tk.END, str(c) + "\n")


def calculate_gpa_window(parent, management):
    win = tk.Toplevel(parent)
    win.title("Calculate & View GPA")

    management.calculate_gpas()
    management.sort_students_by_gpa()

    txt = tk.Text(win, width=60, height=12)
    txt.pack(padx=10, pady=10)

    for s in management.get_students():
        txt.insert(tk.END, f"{s.get_id()} - {s.get_name()} - GPA: {s.get_gpa():.2f}\n")


def on_exit(root, management):
    if messagebox.askokcancel("Quit", "Do you really want to save & quit?"):
        save_thread = threading.Thread(
            target=background_save,
            args=(management, PICKLE_FILE, ZIP_FILE),
            daemon=False
        )
        save_thread.start()
        save_thread.join()
        root.destroy()


def background_save(management, pickle_file, zip_file):
    save_management_data(management, pickle_file)
    compress_data(pickle_file, zip_file)


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
