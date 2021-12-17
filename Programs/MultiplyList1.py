# Multiply list elements using loop

def mul_list():

    try:
        org_list = input("Key in list elements (Integer or float) separated by coma(,):")
        org_list = org_list.split(",")

        ele_list =[]
        for ele in org_list:
            ele_list.append(float(ele))

        result=1
        for e in ele_list:
            result = result * e

        print("Result of multiply=", result)

    except (ValueError, TypeError):
        print("Invalid input")

mul_list()