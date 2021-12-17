# List Reversal

# Approach 1 - using reverse() method

list1 = input("Key in list elements separated by coma(,):")
list1 = list1.split(",")
print("Original list", list1)
list1.reverse()
print("Reversed list:", list1)

print("**********-----------")
# Approach 2 using slicing operator
list2 = input("Key in the list elements seperated by coma(,):")
list2 = list2.split(",")
print("Original list2:", list2)
rev_list = list2[::-1]
print("Reversed list", rev_list)