# To swap any 2 elements of a list - using simple swap

def swap_elements():

    try:
        ele_list = input("Key in the list elements separated by coma(,):")
        ele_list = ele_list.split(",")
        print("List before swapping:", ele_list)
        pos1 = int(input("Key in the index position of first element to be swapped:"))
        pos2 = int(input("Key in the index position of the second element to be swapped:"))

        ele_list[pos1],ele_list[pos2] = ele_list[pos2], ele_list[pos1]

        print("After swapping elements at index position {} and {} :".format(pos1, pos2))
        print(ele_list)

    except (ValueError, TypeError,IndexError):
        print("Invalid Input")


swap_elements()