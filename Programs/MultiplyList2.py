# Multiply list elements using numpy package

import numpy

def mul_list():

    try:
        org_list = input("Key in list elements(integers or float) separated by coma(,):")
        org_list = org_list.split(",")

        elements =[]
        for ele in org_list:
            elements.append(float(ele))

        result = numpy.prod(elements)
        print("Result of multiply=", result)
    except (ValueError,TypeError):
        print("Invalid Input")

mul_list()