class FlashCard():

    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):

        return self.word+' ( '+self.meaning+' )'


flash = []

while(True):
    word = input("enter word")
    meaning = input("enter the meaning ")

    flash.append(FlashCard(word, meaning))
    option = int(input("Enter 0 to add another"))
    if option == 0:
        continue
    else:
        break

print("Your Flashcards")

for i in flash:
    print(">", i)