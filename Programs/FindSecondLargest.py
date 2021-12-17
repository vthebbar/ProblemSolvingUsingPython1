# To find second largest element in a list

def find_second_largest():
    try:
        input_list = input("Key in elements separated by coma(,):")
        input_list = input_list.split(",")

        elements = []
        for ele in input_list:
            elements.append(float(ele))


        elements.sort()
        print("Sorted list", elements)
        print("Second largest element=",elements[-2])

    except (ValueError, TypeError):
        print("Invalid Input")


find_second_largest()