"""Printing star in triangle """

def triangle_pattern():
    for i in range(1,5):
        for j in range(i):
            print(j+1,end = " ")

        print()  #Move the next line after each row


triangle_pattern()

"""Printing square pattern"""

def square_pattern():
    for i in range(4):
        for j in range(4):
            print("#", end =" ")

        print()

square_pattern()