
def large_and_small():

    l1 = [1,2,3,4,5,6,7,8,9]

    l1.sort(reverse=True)
    print(l1)

    k = int(input("Enter the kth largest element to find : "))
    print(k)
    for num in range(0,len(l1)):
        num = k-1
        print(l1[num])
        break

    l1.sort()

    s = int(input("Enter the kth smallest element to find : "))
    print(s)
    for num1 in range(0, len(l1)):
        num1 = s - 1
        print(l1[num1])
        break


large_and_small()
