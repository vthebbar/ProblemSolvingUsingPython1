# Find sum of elements in a list

def listsum():

    try:
        ele_list = input("Key in list element (Integers or float) separated by coma(,):")
        ele_list = ele_list.split(",")

        elements =[]
        for ele in ele_list:
            elements.append(float(ele))

        total = sum(elements)
        print("Sum of list elements=", total)

    except (ValueError, TypeError):
        print("Invalid input")


listsum()