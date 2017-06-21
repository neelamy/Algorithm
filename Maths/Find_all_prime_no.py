# Problem : Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.

# Source : http://www.geeksforgeeks.org/sieve-of-eratosthenes/

# Algo/DS : sieve of eratosthenes

# Complexity : O(n loglog n)


class Solution:
    # @param A : integer
    # @return a list of integers
    def All_Prime(self, A):

    	is_prime =  self.find_prime_no(A)


    	prime_no = [ind for ind , val in enumerate(is_prime) if val ]

    	return prime_no



    def find_prime_no(self, n):

    	is_prime = [True] * (n + 1)

    	is_prime[0], is_prime[1] = False, False

    	for number in xrange(2, int( n **.5)+ 1 ):

    		if is_prime[number]:

    			for i in xrange(2 * number, n + 1, number):

    				is_prime[i] = False

    	return is_prime


print Solution().All_Prime(20) # [2, 3, 5, 7, 11, 13, 17, 19]








        
       


