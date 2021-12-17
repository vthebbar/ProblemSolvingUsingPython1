# To swap any 2 elements in list using tuple packing and unpacking

def swap_elements():

    try:
        ele_list = input("Key in the list elements separated by coma(,):")
        ele_list = ele_list.split(",")
        print("Elements before swapping:", ele_list)

        pos1 = int(input("Key in the index position of the first element to be swapped:"))
        pos2 = int(input("Key in the index position of the another element to be swapped:"))

        # Tuple packing with 2 elements- create tuple
        get_tup = (ele_list[pos1],ele_list[pos2])

        # Tuple unpacking - first element in get_tup will be assigned to ele_list[pos2] and second assigned to ele_list[pos1]
        ele_list[pos2], ele_list[pos1] = get_tup

        print("After swapping element at position {} and {}:".format(pos1, pos2))
        print(ele_list)

    except (ValueError, TypeError,IndexError):
        print("Invalid Input")



# call function
swap_elements()