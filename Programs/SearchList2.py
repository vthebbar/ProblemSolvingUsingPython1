# To search element in a list

def search():

    try:
        ele_list1 = input("Key in the list elements separated by coma(,):")
        ele_list1 = ele_list1.split(",")
        ele_list=[]
        for ele in ele_list1:
            ele_list.append(ele.strip())

        search_item = input("Key in the value to search:")

        if search_item in ele_list:
            print("Search element '{}' found".format(search_item))
        else:
            print("Serach element '{}' not found".format(search_item))

    except (ValueError,TypeError):
        print("Invalid Input")

search()