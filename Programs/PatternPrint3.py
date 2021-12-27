# Print below pattern
'''
*
**
***
****
*****
*****
****
***
**
*
'''

for i in range(0,6):
    for j in range(0,i):
        print("*", end="")
    print()
print("----------------")
for x in range(0,5):
    for y in range(4,x,-1):
        print("*", end="")
    print()