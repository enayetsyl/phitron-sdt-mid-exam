from question2 import Student
from question1 import StudentDatabase

def main():
    # Manually create some Student objects (Step 3: done manually)
    # You can create more or fewer as you like. This is just to have some initial data.
    s1 = Student(101, "Alice Johnson", "Computer Science", is_enrolled=True)
    s2 = Student(102, "Bob Smith", "Mathematics")
    s3 = Student(103, "Charlie Brown", "Physics", is_enrolled=False)

    while True:
        print("\n--- Student Management Menu ---")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # View All Students
            if len(StudentDatabase.student_list) == 0:
                print("No students in the database.")
            else:
                for student_obj in StudentDatabase.student_list:
                    student_obj.view_student_info()

        elif choice == "2":
            # Enroll Student
            try:
                student_id_to_enroll = int(input("Enter student ID to enroll: "))
                # Find the student by ID
                student_found = False
                for student_obj in StudentDatabase.student_list:
                    if student_obj.student_id == student_id_to_enroll:
                        student_found = True
                        # Attempt to enroll
                        student_obj.enroll_student()
                        print(f"Student {student_id_to_enroll} enrolled successfully.")
                        break
                if not student_found:
                    print(f"No student found with ID: {student_id_to_enroll}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            # Drop Student
            try:
                student_id_to_drop = int(input("Enter student ID to drop: "))
                # Find the student by ID
                student_found = False
                for student_obj in StudentDatabase.student_list:
                    if student_obj.student_id == student_id_to_drop:
                        student_found = True
                        # Attempt to drop
                        student_obj.drop_student()
                        print(f"Student {student_id_to_drop} dropped successfully.")
                        break
                if not student_found:
                    print(f"No student found with ID: {student_id_to_drop}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
