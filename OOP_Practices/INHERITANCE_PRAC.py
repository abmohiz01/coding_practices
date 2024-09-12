'''Inheritance of employyee and persons class'''
class Person():

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def details(self):
        print("Employee name is :", self.name)
        print("Employee age is :", self.age)

class Employee(Person):
    def __init__(self,name,age, salary, role):
        self.salary = salary
        self.role = role

        Person.__init__(self,name, age)

    def identity(self):
        print("salary is ",self.salary)
        print("role is ",self.salary)


emp1 = Employee("haris",19,23000,"Developer")
emp1.details()
emp1.identity()