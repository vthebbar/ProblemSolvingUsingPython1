# To find smallest and largest element in list using min() and max(0 methods

def find_smallest_largest():
    try:
        input_list = input("Key in list elements(Integers or float) separated by coma(,):")
        input_list = input_list.split(",")

        elements = []
        for ele in input_list:
            elements.append(float(ele))
        
        print("Maximum element=", max(elements))
        print("Minimum element=", min(elements))

    except (ValueError, TypeError):
        print("Invalid Input")

find_smallest_largest()