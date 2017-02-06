'''
https://community.topcoder.com/stat?c=problem_statement&pm=14417&rd=16822&rm=&cr=22671942

Problem Statement
    	
You are given a int[] a. The elements of a are not necessarily distinct.

You want to rearrange the elements of a into a non-decreasing order. What is the smallest possible number of elements you have to move?

Formally, the operation looks as follows:

You select some set of positions in a.
You permute the elements on the chosen positions arbitrarily.
Compute and return the smallest possible size of the set of selected positions.
 
Definition
    	
Class:	SortingSubsets
Method:	getMinimalSize
Parameters:	int[]
Returns:	int
Method signature:	int getMinimalSize(int[] a)
(be sure your method is public)
    
 
Constraints
-	a will contain between 1 and 50 elements, inclusive.
-	Each element of a will be between 1 and 100, inclusive.
 
Examples
0)	
    	
{3, 2, 1}
Returns: 2
One can take the first and the last element and swap them.
1)	
    	
{1, 2, 3, 4}
Returns: 0
The array is already sorted, so we can select an empty set of positions.
2)	
    	
{4, 4, 4, 3, 3, 3}
Returns: 6
Here all elements must be taken and permuted.
3)	
    	
{11, 11, 49, 7, 11, 11, 7, 7, 11, 49, 11}
Returns: 7

'''

class SortingSubsets:
	def getMinimalSize(self, a):
		
		# increment count whenever elements in a are not in correct position
		# i.e a[i] != b[i] as b (i.e.sorted(a)) has correct position of all elements
		return sum(x!=y for x,y in zip(a, sorted(a)))
			

s =  SortingSubsets()

a = [11, 11, 49, 7, 11, 11, 7, 7, 11, 49, 11]

print s.getMinimalSize(a)