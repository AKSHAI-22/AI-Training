class Employee:
    def __init__(self, salary):
        self.__salary = salary  

    def update_salary(self, amount):
        if amount > 0:
            self.__salary = amount
            print("Salary updated")

    def get_salary(self):
        return self.__salary

emp = Employee(30000)
emp.update_salary(40000)
print("Salary:", emp.get_salary())
