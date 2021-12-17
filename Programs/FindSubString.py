# To find sub string in the main string
def find_substr():

    try:
        main_str = input("Key in the main string:")
        sub_str = input("Key in the sub string:")

        flag = main_str.find(sub_str)

        if flag == -1:
            print("Substring NOT found in main string")
        else:
            print("Substring FOUND in main string")

    except (TypeError, ValueError):
        print("Invalid input")

find_substr()