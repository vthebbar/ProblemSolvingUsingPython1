# To check whether given string is palindrome or not
# Palindrome example : RAR, MADAM (Reading L->R and L <-R both are same)

def check_palindrome():

    try:
        input_element = input("Key in the string:")
        reversed_element = input_element[::-1]

        if input_element == reversed_element:
            print("Given string '{}' is palindrome".format(input_element))
        else:
            print("Given string '{}' is NOT a palindrome".format(input_element))

    except Exception as e:
        print("Invalid input", e)


check_palindrome()
