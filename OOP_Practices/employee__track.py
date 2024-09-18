'''
Write a class Employee that keeps track of the number of employees created and allows setting and getting employee details.
'''

class Employee():

    total_employees = 0
    def __init__(self,name: str,age: int,department:str):
        self.name = name
        self.age = age
        self.department = department

        Employee.total_employees += 1

    @property
    def employee(self):
       return f"Employee name :{self.name}, age: {self.age}, department {self.department}"

    @employee.setter
    def employee(self,info_dict :dict):
        self.name = info_dict["name"]
        self.age = info_dict["age"]
        self.department = info_dict["department"]


        # return f"change_name :{newName}, age : {newage}, department : {newdepartment}"

    #Allow to access class variable
    @classmethod
    def totalEmployess(self):
        return f"Total Employees are {Employee.total_employees}"




obj = Employee("name",21,"HR")
print(obj.employee)
obj2 = Employee("abrar",23,"HR")

obj.employee = {
        "name" : "newName",
        "age" : 30,
        "department" : "newdepartment"
        }
print(obj.employee)
print(obj2.employee)
print("Total Employees are :", obj.total_employees)
