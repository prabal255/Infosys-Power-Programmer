# Python3 program for the above approach
import sys

# Function to return minimum difference
# between two subarray sums
def minDiffSubArray(arr, n):

	# To store prefix sums
	prefix_sum = [0] * n

	# Generate prefix sum array
	prefix_sum[0] = arr[0]

	for i in range(1, n):
		prefix_sum[i] = (prefix_sum[i - 1] +
								arr[i])

	# To store suffix sums
	suffix_sum = [0] * n

	# Generate suffix sum array
	suffix_sum[n - 1] = arr[n - 1]

	for i in range(n - 2, -1, -1):
		suffix_sum[i] = (suffix_sum[i + 1] +
								arr[i])

	# Stores the minimum difference
	minDiff = sys.maxsize

	# Traverse the given array
	for i in range(n - 1):

		# Calculate the difference
		diff = abs(prefix_sum[i] -
				suffix_sum[i + 1])

		# Update minDiff
		if (diff < minDiff):
			minDiff = diff

	# Return minDiff
	return minDiff

# Driver Code
if __name__ == '__main__':
	
	# Given array
	arr=[10, 20, 15, 5, 25]
	# Length of the array
	n = len(arr)

	print(minDiffSubArray(arr, n))

# This code is contributed by mohit kumar 29
