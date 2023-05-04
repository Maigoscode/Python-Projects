import tkinter as tk
from tkcalendar import Calendar, DateEntry

root = tk.Tk()
root.title("Calendar Popup")

cal = Calendar(root, selectmode="day", year=2021, month=5, day=22)
date_entry = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd", calendar=cal)
date_entry.grid(row=0, column=0)

root.mainloop()
