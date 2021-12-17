# Sum of range of numbers
# Write a function, add_it_up(), that takes a single integer as input and returns the sum of the
# integers from zero to the input parameter.
# The function should return 0 if a non-integer is passed in.

def add_it_up(n):

    try:
        m=int(n)
        result = sum(range(m + 1))

    except ValueError:
        print("Not a number;", end=" ")
        result = 0
    return result

n=input("Enter a Number:")
res=add_it_up(n)
print("Sum=", res)