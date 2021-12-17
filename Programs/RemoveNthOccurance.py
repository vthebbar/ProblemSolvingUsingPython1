# To remove Nth occurance of a word from list

def remove_occ():

    try:
        ele_list1 = input("Key in the elements separated by coma(,) , example : raj,kumar,raj :- ")
        ele_list1 = ele_list1.split(",")

        ele_list=[]
        for ele in ele_list1:
            ele_list.append(ele.strip())

        print("Original list:", ele_list)

        word = input("Key in the word to be removed from the list:")
        occ = int(input("Key in which occurance to be removed:"))
        count = 0

        for i in range(0,len(ele_list)):
            if ele_list[i] == word:
                count += 1

            if count == occ:
                del ele_list[i]
                print("List after removing word {} at occurance {}:".format(word, count))
                print(ele_list)
                break
    except (ValueError,IndexError, TypeError):
        print("Invalid Input")




remove_occ()