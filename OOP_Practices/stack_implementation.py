from collections import deque

class StackImplementation_List():

    def __init__(self):
        self.my_list_stack = []
    def pushing_elements(self):

        for num in range(1,10):
            self.my_list_stack.append(num)
            print(f"Pushing: {num}")

        print(self.my_list_stack)
        return self.my_list_stack


    def poping_elements(self):

        while self.my_list_stack:
            popped_elememt = self.my_list_stack.pop()

            print(f"Popping :{popped_elememt}")

        print(self.my_list_stack)



mystact =StackImplementation_List()
print(mystact.pushing_elements())
print(mystact.poping_elements())
