# Find number of occurrence of an element in list using counter

from collections import Counter

ele_list = input("Key in the list elements separated by coma(,):")
ele_list = ele_list.split(",")
find = input("Key in element to find:")

dict = Counter(ele_list)  # this will return dictionary key:value pair
print("Dictionary:", dict)

print("Element '{}' found '{}' times".format(find,dict[find]))

