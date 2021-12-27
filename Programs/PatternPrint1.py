# print below pattern
'''
      *
      **
      ***
      ****
      *****

'''
def pattern():

    for i in range(0,6):   # Rows 0 to 4 = 5 rows
        for j in range(0,i):   # columns based on row number
            print("*", end="")
        print()

pattern()