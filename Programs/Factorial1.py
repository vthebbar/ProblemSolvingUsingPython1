# Program to Find Factorial of a number - Recursive Approach

num = int(input("Key in a whole number:"))


def factorial(num):

    if num == 0 or num == 1:
        return 1
    elif num < 0:
        print("Factorial not exist for negative number")
    else:
        return num * factorial(num-1)

val=factorial(num)
print(val)


