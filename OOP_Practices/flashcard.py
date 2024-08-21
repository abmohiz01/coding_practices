import random

class FlashCard():

    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):

        return self.word+' ( '+self.meaning+' )'


flash = []

# while(True):
#     word = input("enter word")
#     meaning = input("enter the meaning ")

    # flash.append(FlashCard(word, meaning))
#     option = int(input("Enter 0 to add another"))
#     if option == 0:
#         continue
#     else:
#         break
#
# print("Your Flashcards")
#
# for i in flash:
#     print(">", i)


class FlashCard1():



    def __init__(self, fruits):
        self.fruits = fruits
        self.right_answers = 0


    def quiz(self):
        print("Options are :",fruits.values())

        self.right_answers = 0
        for fruit, color in fruits.items():

            print(fruit)
            ask = input("Enter the name of fruit color")
            print(ask)
            if ask == color:
                if True:
                    print("True")
                    self.right_answers +=1
                    continue


            else:
                print("Wrong answer")
                break

        print(f"Total right answers are: {self.right_answers}")


    def calculate_points(self):
        total_points = self.right_answers * 5
        print("Total points are ",total_points)





fruits = {'apple': "red",
                       'banana': "yellow",
                       'watermelon': 'green',
                       'grapes': 'purple',
                       'mango':"yellow"}
Keys = FlashCard1(fruits=fruits)
Keys.quiz()
Keys.calculate_points()




