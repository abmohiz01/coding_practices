"""Reverse a string """

def reverse(word :str) -> str:
    return word[::-1]

def reverse_string(word_2: str) -> str:
    myword = ""

    for empty in word_2:
        myword = empty + myword
    return myword


#reverse("hello world")
print(reverse_string("helloworld 2"))

'''Write a Python function to check if a string is a palindrome'''

def palandrome(palind_word: str) -> bool:
    '''It first reverse a strings and then check if it is true or not'''
    word_reversing = reverse(palind_word)

    if word_reversing == palind_word:
        print("PALINDROME ")
        return True

    else:
        print("NOT PALINDROME ")
        return False


print(palandrome("nayak"))

def remove_duplicates(word3):
    """Using a Set method"""

    my_list = []
    unique_word = set()
    for word in word3:
       if word not in unique_word:
           unique_word.add(word)
           my_list.append(word)

    print("Unique characters in order:", "".join(my_list))

def remove_char(word4):
    """Removing duplicates in string using a list """

    list_4 = []
    for char in word4:
        if char not in list_4:
            list_4.append(char)


    print("Removed duplicates in string using list method :", "".join(list_4))



remove_duplicates("hello")
remove_char("Programming")