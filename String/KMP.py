# Source : Searching for Patterns. FInd all occurances of pattern in the string

# Algo/DS : KMP

# Complexity :O(n + m) n = length of string , m = length of search string

# O(m)

def calculateLPSArray(s):

	m = len(s)

	lps = [0] * m

	prefix = 0 ; suffix= 1

	# the loop calculates lps[i] for i = 1 to M-1
	while suffix < m:

			# if prefix and suffix  chrachter matches then lps[suffix] = 
			# length of prefix which is prefix + 1
			# increament suffix and prefix
		if s[prefix] == s[suffix]:

			lps[suffix] = prefix + 1

			prefix += 1

			suffix += 1

		else:
			# if prefix is 0 then suffix doesnt match even with 1st char
			# so lps[suffix] = 0
			# increament suffix
			if prefix == 0:

				lps[suffix] = 0

				suffix += 1

			else:
				# prefix doesnt match with suffix so now move prefix to
				# position where its suffix is equal to prefix 
				# i.e. lps[prefix - 1] .The idea is similar
            	# to search step.
            	# Note that we donot increament suffix.
				prefix = lps[prefix - 1]
	return lps

# O(n)
def KMP(original_string, search_string):

	lps = calculateLPSArray(search_string)

	original_index , search_index = 0, 0

	n = len(original_string); m = len(search_string) 

	while original_index < n :

		# if chars match then increament search_index
		if original_string[original_index] == search_string[search_index]:

			search_index += 1

			original_index += 1

		else:

			# else if search_index != 0 then reset it
			if search_index != 0:

				search_index = lps[search_index - 1]

			else:

				# if serach_index is 0 then just move to next char of original string
				original_index += 1

		# if search string reaches its end then match has been found
		# reset search index
		if search_index  == m : 

			print "Found pattern at : ", original_index - m 

			search_index = lps[search_index- 1]

def main():
	KMP("AABAACAADAABAABAA", "AABA")


if __name__ == '__main__':
	main()
