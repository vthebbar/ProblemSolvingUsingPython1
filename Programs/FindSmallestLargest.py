# To find smallest and largest element in list using sort() method

def find_Smallest_Largest():

    try:
        input_list = input("Key in elements (Integers or float) separated by coma(,):")
        input_list = input_list.split(",")

        elements = []
        for ele in input_list:
            elements.append(float(ele))

        elements.sort()
        print("Sorted List:", elements)

        print("Largest element=", elements[-1])
        print("Smallest element=", elements[0])

    except (ValueError, TypeError):
        print("Invalid Input")



find_Smallest_Largest()