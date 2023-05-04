
# To create a registration form using Python,
# we can use the Tkinter library which is a standard GUI (Graphical User Interface) library for Python.
# Here is an example of a simple registration form using Tkinter:


import tkinter as tk

# Create a window
window = tk.Tk()
window.title("Registration Form")

# Create labels
name_label = tk.Label(text="Name:")
name_label.pack()
email_label = tk.Label(text="Email:")
email_label.pack()

# Create entry fields
name_entry = tk.Entry()
name_entry.pack()
email_entry = tk.Entry()
email_entry.pack()

# Create a submit button
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    print("Name: " + name)
    print("Email: " + email)

submit_button = tk.Button(text="Submit", command=submit_form)
submit_button.pack()

# Run the window
window.mainloop()
