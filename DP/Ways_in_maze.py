# Source : http://www.geeksforgeeks.org/count-number-ways-reach-destination-maze/

# Algo/DS : DP

# Complexity : O(R *C)

# Python program to count number of paths in a maze
# with obstacles using top down approach

# function to returns count of possible paths in a maze
def countways(maze, dp, row, col, i, j):

	# if i and j exceeds row and col then return 0
	if i >= row or j >= col : return 0

	# if current cell value is -1 then return 0 as there can be no path from here
	if maze[i][j] == -1 : return 0

	# if total path from maze[i,j] is already calculated then return that value
	if dp[i][j]:
	
		return dp[i][j]

	# if we have reached destination then return 1
	if i == row - 1 and j == col - 1: return 1
	
	# dp[i][j] = total ways from dp[i+1][j] + dp[i][j+1]
	dp[i][j] = countways(maze, dp, row, col, i + 1, j) + countways(maze, dp, row, col, i, j + 1)

	# return dp[i][j]
	return dp[i][j]


# Driver code
def main():
	maze =  [[0,  0, 0, 0],
			[0, 0, 0, 0],
			[-1, 0, 0, 0],
			[0,  0, 0, 0]]

	row = len(maze)

	col = len(maze[0])

	dp = [[0] * col for i in range(row)]

	print countways(maze, dp, row, col, 0, 0)


if __name__ == '__main__':
	main()