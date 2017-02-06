# Source : http://www.geeksforgeeks.org/dynamic-programming-set-15-longest-bitonic-subsequence/

# Algo/DS : DP

# Complexity : O(n^2)

# Dynamic Programming implementation of longest bitonic subsequence problem
"""
lbs() returns the length of the Longest Bitonic Subsequence in
arr[] of size n. The function mainly creates two temporary arrays
increasing_seq[] and decreasing_seq[] and returns the maximum increasing_seq[i] + decreasing_seq[i] - 1.
 
increasing_seq[i] ==> Longest Increasing subsequence ending with arr[i]
decreasing_seq[i] ==> Longest decreasing subsequence starting with arr[i]
"""

def lbs(arr):

	n = len(arr)

	# allocate memory for increasing_seq[] and initialize its values as 1
    # for all indexes
	increasing_seq = [1] * n

	# Compute LIS values from left to right
	for i in range(n):

		for j in range(0, i):

			if arr[i] > arr[j] and increasing_seq[i] < increasing_seq[j] + 1:

				increasing_seq[i] = increasing_seq[j] + 1

	# allocate memory for decreasing_seq and initialize its values for
    # all indexes
	decreasing_seq = [1] * n

	# Compute LIS values from right to left
	for i in range(1, n + 1):

		for j in range(1, i):

			if arr[-i] > arr[-j] and decreasing_seq[-i] < decreasing_seq[-j] + 1:
	
				decreasing_seq[-i] = decreasing_seq[-j] + 1



	# Return the maximum value of (increasing_seq[i] + decreasing_seq[i] - 1)
	max_length = 0 

	for i ,j in zip(increasing_seq,decreasing_seq):

		max_length = max(max_length, i + j - 1)

	print max_length


# Driver program to test the above function# 
def main():

	arr = [0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15]

	lbs(arr)


if __name__ == '__main__':
	main()