# print below pattern

'''
A
B B
C C C
D D D D
E E E E E
'''

# ASCI value of A=65, B=66...so on
# use chr() function to convert
# ASCI range A-Z : 65 to 90, a-z : 97 to 122

# approach 1
for i in range(0,5):
    for j in range(0,i+1):
        print(chr(65+i)," ",end="")    # to print small case letter use 97+i
    print()

print("-------------Approach2------------")
# approach 2
asci_val=65   # to print small case use asci_val=97
for a in range(0,5):
    for b in range(0,a+1):
        print(chr(asci_val)," ", end="")
    asci_val+=1
    print()
