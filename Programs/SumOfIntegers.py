# Write a function, add_it_up(), that takes a single integer as input and returns the sum of the
# integers from zero to the input parameter.
# The function should return 0 if a non-integer is passed in.

def add_it_up(n):
    sum = 0
    try:
        m = int(n)
    except ValueError:
        print("Not a number, sum=", end=" ")
        return sum

    for i in range(0,m+1):
        sum=sum+i
    return sum

n = input("Key in a number:")
total = add_it_up(n)
print("Sum=",total)



