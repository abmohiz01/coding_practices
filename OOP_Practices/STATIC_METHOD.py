'''Static method is used when Instance of class is not required'''

class Math():

    def __init__(self, num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num + n
        print(self.num)


    @staticmethod
    def add(a,b):
        return a + b

class Employee():

    def __init__(self,name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name


    @staticmethod
    def gather_requirements(project_name):

        if project_name == "ABC Project":

            requirement_task = ["task1", "task2", "task3"]

        else:
            requirement_task = "task1"

        return requirement_task

    #Instance method

    def work(self):

        requirement_task = self.gather_requirements(self.project_name)
        for task in requirement_task:

            print("Completed: ",task)

emp1= Employee("abmohiz",2300,"ABC Project")
emp1.work()