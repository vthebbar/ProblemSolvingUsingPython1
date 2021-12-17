# Concat 2 list of strings  and remove duplicates


names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]

def unique_names(names1, names2):
    # should print Ava, Emma, Olivia, Sophia
    res=names1 + names2
    res = set(res)
    print(res)


if __name__ == "__main__":
    unique_names(names1, names2)


# Print string in particular format
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

