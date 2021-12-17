# Find Length of a list

# Approach 1 - using built in len(0 method
list1=[1,2,3,4,10,99]
print("Approach 1- Length of list=",len(list1))


# Approach 2 - using counter
count=0
for i in list1:
    count+=1
print("Approach 2- Length of list=", count)
