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


demo_list= [i for i in range(1,20+1)]
mystact =StackImplementation_List(my_list_stack=demo_list)
mystact.pushing_elements()
mystact.poping_elements()

class StackImplementaion_deques():

    def __init__(self,my_deques: deque):

        self.mydeques = my_deques

    def pushing_deque(self):

        self.mydeques = []
        for deq in demo_list:
            self.mydeques.append(deq)
            print(f"Pushing using deque:{deq}")

        print(self.mydeques)

    def poping_deque(self):

        while self.mydeques:
            popped_queue = self.mydeques.pop()
            print("Poping :",popped_queue)

        print(self.mydeques)

demo_list1= deque(i for i in range(1,20+1))
demo_deq = StackImplementaion_deques(my_deques=demo_list1)
demo_deq.pushing_deque()
demo_deq.poping_deque()