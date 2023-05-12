# Text Editor:
# Create a script that allows users to edit text files using the tkinter module,
# allowing users to open, edit, and save text files.

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
with open(file_path, "r") as f:
  text = f.read()

text_box = tk.Text()
text_box.insert(tk.END, text)
text_box.pack()

save_button = tk.Button(text="Save")
save_button.pack()

def save_file():
  with open(file_path, "w") as f:
    f.write(text_box.get("1.0", tk.END))

save_button.config(command=save_file)

root.mainloop()
