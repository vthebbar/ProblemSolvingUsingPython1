# To find length of a string

def find_string_length():

    input_element = input("Key in the string:")

    # Approach 1
    length = len(input_element)
    print("Sting length using approach 1:", length)

    # Approach 2
    count =0
    for i in input_element:
        count+=1

    print("Length of string using approach 2:", count)

find_string_length()