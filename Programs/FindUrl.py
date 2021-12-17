# To find URL in a string

import re

def find_url():

    input_string = input("Key in the string with or without URL:")
    res = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',input_string)
    # print(res)
    if res == []:
        print("No URL found in given string")
    else:
        print("URL found-", res)



find_url()