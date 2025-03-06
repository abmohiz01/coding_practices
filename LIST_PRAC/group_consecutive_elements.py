
def group_elements():

    elements = [1,2,3,6,7,8,9,10,5,6]

    sub_list = []

    group = []

    for g1 in range(0, len(elements)):
        if elements[g1] == elements[g1 -1] +1:
            group.append(elements[g1])

        else:
            sub_list.append(group)
            group = [elements[g1]]  # Start new group

    sub_list.append(group)  # Add the last group
    sub_list.pop(0)
    print(sub_list)








group_elements()