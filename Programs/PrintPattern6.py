# print below pattern
'''
A
A B C
A B C D
A B C D E

'''
# use chr() function to convert asci value to character
# ASCI value of A=65, B=66...so on
for i in range(0,5):
    for j in range(0,i+1):
        print(chr(65+j)," ", end="")          # to print small case letters use 97+j
    print()

