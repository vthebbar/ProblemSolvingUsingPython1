# Program to generate Fibonacci series
# Each number is sum of 2 preceding numbers - 0, 1, 1,2,3,5,8,13,21....

def fibonacci():
    try:
        values = int(input("Key in number of fibonacci numbers to be printed:"))
        print("Generated Fibonacci series is as below:")
        n1 = 0
        n2 = 1
        print(n1, end=" ")
        print(n2, end=" ")
        # range starts from 2 because first 2 numbers 0,1 are printed outside the loop
        for i in range(2,values):
            sum = n1+n2
            print(sum, end=" ")
            n1 = n2
            n2 = sum
    except ValueError:
        print("Invalid input")


fibonacci()