import random

class Apples:

    apple_num = 0

    apple_weight = 0.0

    def __init__(self, total_apples):
        self.total_apples = total_apples



    def program(self):

        while self.total_apples > 0:

            apple_weight = random.uniform(0.2,0.5)

            for apple_num in range(self.total_apples):
                apple_weight += apple_num


            if apple_weight > 300:
                print("Package limit Exceeded", apple_weight)
                break

            else:
                print("Package Weight",apple_weight)
                break


myentry = Apples(24)
myentry.program()

