# Source : http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/

# Algo/DS : DP

# Complexity :O(nW)


def knapsack(dp, W, val, wt , i):

	# return 0 if W = 0 or no more elements left
	if i < 0 or W ==0 : return 0

	# return 0 if current element's weight > W remaining
	if W - wt[i] < 0 : return 0

	if dp[i][W] : 
		
		return dp[i][W]

	# dp[i][W] is max of (value obtained by taking current element, value obtained by not taking current element)
	dp[i][W]= max(val[i]+knapsack(dp, W - wt[i] , val, wt, i -1 ), knapsack(dp, W , val, wt ,i - 1 ))

	return dp[i][W]


def main():
	
	W = 50

	val = [120, 60, 100]
	
	wt = [30, 10, 20]

	n = len(wt)

	# initialize dp
	dp = [[0 for j in range(W + 1)] for i in range(n + 1)]

	print knapsack(dp, W, val, wt ,n-1)


if __name__ == '__main__':
	
	main()