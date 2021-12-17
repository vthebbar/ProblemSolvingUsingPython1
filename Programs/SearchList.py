# To search an element in a list

def search():

    try:
        flag = 0
        ele_list1 = input("Key in the list elements sepearated by coma(,):")
        ele_list1 = ele_list1.split(",")
        ele_list = []
        for ele in ele_list1:
            ele_list.append(ele.strip())

        print("List elements:", ele_list)

        search_item = input("Key in the search element:")

        for i in range(0,len(ele_list)):

            if ele_list[i] == search_item:
                print("Element '{}' found at index position '{}'". format(search_item,i))
                flag = 1

        if flag == 0:
            print("Element '{}' not found". format(search_item))
    except (ValueError,TypeError,IndexError):
        print("Invalid Input")


search()


