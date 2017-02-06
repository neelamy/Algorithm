# Source : http://www.geeksforgeeks.org/maximum-sum-bi-tonic-sub-sequence/

# Algo/DS : DP

# Complexity : O(n^2)

# Dynamic Programming implementation of maximum sum of bitonic subsequence 

# Function return maximum sum of Bi-tonic sub-sequence
def max_sum(arr, n):

	# MSIBS[i] ==> Maximum sum Increasing Bi-tonic
    #              subsequence ending with arr[i]
    # MSDBS[i] ==> Maximum sum Decreasing Bi-tonic
    #              subsequence starting with arr[i]

	# allocate memory for MSIBS and initialize it to arr[i] for
    # all indexes
	MSIBS = arr[:]

	# Compute MSIBS values from left to right
	for i in range(n):

		for j in range(0, i):

			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]:

				MSIBS[i] = MSIBS[j] + arr[i]

	# allocate memory for MSDBS and initialize it to arr[i] for
    # all indexes
	MSDBS = arr[:]

	# Compute MSDBS values from right to left
	for i in range(1, n + 1):

		for j in range(1, i):

			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]:
	
				MSDBS[-i] = MSDBS[-j] + arr[-i]

	max_sum = float("-Inf") 

	# Find the maximum value of MSIBS[i] + MSDBS[i] - arr[i]
	for i ,j ,k in zip(MSIBS, MSDBS, arr):

		max_sum = max(max_sum, i + j - k)

	# return max sum of bi-tonic sub-sequence
	return max_sum


# Driver program to test the above function
def main():

	arr = [1 , 15 ,51 ,45 ,33 ,100 ,12 ,18 ,9]

	n = len(arr)

	print max_sum(arr, n)


if __name__ == '__main__':
	main()