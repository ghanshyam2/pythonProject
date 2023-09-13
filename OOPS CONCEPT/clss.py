class Employee:
    def __init__(self, e_no, e_name, e_sal, e_add):
        self.e_no = e_no
        self.e_name = e_name
        self.e_sal = e_sal
        self.e_add = e_add

    def display(self):
        print("*" * 20)
        print("Employee Number -", self.e_no)
        print("Employee Name -", self.e_name)
        print("Employee Salary -", self.e_sal)
        print("Employee Address -", self.e_add)
        print("*" * 20)


emp = Employee(100, "Ranch", 45000, "Varanasi")  # object created
emp.display()
