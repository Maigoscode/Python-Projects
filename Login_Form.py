
# Login Form:


import tkinter as tk

def submit_login():
    email = email_entry.get()
    password = password_entry.get()

    # Here you can validate the user credentials
    print("Email: " + email)
    print("Password: " + password)

# Create a window
login_window = tk.Tk()
login_window.title("Login Form")

# Create labels
email_label = tk.Label(login_window, text="Email:")
email_label.pack()
password_label = tk.Label(login_window, text="Password:")
password_label.pack()

# Create entry fields
email_entry = tk.Entry(login_window)
email_entry.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

# Create a submit button
submit_button = tk.Button(login_window, text="Submit", command=submit_login)
submit_button.pack()

# Run the window
login_window.mainloop()
