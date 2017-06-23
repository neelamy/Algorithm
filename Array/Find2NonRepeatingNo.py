# Source : http://www.geeksforgeeks.org/?p=2457
#		   Find the two non-repeating elements in an array of repeating elements

# Algo/DS : Array , bit manipulation

# Complexity :O(n) , space - O(1)

# Note : x ^ x = 0 so xor will remove all even nos and only odd nos are left
# if all nos are repeated except one : xor all elements of A. This will return only one odd element of array
# if only 1 no is repeated : (xor all element of A) xor ( 1^2^3....n). This will make all elements even except one repeated element which will now be odd

class get2NonRepeatingNos:

	def NonRepeatingNo(self, A):

		# Get the xor of all elements
		xor = reduce(lambda x, y : x^y , A)

		# Get the rightmost set bit in set_bit_no
		set_bit_no = xor & ~(xor - 1)

		# Now divide elements in two sets by comparing rightmost set
   		# bit of xor with bit at same position in each element
		x = reduce(lambda x, y : x^y ,[i for i in A if set_bit_no & i])

		y = reduce(lambda x, y : x^y ,[i for i in A if not set_bit_no & i])

		print x,y



def main():
	get2NonRepeatingNos().NonRepeatingNo([2, 3, 7, 9, 11, 2, 3, 11])


if __name__ == '__main__':
	main()