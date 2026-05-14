# This program demonstrates the use of classes and objects in Python.
# A Student class is created to store student details and subject marks.
# The user enters the number of subjects, subject names,
# and marks obtained in each subject.
# The program calculates the total marks and percentage
# and displays the complete student record.



class student:
    def __init__(self):
        self.rollno = 0
        self.name = ""
        self.subjects = {}
        self.total = 0
        self.percentage = 0

    def get_student(self):
        self.rollno = int(input("Enter roll no: "))
        self.name = input("Enter student name: ")

        n = int(input("Enter number of subjects: "))

        for i in range(n):
            subject = input("Enter subject name: ")
            marks = float(input(f"Enter marks in {subject} out of 100: "))

            self.subjects[subject] = marks
            self.total += marks

        self.percentage = self.total / n

    def display_student(self):
        print("\n ------------------ STUDENT DETAILS ------------------\n")
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("\nSubject Marks:")
        for subject, marks in self.subjects.items():
            print(f"{subject} : {marks}")
        print("\nTotal Marks:", self.total)
        print(f"Percentage: {self.percentage:.2f}%")
        print()

    
stud1 = student()
stud2 = student()

stud1.get_student()
stud2.get_student()

stud1.display_student()
stud2.display_student()


