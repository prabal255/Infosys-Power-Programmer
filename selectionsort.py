def selection(arr):
    for i in range(len(arr)):
        indx=i
        for j in range(i+1,len(arr)):
            if arr[indx]>arr[j]:
                indx=j
            arr[i],arr[indx]=arr[indx],arr[i]
            
    return arr

arr=[3,2,1,6,1]
print("sorted array",selection(arr))