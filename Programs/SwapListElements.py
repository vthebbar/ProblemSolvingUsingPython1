# To swap first and last elements of a list


def swap_frist_last():
    try:
        list1 = input("Key in the list elements separated by coma(,):")
        list1=list1.split(",")
        print("Elements before swapping:")
        print(list1)
        temp=list1[0]
        list1[0] = list1[-1]
        list1[-1] = temp
        print("After swapping first and last elements:")
        print(list1)
    except:
        print("Invalid Input")

swap_frist_last()