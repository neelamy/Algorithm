# Source :http://www.geeksforgeeks.org/maximum-subsequence-sum-such-that-no-three-are-consecutive/

# Algo/DS : DP

# Complexity : O(n)

# Function to return max sum without including 3 consecutive numbers
def maxSumWO3Consec(arr, n):

	# max_sum[i][0] = max sum including i-1th element with element i
	# max_sum[i][1] = max sum without including i-1th element with element i
	max_sum = [[0] * 2 for i in range(n)]

	# initialize first 2 indexes
	max_sum[0][0] =  arr[0]

	max_sum[0][1] = 0

	max_sum[1][0] = arr[0] + arr[1]

	max_sum[1][1] = arr[1]

	for i in range(2,n):

		# max_sum[i][0] : as we are including (i-1) so we cannot including (i-2)
		# so ax_sum[i][0]  = arr[i] + max_sum[i-1][1]
		max_sum[i][0] = arr[i] + max_sum[i-1][1]

		# as we are not including i-1 so we can take max of (i-2)
		max_sum[i][1] = arr[i] + max(max_sum[i-2][0],max_sum[i-2][1])

	# final answer will be max of n-1 and n-2
	return max(max_sum[n-1][0], max_sum[n-1][1],max_sum[n-2][0], max_sum[n-2][1])


def main():

	arr = [1, 2, 3, 4, 5, 6, 7, 8]

	n = len(arr)

	print maxSumWO3Consec(arr, n)


if __name__ == '__main__':
	main()