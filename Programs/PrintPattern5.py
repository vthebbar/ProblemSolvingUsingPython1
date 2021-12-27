# Print below pattern
'''
*
**
***
****
*****

          *
         * *
        * * *
       * * * *

'''

for i in range(0,5):
    for j in range(0,i+1):
        print("*", end="")
    print()

print("-------------------------")

for a in range(0,4):
    for b in range(4,a+1,-1):
        print(" ", end="")

    for c in range(0,a+1):
        print(" *",end="")     # give space before *
    print()