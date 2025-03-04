'''ROTATE A LIST TO THE RIGHT BY K STEPS'''
from collections import  deque
def rotations():
    my_list = [1,2,3,4,5]
    k = int(input("Enter a number to rotate by its step"))
    print(k)
    rotated_list = my_list[-k:] + my_list[:-k]
    print(rotated_list)

rotations()

def rotations_builtin():
    my_list = [1,23,4,5,6]
    print(my_list)
    k = int(input("Enter a number to rotate by its step"))
    print(k)

    d = deque(my_list)
    d.rotate(k)
    new_list = list(d)
    print(new_list)


def rotation_left():
    my_list = [1,23,4,5,6]
    k = int(input("Enter a number to rotate the list to left"))
    print(k)
    rotate_left = my_list[k:] + my_list[:k]
    print(f"List {my_list} rotated to {k} steps : {rotate_left}")
rotations_builtin()
rotation_left()