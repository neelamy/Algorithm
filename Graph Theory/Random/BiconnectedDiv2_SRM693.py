'''
https://community.topcoder.com/stat?c=problem_statement&pm=14332

Problem Statement
    	A biconnected graph is a connected undirected graph with the following property: for any three distinct vertices u,v,w there exists a path from u to v that does not contain w.

You are given a graph G with n vertices numbered 0 through n-1, where n is not less than 3. The graph has a very specific structure. For each i between 0 and n-2, inclusive, vertices i and i+1 are connected by an edge with weight w1[i]. Additionally, for each i between 0 and n-3, inclusive, vertices i and i+2 are connected by an edge with weight w2[i]. It is easy to verify that this graph is biconnected.

Note that some of the edge weights may be zeros or negative integers. An edge with weight zero is still present in the graph and it may contribute to its biconnectedness.

You may erase some edges of the graph G. If you do, you must do it in such a way that the graph remains biconnected. Your goal is to minimize the sum of weights of edges that remain in G.

You are given the int[]s w1 and w2 that describe the graph G. Compute and return the smallest possible sum of weights of a graph that can be produced in the way described above.

 
Definition
    	
Class:	BiconnectedDiv2
Method:	minimize
Parameters:	int[], int[]
Returns:	int
Method signature:	int minimize(int[] w1, int[] w2)
(be sure your method is public)
    
 
Constraints
-	n will be between 3 and 100, inclusive.
-	w1 will contain exactly n-1 elements.
-	w2 will contain exactly n-2 elements.
-	Each element of w1 and w2 will be between -10,000 and 10,000, inclusive.
 
Examples
0)	
    	
{1,2}
{3}
Returns: 6
There are three vertices and three edges (0,1), (1,2), (2,0). If you erase edge (0,1), then any path from 0 to 1 has to go through vertex 2. And if you erase two or more edges, the graph will become disconnected. So you cannot erase anything.
1)	
    	
{-1,-2,-3}
{-4,-5}
Returns: -15
An optimal solution is to keep all the edges.
2)	
    	
{1,100,-3,2}
{-2,1,4}
Returns: 3
An optimal solution is to erase edge (1,2).

'''

'''
Solution: add w2 as removing any edge from w2 will make the graph non-biconnected. Add w1[0] and w1[n-1](i.e.first and last element).
Now except first and last element of w1, rest all are exceptional edges and can be removed. SO add them only if they are -ve
'''
class BiconnectedDiv2: 
	def minimize(self, w1, w2):
		return sum(w2 )+ w1[0] + w1[-1] + reduce(lambda x,y: x if y > 0 else x + y, w1[1: -1], 0 )
  


b= BiconnectedDiv2()

w1,w2 =[-1,-2,-3], [-4,-5]

print b.minimize(w1, w2)
