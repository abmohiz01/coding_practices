'''
First In First Out

'''
from collections import deque


class My_QUEUE():

    @staticmethod
    def queing_list():

        my_queue = []
        my_queue.append("a")
        my_queue.append("b")
        my_queue.append("c")
        my_queue.append("d")

        print("Initial Queue")
        print(my_queue)

        # my_queue.pop(0)
        # my_queue.pop(0)
        # my_queue.pop(0)
        # my_queue.pop(0)
        #
        # print("Final queue")
        # print(my_queue)
        print("Removing Queues in order")
        while len(my_queue) > 0:
            my_queue.pop(0)
            print(my_queue)
        print("Queue emptied")


    @staticmethod
    def q_method():
        o_q = deque()

        for num in range(0,10):
            o_q.append(num)
            print(o_q)

        print("Collected QUEUE :",o_q)

        while len(o_q) > 0:
            # This will pop the first element we inserted
            o_q.popleft()
            print("Popping QUEUE",o_q)





first_attempt = My_QUEUE
first_attempt.queing_list()
first_attempt.q_method()
