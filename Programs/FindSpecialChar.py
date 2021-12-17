# To find whether string contains special character

import re
def find_special_char():

    input_string = input("Key in the string:")
    regex = re.compile('[`~!@#$%^&*()_+=<>?/.,]')

    flag = regex.search(input_string)
    #print(flag)
    if flag == None:
        print("No special character found")
    else:
        print("Special character found")

find_special_char()