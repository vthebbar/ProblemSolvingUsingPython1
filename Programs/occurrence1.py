# Count Number of occurence of an element in list

def count_occ():

    try:
        ele_list = input("Key in array elements separated by coma(,):")
        ele_list = ele_list.split(",")
        print("Given list:", ele_list)
        find = input("Key in element to find:")
        count =0

        for i in ele_list:
            if i == find:
                count+=1

        if count == 0:
            print("Element '{}' not found in given list".format(find))
        else:
            print("Element '{}' found '{}' time(s) in given list".format(find, count))

    except (ValueError, TypeError):
        print("Invalid Input")

count_occ()