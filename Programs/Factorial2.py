# Program to find factorial of a number - Iterative Approach

num = input("Key in a number:")

def fact(num):
    factorial=1
    try:
        num=int(num)

        if num == 0:
            print("Factorial of 0 is 1")
        elif num == 1:
            print("Factorial of 1 is 1")
        elif num < 0:
            print("Factorial does not exist for negative number")
        else:
            for i in range(1, num+1):
                factorial=factorial * i
            print("Factorial of %s="%num,factorial)
    except ValueError:
        print("Invalid Input")


fact(num)