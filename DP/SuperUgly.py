# Source : http://www.geeksforgeeks.org/super-ugly-number-number-whose-prime-factors-given-set/

# Algo/DS : DP

# Complexity : O(n)

# Python program to find n'th Super Ugly number

# Function to get the nth Super ugly number
def superUgly(primes, n):

	ugly = [0] * n # To store ugly numbers

	# 1 is the first ugly number
	ugly[0] = 1

	# i array  will indicate indices for all primes 
	i = [0] * len(primes)

	# set initial multiple value
	multiples = primes[:]

	# start loop to find value from ugly[1] to ugly[n]
	l = 1

	while (l < n ):

		# choose the min value of all available multiples
		next_no = min(multiples)

		# add this value if it is not already present
		if ugly[l - 1] != next_no:

			ugly[l] = next_no

			l = l + 1

		# increment the value of index accordingly
		p = multiples.index(next_no)

		i[p] +=1

		multiples[p] = ugly[i[p]] * primes[p]

	# return ugly[n] value
	return ugly[-1]



def main():

	primes = [3, 5, 7, 11, 13]

	n = 9

	print superUgly(primes, n)


if __name__ == '__main__':
	main()