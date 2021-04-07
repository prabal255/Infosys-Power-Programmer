def heapify(arr,n,i):
    largest=i
    l=i*2+1
    r=i*2+2

    if l< n and arr[i]<arr[l]:
        largest=l
    if r< n and arr[largest]<arr[r]:
        largest=r
    
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]

        return heapify(arr,n,largest)


def heapSort(arr):
    n=len(arr)
   
# Build a maxheap.
# Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)
    return arr


arr=[1,4,7,6,5,32,23]
print(heapSort(arr))


    