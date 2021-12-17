# To copy the list

def copylist():

    list1 = input("Key in list elements separated by coma(,):")
    list1 = list1.split(",")
    print("original list", list1)

    # using copy method
    list2 = list1.copy()
    print("Copy of list", list2)

    # using extend method
    list3 =[]
    list3.extend(list1)
    print("Copy 2 of list", list3)

    # Using slicing operator
    list4 = list1[:]
    print("COpy 3 of list", list4)

    # Using list comprehension
    list5 = [i for i in list1]

    print("copy 4 of list", list5)

copylist()