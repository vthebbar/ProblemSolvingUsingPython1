# Find sum of list elements using loop

def sum_of_list():

    try:
        ele_list = input("Key in list elements(Integer or float) separated by coma(,):")
        ele_list = ele_list.split(",")

        elements =[]
        for ele in ele_list:
            elements.append(float(ele))

        sum=0
        for e in elements:
            sum = sum + e

        print("Sum of list elements=", sum)
    except (TypeError, ValueError):
        print("Invalid Input")

sum_of_list()