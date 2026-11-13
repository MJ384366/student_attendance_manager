import json
import os

FILE_NAME = "attendance.txt"

students = []


# Load student records from file
def load_data():
    global students

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    else:
        students = []


# Save student records to file
def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)
        
        # Add a new student
def add_student():
    roll = input("Enter roll number: ").strip()

    if not roll:
        print("Roll number cannot be empty.")
        return

    # Check duplicate roll number
    for student in students:
        if student["roll"] == roll:
            print("Roll number already exists.")
            return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    # Create student dictionary
    student = {
        "roll": roll,
        "name": name,
        "held": 0,
        "attended": 0
    }

    # Add student to list
    students.append(student)

    # Save records
    save_data()

    print(
        f"Student added: {roll} | {name} | "
        "Held: 0 | Attended: 0"
    )
    # Mark student attendance
def mark_attendance():
    roll = input("Enter roll number: ").strip()

    student = None

    for s in students:
        if s["roll"] == roll:
            student = s
            break

    if student is None:
        print(f"Roll number {roll} not found.")
        return

    status = input("Enter status (P/A): ").strip().upper()

    if status not in ["P", "A"]:
        print("Invalid status. Enter P or A.")
        return

    student["held"] += 1

    if status == "P":
        student["attended"] += 1

    save_data()

    print("Attendance marked successfully.")




# Show attendance percentage
def show_percentage():
    roll = input("Enter roll number: ").strip()

    for student in students:
        if student["roll"] == roll:

            if student["held"] == 0:
                print(
                    f'{student["name"]}: '
                    'Attendance 0.00% (no classes held yet)'
                )
                return

            percentage = (
                student["attended"] / student["held"]
            ) * 100

            print(
                f'{student["name"]}: '
                f'Attendance {percentage:.2f}%'
            )
            return

    print(f"Roll number {roll} not found.")
    
    # Show students with attendance below 75%
def show_shortage():
    print("\nStudents with attendance below 75%:")
    found = False

    for student in students:
        if student["held"] == 0:
            continue

        percentage = (
            student["attended"] / student["held"]
        ) * 100

        if percentage < 75:
            print(
                f'{student["roll"]} - '
                f'{student["name"]} - '
                f'{percentage:.2f}%'
            )
            found = True

    if not found:
        print("No students have attendance below 75%.")
        
        # Main Menu
def main_menu():
    while True:
        print("\n===== STUDENT ATTENDANCE MANAGER =====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Show Attendance Percentage")
        print("4. Show Attendance Shortage")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            show_percentage()
        elif choice == "4":
            show_shortage()
        elif choice == "5":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice!")


# Run the program
if __name__ == "__main__":
    load_data()
    main_menu()