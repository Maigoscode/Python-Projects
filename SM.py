import sqlite3

# Establishing a connection to the SQLite database

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Creating the "students" table if it doesn't exist
create_table_query = """CREATE TABLE IF NOT EXISTS students (
                            roll_number INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            age INTEGER,
                            email TEXT
                        );"""
cursor.execute(create_table_query)
conn.commit()


def add_student():
    # Prompting the user to enter student details
    roll_number = int(input("Enter roll number: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")

    # Inserting the student details into the database
    insert_query = "INSERT INTO students VALUES (?, ?, ?, ?);"
    cursor.execute(insert_query, (roll_number, name, age, email))
    conn.commit()
    print("Student added successfully!")


def display_students():
    # Retrieving all students from the database
    select_query = "SELECT * FROM students;"
    cursor.execute(select_query)
    students = cursor.fetchall()

    if len(students) == 0:
        print("No students found.")
    else:
        # Displaying the student information
        print("Student List:")
        for student in students:
            print(f"Roll Number: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Age: {student[2]}")
            print(f"Email: {student[3]}")
            print("-------------------------")


# Main program loop
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

# Closing the database connection
conn.close()
