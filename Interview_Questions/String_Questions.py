"""Reverse a string """

def reverse(word :str) -> str:
    print(word[::-1])

def reverse_string(word_2: str) -> str:
    myword = ""

    for empty in word_2:
        myword = empty + myword
    return myword


#reverse("hello world")
print(reverse_string("helloworld 2"))
