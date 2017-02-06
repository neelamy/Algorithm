# Source : http://www.geeksforgeeks.org/maximum-path-sum-position-jumps-divisibility-condition/

# Algo/DS : DP

# Complexity : O( n* sqrt(n))

# Python program to print maximum path sum ending with
# each position x such that all path step positions
# divide x.
import math

def printMaxSum(arr, n):

	# 1 is divisor of all so any position can be reached via 1 so add arr[0] to all arr element
	sum_array = [arr[0] + arr[i]  if i != 0 else arr[0] for i in range(n) ]

	# Now pick one number at a time and keep changing the sum of all its multiples
	# i = 1 means no = 2
	for i in range(1 , int(math.sqrt(n)) + 1): # runs (sqr(n) times)

		# m is the next multiple of no eg : if i = 1, no is 2 and m = 4
		# no will not affect its sum but all multiple ahead of it
		m = (i + 1 ) * 2 - 1

		while m < n : # (runs max n time: (n/2) +  (n/3) + (n/4) ..... )

			# sum[m] = max ( sum till no + arr[m] , existing sum till m)
			sum_array[m] = max(arr[m] + sum_array[i], sum_array[m])

			# increment m to next multiple of no
			m = m + (i + 1 ) 

	print sum_array


def main():

	arr = [2, 3, 1, 4, 6, 5]

	n = len(arr)

	printMaxSum(arr, n)

if __name__ == '__main__':
	main()