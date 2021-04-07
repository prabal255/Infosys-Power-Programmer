def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)
    return arr        
arr=[7,6,3,5,23,45,11,21]
print(bubblesort(arr))