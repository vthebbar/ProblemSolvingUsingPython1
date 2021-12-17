# To swap first and last elements of a list

def swap_first_last():
    try:
        list1 = input("Key in the list elements separated by coma(,):")
        list1 = list1.split(",")

        start, *middle, last = list1
        print("Start element=",start)
        print("Middle elements=",middle)
        print("Last element=",last)

        print("List Before swapping:", list1)

        list1[0] = last
        list1[-1] = start
        print("List after swapping first, last elements:", list1)

    except (IndexError, TypeError, ValueError):
        print("Invalid Input")



swap_first_last()