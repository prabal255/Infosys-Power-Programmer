def scndmax(arr):
    f=s=-21478
    for i in range(len(arr)):
        if arr[i]>f:
            s=f
            f=arr[i]
        elif arr[i]<f and arr[i]>s:
            s=arr[i]
    return s





arr=[1,1,1,1]
print(scndmax(arr))