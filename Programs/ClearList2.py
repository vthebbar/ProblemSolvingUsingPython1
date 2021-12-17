# Clear list

# by initializing list with nothing
list1 =[1,2,3,4,5]
print("List1 before clear",list1)
list1 =[]
print("List1 after clear", list1)

# by using del

list2 = ['raj', 'ram,',10,20,30,40]
print("List2 before clear=", list2)

del list2[:]

print("List2 after del", list2)


# by using *

list3 = [10,20,40,90,80]
print("List3 before clear", list3)

list3 *=0

print("List3 after clear", list3)