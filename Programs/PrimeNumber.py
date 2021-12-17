# Program to check number is prime or not
# A number that is divisible only by itself and 1 is called prime number (e.g. 2, 3, 5, 7, 11 are prime numbers)

def prime():
    try:
        num = int(input("Key in a integer value:"))
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count == 2:
            print("%s is a prime number" % num)
        else:
            print("%s is NOT a prime number" % num)

    except ValueError:
        print("Invalid Input")


# call function
prime()