# Source : http://www.geeksforgeeks.org/minimum-cost-sort-strings-using-reversal-operations-different-costs/

# Algo/DS : DP

# Complexity :O(n)

# Python program to get minimum cost to sort
# strings by reversal operation

# Returns minimum cost for sorting arr[]
# using reverse operation. This function
# returns -1 if it is not possible to sort.
def ReverseStringMin(arr, reverseCost, n):
	
	# dp[i][j] represents the minimum cost to
    # make first i strings sorted.
    # j = 1 means i'th string is reversed.
    # j = 0 means i'th string is not reversed.
   
	dp = [[float("Inf")] * 2  for i in range(n)]

	# initializing dp array for first string
	dp[0][0] = 0

	dp[0][1] = reverseCost[0]

	# getting array of reversed strings
	rev_arr = [i[::-1] for i in arr]

	# looping for all strings
	for i in range(1, n):

		# Looping twice, once for string and once
        # for reversed string
		for j in range(2):

			# getting current string and current
            # cost according to j
			curStr = arr[i] if j==0 else rev_arr[i]

			curCost = 0 if j==0 else reverseCost[i]

			# Update dp value only if current string
            # is lexicographically larger
			if (curStr >= arr[i - 1]):

				dp[i][j] = min(dp[i][j], dp[i-1][0] + curCost)

			if (curStr >= rev_arr[i - 1]):

				dp[i][j] = min(dp[i][j], dp[i-1][1] + curCost)

	#  getting minimum from both entries of last index
	res = min(dp[n-1][0], dp[n-1][1])

	return res if  res != float("Inf") else -1


#  Driver code 
def main():


	arr = ["aa", "ba", "ac"]

	reverseCost = [1, 3, 1]

	n = len(arr)

	dp = [float("Inf")] * n

	res = ReverseStringMin(arr, reverseCost,n)

	if res != -1 :

		print "Minimum cost of sorting is" , res

	else :
		print "Sorting not possible"


if __name__ == '__main__':
	main()