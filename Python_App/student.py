# Simple Student Management System using Python

# In-memory database (dictionary)
students = {}

def add_student():
    """Add a new student to the database."""
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student ID already exists!")
        return
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    grade = input("Enter Student Grade: ")
    students[student_id] = {"name": name, "age": age, "grade": grade}
    print("Student added successfully!")

def view_students():
    """Display all students in the database."""
    if not students:
        print("No students in the database.")
        return
    print("\nStudent Records:")
    for student_id, details in students.items():
        print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Grade: {details['grade']}")
    print()

def delete_student():
    """Delete a student from the database."""
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student ID not found!")

def main():
    """Main menu for the application."""
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
