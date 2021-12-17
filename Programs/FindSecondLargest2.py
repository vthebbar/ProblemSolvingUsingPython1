# To find second largest element in a list by converting to set and remove max element

def find_second_largest():

    try:
        input_list = input("Key in element(Integer or float) separated by coma(,):")
        input_list = input_list.split(",")
        elements = []
        for ele in input_list:
            elements.append(float(ele))

        ele_set = set (elements)
        ele_set.remove(max(ele_set))

        print("After removing largest element", ele_set)
        print("Second largest =", max(ele_set))

    except (ValueError, TypeError):
        print("Invalid Input")

find_second_largest()