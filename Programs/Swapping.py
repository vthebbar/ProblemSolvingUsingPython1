# Program to swap 2 numbers

# Approach 1

a=input("Key in first value:")
b=input("Key in second value:")

print("Before swap a=%s, b=%s"%(a,b))

#swap
a,b = b,a

print("After swap a=%s, b=%s"%(a,b))

print("****Approach 2***********")
# Approach 2

p=input("Key in first value:")
q=input("Key in second value:")

print("Before swap p=%s, q=%s"%(p,q))

temp=p
p=q
q=temp

print("After swap p=%s, q=%s"%(p,q))