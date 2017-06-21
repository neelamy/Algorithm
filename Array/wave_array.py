# Source : https://www.interviewbit.com/problems/wave-array/
# Given an array of integers, sort the array into a wave like array and return it

# Algo/DS : Array

# Complexity : O(n lg n)

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        
        A = sorted(A)
        
        for i in xrange(0, len(A) - 1, 2):
            
            A[i] , A[i+1] = A[i+1], A[i]
            
        return A


def main():
	print Solution().wave([1, 2, 3, 4]) # [2, 1, 4, 3]


if __name__ == '__main__':
	main()