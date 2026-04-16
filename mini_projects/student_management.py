# =====================================
# Student Management System
# =====================================

# List to store student records
students = []


# ------------------------------
# Add Student
# ------------------------------
def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


# ------------------------------
# View Students
# ------------------------------
def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\nStudent List:")
    for i in range(len(students)):
        s = students[i]
        print(f"{i+1}. Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")


# ------------------------------
# Update Student
# ------------------------------
def update_student():
    view_students()

    if len(students) == 0:
        return

    try:
        index = int(input("Enter student number to update: ")) - 1

        if index >= 0 and index < len(students):
            name = input("Enter new name (leave blank to keep same): ")
            age = input("Enter new age: ")
            course = input("Enter new course: ")

            if name != "":
                students[index]["name"] = name
            if age != "":
                students[index]["age"] = age
            if course != "":
                students[index]["course"] = course

            print("Student updated successfully!")
        else:
            print("Invalid number.")

    except:
        print("Invalid input.")


# ------------------------------
# Delete Student
# ------------------------------
def delete_student():
    view_students()

    if len(students) == 0:
        return

    try:
        index = int(input("Enter student number to delete: ")) - 1

        if index >= 0 and index < len(students):
            removed = students.pop(index)
            print(f"Deleted student: {removed['name']}")
        else:
            print("Invalid number.")

    except:
        print("Invalid input.")


# ------------------------------
# Menu
# ------------------------------
def show_menu():
    print("\n===== Student Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")


# ------------------------------
# Main Function
# ------------------------------
def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            add_student()

        elif choice == '2':
            view_students()

        elif choice == '3':
            update_student()

        elif choice == '4':
            delete_student()

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice.")


# ------------------------------
# Entry Point
# ------------------------------
if __name__ == "__main__":
    main()