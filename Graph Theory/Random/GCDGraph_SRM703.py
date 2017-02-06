'''

https://community.topcoder.com/stat?c=problem_statement&pm=14461&rd=16848

Problem Statement
    	You are given four ints: n, k, x, and y. 



The ints n and k describe a simple undirected graph. The graph has n nodes, numbered 1 through n. Two distinct vertices i and j are connected by an edge if and only if gcd(i, j) > k. Here, gcd(i, j) denotes the greatest common divisor of i and j. 



The ints x and y are the numbers of two (not necessarily distinct) vertices in our graph. Return "Possible" if it is possible to travel from x to y by following the edges of our graph. Otherwise, return "Impossible". 



In other words, return "Possible" if our graph contains a path that connects the nodes x and y, and "Impossible" if there is no such path.
 
Definition
    	
Class:	GCDGraph
Method:	possible
Parameters:	int, int, int, int
Returns:	String
Method signature:	String possible(int n, int k, int x, int y)
(be sure your method is public)
    
 
Constraints
-	n will be between 2 and 1,000,000, inclusive.
-	k will be between 0 and n, inclusive.
-	x and y will be between 1 and n, inclusive.
 
Examples
0)	
    	
12
2
8
9
Returns: "Possible"
We have a graph with n = 12 nodes. As k = 2, vertices i and j are connected by an edge if and only if gcd(i, j) is strictly greater than 2. In this graph it is possible to travel from node 8 to node 9. One possible path: 8 -> 4 -> 12 -> 9.
1)	
    	
12
2
11
12
Returns: "Impossible"
This is the same graph as in Example 0, but now we are interested in another pair of nodes. It is not possible to travel from node 11 to node 12. In particular, in our graph node 11 is an isolated node because for any other node x we have gcd(11, x) = 1.
2)	
    	
12
2
11
11
Returns: "Possible"
A node is always reachable from itself.
3)	
    	
10
2
8
9
Returns: "Impossible"
4)	
    	
1000000
1000
12345
54321
Returns: "Possible"
5)	
    	
1000000
2000
12345
54321
Returns: "Impossible"
6)	
    	
2
0
1
2
Returns: "Possible"

'''


class GCDGraph:
	
	def possible(self,n, k, x, y):
		parent = [i for i in range(n + 1)]	# set i as its own parent	
		for i in range(k+1 , (n+1)/2+1): # gcd > k so start from k and take only n/2 number coz 2*(n/2) will be out of range
			for j in range(i+i, n+1, i): # find all multiple of i and set their parent value
				self.union(i, j, parent)			
		return "Possible" if self.find(x, parent) == self.find(y, parent) else "Impossible"

	# find using path compression	
	def find(self,i, parent):
		if parent[i] != i:
			parent[i] = self.find(parent[i], parent)
		return parent[i]

	# union using rank( here integer value)
	def union(self, i, j, parent):
		p = self.find(i, parent)
		m = self.find(j, parent)
		if m < p:
			parent[p] = m
		else:
			parent[m] = p



g = GCDGraph()

n,k,x,y = 12, 2, 8, 9

print(g.possible(n, k, x, y))