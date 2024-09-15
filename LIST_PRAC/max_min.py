class MaxMin():

    def __init__(self, operation_list: list):
        self.operation_list = operation_list

    def min_list(self):

        min = self.operation_list[0]

        for i in range(len(self.operation_list)):

            if  self.operation_list[i] < min:
                min = self.operation_list[i]

        print("minimum using list operations",min)

    def min_list_sort(self):

        self.operation_list.sort()
        print("minimum using sort ",self.operation_list[0])


    def max_list_sort(self):
        self.operation_list.sort(reverse=True)
        print("maximum using sort ",self.operation_list[0])

    def max_list(self):


        max = self.operation_list[0]

        for j in range(len(self.operation_list)):

            if self.operation_list[j] > max:
                max = self.operation_list[j]

        print("maximum using list operation ",max)







my_list = [1,2,3,4,5,6]
example1 = MaxMin(operation_list=my_list)
example1.min_list()
example1.max_list()
example1.min_list_sort()
example1.max_list_sort()