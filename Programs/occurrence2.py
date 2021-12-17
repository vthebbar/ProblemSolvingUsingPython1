# To find number of occurrence of an element in list using count() method

def find_occurrence():
    try:
        ele_list = input("Key in list elements separated by coma(,):")
        ele_list = ele_list.split(",")
        print("Given list",ele_list)
        find = input("Key in the element to find:")

        res=ele_list.count(find)

        if res == 0:
            print("Element '{}' not found in given list".format(find))
        else:
            print("Element '{}' found '{}' times in given list".format(find, res))

    except:
        print("Invalid Input")

find_occurrence()