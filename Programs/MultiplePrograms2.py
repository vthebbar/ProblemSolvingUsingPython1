
# program to accept a filename from the user and print the extension of that

def find_file_extension(fname):
    list1 = fname.split(".")
    flag= "." in fname
    if flag == True:
        print("File Extension= .", list1[-1])
    else:
        print("Invalid file name")

file_name=input("Key in file name with extension:")
find_file_extension(file_name)

# program to display the first and last elements from the following list

list2 =["Green","Blue","Red","White"]
print("First element=",list2[0]," Last element=", list2[-1])

# program to display the examination schedule, extract the date from exam_start_date
exam_start_date = (12,12,2022)
print( "The examination will start from : %s / %s / %s"%exam_start_date)


# program that accepts an integer (n) and computes the value of n+nn+nnn

def calc():
    try:
        n=int(input("Key in a whole number:"))
        n1=int("%s" %n)
        n2=int("%s%s"%(n,n))
        n3=int("%s%s%s"%(n,n,n))
        tot=n1+n2+n3
        print("value of n+nn+nnn=",tot)
    except ValueError:
        print("Invalid Input, Not a  number")

calc()