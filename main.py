class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def email(self):
        return "{}@gmail.com".format(self.name)


class Manager(Employee): # Inheritance parent -> Employee child-> Manager

    def work(self):
        self.domain = input("Enter Manager Domain")
        if self.domain == "DB Administrator":
            self.salary = 100000
        elif self.domain == "trainee programmer":
            self.salary = 30000


class Admin(Employee, Manager): # multiple inheritance Admin -> employee, manager
    def admin(self):
        print("I am a administrator")


if __name__ == "__main__":
    emp = Employee("bhargav", 373)
    print(emp.email())
