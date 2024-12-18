import curses

def display_students_curses(students):
    def draw_menu(stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Student List (Sorted by GPA):")
        for idx, student in enumerate(students, start=1):
            stdscr.addstr(idx, 0, str(student))
        stdscr.addstr(len(students) + 2, 0, "Press any key to exit...")
        stdscr.refresh()
        stdscr.getch()
    
    curses.wrapper(draw_menu)
