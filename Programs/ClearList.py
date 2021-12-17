# To clear a list using clear() method

def clear_list():
    try:
        ele_list1 = input("Key in list elements separated by coma(,):")
        ele_list1 = ele_list1.split(",")
        ele_list = []
        for ele in ele_list1:
            ele_list.append(ele.strip())
        print("List elements before clear:", ele_list)

        ele_list.clear()

        print("List elements after clear:", ele_list)

    except:
        print("Invalid input")

clear_list()