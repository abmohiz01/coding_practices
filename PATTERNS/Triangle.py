"""Printing star in triangle """

def triangle_pattern():
    for x in range(1, 5):
        for y in range(x):
            print("*", end=" ")

        print()
    for i in range(5):
        for j in range(i, 5):
            print("*", end=" ")

        print()







triangle_pattern()

"""Printing square pattern"""

def square_pattern():
    for i in range(4):
        for j in range(4):
            print("#", end =" ")

        print()

square_pattern()