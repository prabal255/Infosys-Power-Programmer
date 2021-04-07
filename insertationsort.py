def sort(arr):
    for i in range(1,len(arr)):
        current_element=arr[i]
        pos=i
        while pos>0 and current_element<arr[pos-1]:
            arr[pos]=arr[pos-1]
            pos=pos-1
            #print(arr[pos])
            print(arr)
        arr[pos]=current_element
        print("After completing",arr)
    return arr

arr=[12,5,1,3,2]
print(sort(arr))