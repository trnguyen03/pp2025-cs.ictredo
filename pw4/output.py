import curses

def curses_display(management):
    def draw_menu(stdscr):
        stdscr.clear()
        management.calculate_gpas()
        management.sort_students_by_gpa()
        stdscr.addstr(0, 0, "Student List (Sorted by GPA):")
        for idx, student in enumerate(management.get_students(), start=1):
            stdscr.addstr(idx, 0, str(student))
        stdscr.addstr(len(management.get_students()) + 2, 0, "Press any key to exit...")
        stdscr.refresh()
        stdscr.getch()
    
    curses.wrapper(draw_menu)
