# Find minimum element in array/list

def find_min():

    try:
        arr=input("Key in the array elements(integers) separated by coma(,):")
        arr=arr.split(",")
        ele_list=[]
        for i in range(0,len(arr)):
            ele_list.append(int(arr[i]))
        print("Input list=",ele_list)

        min=ele_list[0]
        for i in range(1,len(ele_list)):
            if ele_list[i]<min:
                min=ele_list[i]

        print("Minimum element=", min)

    except:
        print("Invalid Input")


find_min()