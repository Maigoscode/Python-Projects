
# Registration Form:


import tkinter as tk

def submit_registration():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Here you can save the data to a database or file
    print("Name: " + name)
    print("Email: " + email)
    print("Password: " + password)

# Create a window
registration_window = tk.Tk()
registration_window.title("Registration Form")

# Create labels
name_label = tk.Label(registration_window, text="Name:")
name_label.pack()
email_label = tk.Label(registration_window, text="Email:")
email_label.pack()
password_label = tk.Label(registration_window, text="Password:")
password_label.pack()

# Create entry fields
name_entry = tk.Entry(registration_window)
name_entry.pack()
email_entry = tk.Entry(registration_window)
email_entry.pack()
password_entry = tk.Entry(registration_window, show="*")
password_entry.pack()

# Create a submit button
submit_button = tk.Button(registration_window, text="Submit", command=submit_registration)
submit_button.pack()

# Run the window
registration_window.mainloop()
