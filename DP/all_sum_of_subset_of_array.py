# Source : http://www.geeksforgeeks.org/find-distinct-subset-subsequence-sums-array/

# Algo/DS : DP

# Complexity : O(n * max_sum)

def printDistSum(arr):

	# Find the max sum that can be achieved
	max_sum = sum(arr)

	n = len(arr)

	# Initialize dp. Set dp[0][0] = 1 as 0 can be obtained by any subset
	dp = [[0] * (max_sum + 1) for i in range(n+1)]

	dp[0][0] = 1

	# Fill dp. Take one array element at a time
	for i in range(n):

		# dp[i] is possible sum without element i
		for j in range(max_sum + 1):

			if dp[i][j] == 1:

				# if sum was possible without arr[i] then it will be 
				# possible with arr[i] as well
				dp[i + 1][j] = 1

				#additional new sums are all previous sums + arr[i]
				dp[i + 1][j + arr[i] ] = 1

	# Print last row elements
	for i in range(max_sum + 1):

		if dp[-1][i] == 1:
		
			print i ,


# Driver code
def main():

	arr = [2, 3, 4, 5, 6]

	printDistSum(arr)


if __name__ == '__main__':
	main()