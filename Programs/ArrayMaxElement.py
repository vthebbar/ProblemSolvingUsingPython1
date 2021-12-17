# To Find maximum element in array/list

def find_max():
    try:
        arr=input("Key in the array elements(integers) separated by coma(,):")
        arr = arr.split(",")
        print(arr)
        ele_list=[]
        for e in range(0,len(arr)):
            ele_list.append(int(arr[e]))
        print(ele_list)
        length=len(ele_list)
        max=ele_list[0]

        for i in range(1,length):
            if ele_list[i]>max:
                max=ele_list[i]
        print("Maximum value in list=",max)
    except ValueError:
        print("Invalid input")

find_max()