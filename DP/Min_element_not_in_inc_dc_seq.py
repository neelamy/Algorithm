# Source : http://www.geeksforgeeks.org/minimum-number-of-elements-which-are-not-part-of-increasing-or-decreasing-subsequence-in-array/

# Algo/DS : DP

# Complexity : O(n^3)


def count_min(arr, dp, n,dec, inc, i):

	# return if complete array has been traversed
	if i == n: return 0 

	# if value has already been calculated then return that value
	if dp[dec][inc][i]!= -1:
		
		return dp[dec][inc][i]

	# check for dec sequence, ie. if current index i can be included in dec seq
	if arr[i] < arr[dec]:

		dp[dec][inc][i] = count_min(arr, dp, n,i, inc, i+1)

	# check for inc sequence, ie. if current index i can be included in inc seq
	if arr[i] > arr[inc]:

		# if i is not in dec seq then directly find count for inc seq
		if dp[dec][inc][i] == -1:

			dp[dec][inc][i] = count_min(arr, dp, n,dec, i, i+1)

		else:
			# i is in dec and inc seq so count will be min of two.
			dp[dec][inc][i] = min(dp[dec][inc][i], count_min(arr, dp, n,dec, i, i+1))

	# check count if current index i is not included in any seq
	if dp[dec][inc][i] == -1:
		# i is neither is inc or dec so update the count by 1 
		# Now i is not part of any seq 
		dp[dec][inc][i] = 1 + count_min(arr, dp, n,dec, inc, i+1)

	else:
		# i is in dec or inc seq. Take min count, when i is included in seq and count
		# when i is not included in seq
		dp[dec][inc][i] = min(dp[dec][inc][i],1 + count_min(arr, dp, n,dec, inc, i+1))


	return dp[dec][inc][i]


# main function
def main():

	arr = [7, 8, 1, 2, 4, 6, 3, 5, 2, 1, 8, 7 ]

	n = len(arr)

	# append infinity to start decreasing sequence
	arr.append(float("Inf"))

	# append -infinity to start increasing sequence
	arr.append(float("-Inf"))

	# initialize dp, dp[dec][inc][i] = -1
	# dp[for all dec index][ for all inc index][current index] = min_count value
	dp =  [[[-1] * (n + 2) for j in range(n + 2)] for i in range(n + 2)]

	print count_min(arr, dp, n, n, n+1, 0)


if __name__ == '__main__':

	main()