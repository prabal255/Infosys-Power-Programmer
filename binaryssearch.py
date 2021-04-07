def binary(arr,low,high,x):
    mid=(low+high)//2
    if low<=high:
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary(arr,low,mid-1,x)
        else :
            return binary(arr,mid+1,high,x)

    else:
        return -1

print(binary([1,2,3,4,5,6,7],0,6,6))
