# Partition set `S` into two subsets, `S1` and `S2`, such that the
# difference between the sum of elements in `S1` and the sum
# of elements in `S2` is minimized
def minPartition(S, n, S1=0, S2=0):
 
    # Base case: if the list becomes empty, return the absolute
    # difference between both sets
    if n < 0:
        return abs(S1 - S2)
 
    # Case 1. Include the current item in subset `S1` and recur
    # for the remaining items `n-1`
    inc = minPartition(S, n - 1, S1 + S[n], S2)
 
    # Case 2. Exclude the current item from subset `S1` and recur for
    # the remaining items `n-1`
    exc = minPartition(S, n - 1, S1, S2 + S[n])
 
    return min(inc, exc)
 
 
if __name__ == '__main__':
 
    # Input: a set of items
    S = [10, 20, 15, 5, 25]
 
    print("The minimum difference is", minPartition(S, len(S) - 1))
 