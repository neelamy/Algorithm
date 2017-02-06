# Source : http://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/

# Algo/DS : DP

# Complexity : O(nW)


def knapsack(dp, W, val, wt):

	# for each weight check max value that can be achieved
	for i in range(W+1):

		# for each weight( i.e. i), consider all weights less than equal to i
		for j,v in zip(wt,val):

			if j <=i:

				# Take max value which can be achieved by weights(wt)
				dp[i] = max(dp[i], dp[i-j] + v)

	return dp[W]


def main():
	
	W = 8

	val = [10, 40, 50, 70]
	
	wt = [1, 3, 4, 5]

	n = len(wt)

	dp = [0]*  (W + 1)

	print knapsack(dp, W, val, wt)

	print dp


if __name__ == '__main__':
	
	main()