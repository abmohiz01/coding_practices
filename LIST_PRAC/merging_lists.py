'''Merge 2 sorted list into a new sorted list'''
import pandas as pd

def sorting():

    list_1 =[9,2,3,6,7,8]

    list_2 = [5,3,2,1,0]


    for num in range(0,len(list_1)):
        for num2 in range(num+1, len(list_1)):

            if list_1[num] > list_1[num2]:
                temp = list_1[num]
                list_1[num] = list_1[num2]
                list_1[num2] = temp

    print(list_1)

    sort1 = list_1

    for n1 in range(0,len(list_2)):
        for n2 in range(n1+1, len(list_2)):
            if list_2[n1] > list_2[n2]:
                temp2 = list_2[n1]
                list_2[n1] = list_2[n2]
                list_2[n2] = temp2

    print(list_2)
    sort2 = list_2

    new_sorted_list = sort1 + sort2
    new_sorted_list.sort()
    print(new_sorted_list)

    again = set(new_sorted_list)

    print(list(again))

    clean_list = []

    for i in new_sorted_list:
        if i not in clean_list:
            clean_list.append(i)

    print(clean_list)

sorting()

