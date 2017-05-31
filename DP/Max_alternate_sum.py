# Source : http://www.geeksforgeeks.org/maximum-sum-alternating-subsequence-sum/

# Algo/DS : DP

# Complexity : O(n^2)

# Pythnon program to find sum of maximum sum alternating sequence starting with
# first element.

# Return sum of maximum sum alternating sequence starting with arr[0] and is first
# decreasing.
def maxAlternateSum(arr, n):

	# inc[] : inc[i] stores results of maximum sum alternating
 	#        subsequence ending with arr[i] such that arr[i]
 	#        is greater than previous element of the subsequence 
	# dec[] : dec[i] stores results of maximum sum alternating
 	#        subsequence ending with arr[i] such that arr[i]
 	#        is less than previous element of the subsequence 

	inc = [0] * n

	dec = [0] * n

	inc[0] = dec[0] = arr[0]

	flag = 0

	for i in range(1, n):

		for j in range(0, i ):
			
			# IF current sub-sequence is decreasing then
            # update dec[j] if needed. dec[i] by current
            # inc[j] + arr[i]
			if  arr[i] < arr[j] :
				
				dec[i] = max(dec[i], inc[j] + arr[i])

				# Revert the flag , if first decreasing
                # is found
				flag = 1
				
			else:
				# inc[i] should be calculated only if first dec value has been found
				if flag:
					
					inc[i] = max(inc[i], dec[j] + arr[i])
		
	return max(inc[n-1], dec[n-1])


def main():

	arr = [8, 2, 3, 5, 7, 9, 10]

	n = len(arr)

	print maxAlternateSum(arr, n)


if __name__ == '__main__':
	main()