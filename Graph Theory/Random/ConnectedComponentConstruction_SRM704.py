'''
Problem : https://community.topcoder.com/stat?c=problem_statement&pm=14466
Problem Statement
    	Any undirected graph can be decomposed into connected components. Two vertices u and v belong to the same connected component if we can travel from u to v by following a sequence of zero or more consecutive edges. The size of a connected component is the number of vertices it contains. 



You are given a int[] s. Construct a simple undirected graph with the following properties:
The number of vertices is n, where n is the number of elements in s.
The vertices are numbered 0 through n-1.
For each i, the size of the connected component that contains vertex i is exactly s[i].
If there is no such graph, return an empty String[]. Otherwise, return a String[] ret with n elements, each containing n characters. For each i and j, ret[i][j] should be 'Y' if there is an edge between i and j in your graph. Otherwise, ret[i][j] should be 'N'. If there are multiple solutions, you may return any of them.
 
Definition
    	
Class:	ConnectedComponentConstruction
Method:	construct
Parameters:	int[]
Returns:	String[]
Method signature:	String[] construct(int[] s)
(be sure your method is public)
    
 
Constraints
-	s will contain between 1 and 50 elements, inclusive.
-	Each element in s will be between 1 and |s|, inclusive.
 
Examples
0)	
    	
{2,1,1,2,1}
Returns: {"NNNYN", "NNNNN", "NNNNN", "YNNNN", "NNNNN" }
The answer is a graph that contains only one edge. This edge connects the vertices 0 and 3. This graph has four connected components: {0, 3}, {1}, {2}, and {4}.
1)	
    	
{1,1,1,1}
Returns: {"NNNN", "NNNN", "NNNN", "NNNN" }
Here the only correct answer is a graph with four vertices and no edges.
2)	
    	
{3,3,3}
Returns: {"NYY", "YNY", "YYN" }
This time one correct answer could be the complete graph on three vertices.
3)	
    	
{4,4,4,4,4}
Returns: { }
There is no solution.
4)	
    	
{1}
Returns: {"N" }



'''

class ConnectedComponentConstruction :
	def construct(self, s):

		# create default result array in which there are no edges i.e all 'N'
		res =[['N' for j in s] for i in s]

		# Now iterate s
		for ind, val in enumerate(s):	

			# findhow may times val is present in s	
			count = s.count(val) 

			# if val ==1 or required edges are already present then skip this index
			if val == 1 or res[ind].count('Y') == val - 1:
				continue

			# if count is not divisible by val then graph is not possible
			# eg :{4,4,4,4,4} val =4 and count is 5 so no graph is possible
			elif count % val != 0 : return {}
			else:
				# set n to total edges already present. n will be updated till it
				# reaches val - 1 
				n = res[ind].count('Y')		
		 		for i in range(ind,len(s)):
		 			# update res when another node with same value found
		 			if  n < val - 1 and i!= ind and s[i] == val:	
		 				res[ind][i] = 'Y'
		 				res[i][ind] = 'Y'
		 				n = n + 1

		res = map(lambda x: "".join(x),res)	 	
		return res			 	

s = [ 3, 3, 3, 3, 3, 3]
c = ConnectedComponentConstruction()

print c.construct(s)

