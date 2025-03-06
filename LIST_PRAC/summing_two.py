

def combos_creation():

    target_num = 10

    my_list = [1,2,3,4,5,5,6,7,9]

    combo_list = []

    for i in my_list:
        for n in my_list[1:len(my_list)]:
            if i + n == target_num:
                l1 = [i,n]
                if l1 not in combo_list:
                    combo_list.append(l1)

    print(combo_list)
  

combos_creation()