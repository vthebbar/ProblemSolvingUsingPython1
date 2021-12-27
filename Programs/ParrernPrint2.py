# print below pattern
'''
*****
****
***
**
*
'''

# approach 1
for i in range(5,0,-1):   # rows - decrement loop 5,4,3,2,1
    for j in range(0,i):  # columns - based on row
        print("*", end="")
    print()

print("--------------------------------------")
# approach 2

for x in range(0,5):
    for y in range(5,x,-1):
        print("*", end="")
    print()