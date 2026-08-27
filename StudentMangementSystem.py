#STUDENT CLASS MANAGEMENT SYSTEM
class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)


s1 = Student("Youraj", 101, "BTech")
s2 = Student("Raghuraj", 102, "BBA")
s3 = Student("Raunak", 103, "MBA")

print("Student 1 Details")
s1.display()

print("\nStudent 2 Details")
s2.display()

print("\nStudent 3 Details")
s3.display()