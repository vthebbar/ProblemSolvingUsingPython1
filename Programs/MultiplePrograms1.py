
import datetime
import sys
from math import pi
# To display python version
print(sys.version)
print(sys.version_info)

# Current date and time
now =datetime.datetime.now()
print("Current date and time=",now)
format = now.strftime("%d-%m-%Y %H:%M:%M")  # formatting
print("Current date and time(formatted)=",format)

# Area of a circle based on radius

r=float(input("Key in the radius of a cirlce:"))
area = pi * r *r
print("Area of a circle=", area)

# program which accepts the user's first and last name and print them in reverse order with a space between them

def reverseName(fname, lname):
    fname = input("Key in first name:")
    lname = input("Key in last name:")
    rever_full_name= lname +" "+fname
    print("Lastname Firstname= ",rever_full_name)

reverseName("Raj","Kumar")

# program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

def listTuple():
    n=input("Key in comma separated numbers:")
    list1 = n.split(",")
    tuple1 = tuple(list1)
    print("List", list1)
    print("Tuple", tuple1)

listTuple()

