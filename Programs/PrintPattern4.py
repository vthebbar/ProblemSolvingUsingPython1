# Print below pattern

'''
    X
   XX
  XXX
 XXXX
XXXXX

'''

for i in range(0,6):
    for j in range(5,i,-1):
        print(" ",end="")

    for k in range(0,i):
        print("X", end="")

    print()