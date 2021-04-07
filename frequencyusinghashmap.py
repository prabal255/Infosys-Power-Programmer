def findCounts(arr, n):
    hash = [0 for i in range(n)]
    print(hash)
    i = 0
    while (i < n):
        hash[arr[i] - 1] += 1
        i += 1
        print(hash)
    print("Below are counts of all elements")
    for i in range(n):
        print(i + 1, "->", hash[i], end = " ")
        print()

# Driver code
arr = [ 2, 3, 3, 2, 5 ]
findCounts(arr, len(arr))

# arr1 = [1]
# findCounts(arr1, len(arr1))

# arr3 = [ 4, 4, 4, 4 ]
# findCounts(arr3, len(arr3))

# arr2 = [ 1, 3, 5, 7, 9,
# 		1, 3, 5, 7, 9, 1 ]
# findCounts(arr2, len(arr2))

# arr4 = [ 3, 3, 3, 3, 3,
# 		3, 3, 3, 3, 3, 3 ]
# findCounts(arr4, len(arr4))

# arr5 = [ 1, 2, 3, 4, 5,
# 		6, 7, 8, 9, 10, 11 ]
# findCounts(arr5, len(arr5))

# arr6 = [ 11, 10, 9, 8, 7,
# 		6, 5, 4, 3, 2, 1 ]
# findCounts(arr6, len(arr6))

# This code is contributed by avanitrachhadiya2155
