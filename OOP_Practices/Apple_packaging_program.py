import random

class Apples:

    apple_num = 0

    apple_weight = 0.0

    def __init__(self, total_apples):
        self.total_apples = total_apples



    def program(self):

        while self.total_apples > 0:
            # Generate random weight for each apple
            current_apple_weight = random.uniform(0.2, 0.5)

            # Update class variables
            Apples.apple_weight += round(current_apple_weight, 1)
            Apples.apple_num += 1

            # Decrease the instance's apple count
            self.total_apples -= 1

            # Check if package weight exceeds 300
            if Apples.apple_weight > 300:
                print(f"Package limit exceeded: {round(Apples.apple_weight,1)} kg with {Apples.apple_num} apples")
                break
            else:
                print(f"Current total weight: {round(Apples.apple_weight,1)} kg, Total apples: {Apples.apple_num}")


myentry = Apples(1000)
myentry.program()

