# To Reverse words in a string

def reverse_words():

    try:
        input_data = input("Key in the string:")

        words = input_data.split(" ")
        print("words=", words)
        words.reverse()
        # words = words[::-1] -> This is another way to reverse
        print("Reversed words=",words)

        rever_str = " ".join(words)
        print("Reversed string=", rever_str)

    except:
        print("Invalid input")

reverse_words()