# Source : https://www.interviewbit.com/problems/largest-number/
# 		   http://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/

# Algo/DS : Aarray , custom sort

# Complexity :O(n lg n)

class CreateLargestNumber:
    
    # compare if ab is greater or ba. Eg a = 30, b = 3 so check if 303 is greater or 330
    def CustomSort(self,a, b):

        return 1 if a + b > b + a else -1


    def largestNumber(self, A):

    	# change int to str
        A = map(str, A)
        
        # sort using custom sort
        A.sort(cmp = self.CustomSort, reverse = True)

        # for [0,0,0,0], output should be "0" and not "0000". For this change str to int and then back to int
        return str(int("".join(A)))



def main():
	CreateLargestNumber().largestNumber([3, 30, 34, 5, 9])


if __name__ == '__main__':
	main()