class Student:

    def __init__(self, name, roll_no, age):
        self.name = name
        self.roll_no = roll_no
        self.age = age

    def display(self):
        print("Name of Student is-", self.name)
        print("Roll No of Student is-", self.roll_no)
        print("Age of Student is-", self.age)


std = Student("Raver", 34, 13)

# print(std.name)
# print(std.roll_no)
# print(std.age)
std.display()

stdunt = Student("Ran veer", 35, 14)
stdunt.display()