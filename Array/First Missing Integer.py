# Source : https://www.interviewbit.com/problems/first-missing-integer/
# Given an unsorted integer array, find the first missing positive integer.
# Your algorithm should run in O(n) time and use constant space.

# Algo/DS : Array

# Complexity : O(n)

class Solution:
	# @param A : list of integers
	# @return an integer
		def firstMissingPositive(self, A):

			# shift all -ve numbers to the end
			# max +ve number that can be present in array now n + 1, 1 being at index 0
			A , n =  self.shiftNegativeNumbers( A)

			# if  A[0] is be -ve then all numbers are -ve so return 1
			if  A[0] < 0 : return 1
			
			# now traverse array till n and if element <= n + 1 ,then mark its presence
			# To mark presence of an element x, we change the value at the index x to negative.
			for i in xrange(n + 1):

				if abs(A[i]) <= n + 1 and A[abs(A[i]) - 1] > 0 : # check if number is within max element range and is not already marked eg[1,1]

					A[abs(A[i]) - 1] = - A[abs(A[i])-1] # mark index corresponding to that element to -ve

			# return the first index for which value is positive
			for i in xrange(n + 1):

				if A[i] > 0 : return i + 1 # 1 is added becuase indexes start from 0


			
			# last  +ve number will be n + 1 so missing number will be (n + 1) + 1
			return n + 2



		# This will move all -ve numbers to right end of the array
		def shiftNegativeNumbers(self, A):

			
			end = len(A) - 1

			start = 0

			while (A[end] <= 0 and end > start): # A[end] will be first positive number from end 

						end = end -1 

			while start < end:

				if A[start] <= 0: # if element is <= 0 then swap with A[end]

					A[start] , A[end] = A[end] , A[start]

					while (A[end] <= 0 and end > start): # A[end] will be first positive number from end 

						end = end -1 

				start = start + 1

			return A, end


def main():

	print Solution().firstMissingPositive([-9,1,-5,-2])


if __name__ == '__main__':
	main()