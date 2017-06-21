# Source : https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

			# print the max sum as well as the array element for the max sum 

# Algo/DS : DP

# Complexity :O(n)

class Solution:
    
    def maxSubArray(self, A):
              
		result = A[:]

		ind = [0] * len(A)
		                
		for i in range(1, len(A)):

			# if sum till last element + current element is greater than current sum
			# then update result(which contain current sum) and ind which store the
			# number of continuous element we have taken to get that sum
			if result[i-1] + A[i] > result[i] :

				result[i] = result[i-1] + A[i]

				ind[i] = ind[i-1] + 1 
		            

		max_sum_index = result.index(max(result))

		print A[max_sum_index - ind[max_sum_index] : max_sum_index + 1] #  [4,-1,2,1] has the largest sum = 6.





def main():

	A = [-2,1,-3,4,-1,2,1,-5,4]

	Solution().maxSubArray(A)


if __name__ == '__main__':
	main()
