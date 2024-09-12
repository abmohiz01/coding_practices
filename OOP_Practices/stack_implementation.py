from collections import deque

class StackImplementation_List():

    def __init__(self,my_list_stack:list):

        self.my_list_stack = my_list_stack
    def pushing_elements(self):

        self.my_list_stack= []
        for num in demo_list:
            self.my_list_stack.append(num)
            print(f"Pushing: {num}")

        print(self.my_list_stack)
        return self.my_list_stack


    def poping_elements(self):

        while self.my_list_stack:
            popped_elememt = self.my_list_stack.pop()
            print(f"Popping :{popped_elememt}")

        print(self.my_list_stack)


demo_list = [i for i in range(1,20+1)]
mystact =StackImplementation_List(my_list_stack=demo_list)
mystact.pushing_elements()
mystact.poping_elements()
