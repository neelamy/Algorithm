# Problem : Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

# Source : https://www.interviewbit.com/problems/prime-sum/
#          http://www.geeksforgeeks.org/sieve-of-eratosthenes/

# Algo/DS : sieve of eratosthenes

# Complexity : O(n loglog n)


class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):

    	prime_no_list =  self.find_prime_no(A)

    	for ind , val in enumerate(prime_no_list):

    		if val and prime_no_list[ A - ind]:

    			return ind, A-ind



    def find_prime_no(self, n):

    	prime_no = [True] * (n + 1)

    	prime_no[0], prime_no[1] = False, False

    	for number in range(2, int( n **.5)+ 1 ):

    		if prime_no[number]:

    			for i in range(2 * number, n + 1, number):

    				prime_no[i] = False

    	return prime_no


print Solution().primesum(16777214)








        
       


