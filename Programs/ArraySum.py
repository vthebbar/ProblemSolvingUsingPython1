# Sum of elements in a list

def total():
    try:
        ele=input("Key in the array elements, separated by coma(,):")
        ele_list=ele.split(",")
        print("Input data :",ele_list)
        lst2=[]

        for i in range(0,len(ele_list)):
            lst2.append(int(ele_list[i]))

        print("Integer list=",lst2)
        total = sum(lst2)
        print("Sum of Integer List=",total)
    except ValueError:
        print("Invalid Input, Key in only integers separated by coma(,)")

total()