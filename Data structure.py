#Write a program that stores student data (name, age, grades)
# in a dictionary and performs CRUD operations.

class Student:
    def __init__(self, name, roll_no, m1, m2, m3, m4, m5):
        # Initialize student data
        self.name = name
        self.roll_no = roll_no
        self.marks = [m1, m2, m3, m4, m5]

    def __str__(self):
        # String representation of student
        return (f"Name: {self.name}, RollNo: {self.roll_no}, "
                f"Marks: {', '.join(map(str, self.marks))}")


class StudentManager:
    def __init__(self):
        # Initialize the list to hold student objects
        self.students = []

    def accept(self, name, roll_no, m1, m2, m3, m4, m5):
        # Accept and add a new student
        student = Student(name, roll_no, m1, m2, m3, m4, m5)
        self.students.append(student)
        print(f"Student {name} added successfully.")

    def display(self):
        # Display all students
        if not self.students:
            print("No students found!")
        else:
            print("\nList of Students:")
            for student in self.students:
                print(student)

    def search(self, roll_no):
        # Search for a student by roll number
        for student in self.students:
            if student.roll_no == roll_no:
                return student
        return None

    def delete(self, roll_no):
        # Delete a student by their roll number
        student = self.search(roll_no)
        if student:
            self.students.remove(student)
            print(f"Student with RollNo {roll_no} deleted successfully.")
        else:
            print(f"Student with RollNo {roll_no} not found.")

    def update(self, roll_no, new_name=None, new_roll_no=None):
        # Update a student's name or roll number
        student = self.search(roll_no)
        if student:
            if new_name:
                student.name = new_name
                print(f"Name updated to {new_name}.")
            if new_roll_no:
                student.roll_no = new_roll_no
                print(f"RollNo updated to {new_roll_no}.")
        else:
            print(f"Student with RollNo {roll_no} not found.")


# Main program
def main():
    manager = StudentManager()
    while True:
        print("\nOperations:")
        print("1. Accept Student Details")
        print("2. Display Student Details")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student Details")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter Name: ")
            roll_no = int(input("Enter RollNo: "))
            marks = [int(input(f"Enter Marks{i+1}: ")) for i in range(5)]
            manager.accept(name, roll_no, *marks)

        elif choice == "2":
            manager.display()

        elif choice == "3":
            roll_no = int(input("Enter RollNo to search: "))
            student = manager.search(roll_no)
            if student:
                print("Student Found:")
                print(student)
            else:
                print(f"Student with RollNo {roll_no} not found.")

        elif choice == "4":
            roll_no = int(input("Enter RollNo to delete: "))
            manager.delete(roll_no)

        elif choice == "5":
            roll_no = int(input("Enter RollNo to update: "))
            new_name = input("Enter new Name (or press Enter to skip): ") or None
            new_roll_no = input("Enter new RollNo (or press Enter to skip): ")
            new_roll_no = int(new_roll_no) if new_roll_no else None
            manager.update(roll_no, new_name, new_roll_no)

        elif choice == "6":
            print("Thank you! Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
