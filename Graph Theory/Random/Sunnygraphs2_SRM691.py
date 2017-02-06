'''
https://community.topcoder.com/stat?c=problem_statement&pm=14302


Problem Statement
    	Hero has just constructed a very specific graph. He started with n isolated vertices, labeled 0 through n-1. For each vertex i Hero then chose a vertex a[i] (other than i) and he added an edge that connected i and a[i]. This way he created a graph with n vertices and n edges. Note that if a[x]=y and a[y]=x, the vertices x and y were connected by two different edges. Hero now wants to perform the following procedure:
Add a new isolated vertex number n.
Choose a subset M of the original vertices.
For each x in M, erase an edge between vertices x and a[x].
For each x in M, add a new edge between vertices x and n.
Hero's goal is to create a final graph in which the vertices 0 through n-1 are all in the same connected component. (I.e., there must be a way to reach any of these vertices from any other of them by following one or more consecutive edges, possibly visiting vertex n along the way.) Note that Hero does not care whether vertex n is in the same component as the other vertices: both possibilities are fine. In step 2 of the above procedure Hero has 2^n possible subsets to choose from. A choice of M is good if it produces a graph with the desired property. Count how many of the 2^n possibilities are good choices. Return that count as a long.
 
Definition
    	
Class:	Sunnygraphs2
Method:	count
Parameters:	int[]
Returns:	long
Method signature:	long count(int[] a)
(be sure your method is public)
    
 
Constraints
-	a will contain n elements.
-	n will be between 2 and 50, inclusive.
-	Each element in a will be between 0 and n - 1, inclusive.
-	For each i between 0 and n - 1 holds a[i] != i.
 
Examples
0)	
    	
{1,0}
Returns: 4
The original graph contained the vertices 0 and 1. This pair of vertices was connected by two edges. Next, Hero added a new vertex 2. Then he had to choose one of four possible subsets M:
If he chose M = {}, the resulting graph contained the edges 0-1 and 0-1. The vertices 0 and 1 were in the same component.
If he chose M = {0}, the resulting graph contained the edges 0-1 and 0-2. The vertices 0 and 1 were in the same component.
If he chose M = {1}, the resulting graph contained the edges 0-1 and 1-2. The vertices 0 and 1 were in the same component.
Finally, if he chose M = {0, 1}, the resulting graph contained the edges 0-2 and 1-2. And again, the vertices 0 and 1 were in the same component. (In the resulting graph we can still go from vertex 0 to vertex 1, even though we have to go via vertex 2.)
As all four choices of M are good, the correct answer is 4.
1)	
    	
{1,0,0}
Returns: 7
Here, M = {2} is not a good choice. This choice produces a graph with edges 0-1, 0-1, and 2-3. In this graph vertex 2 is not in the same component as vertices 0 and 1. The other seven possible choices of M are all good.
2)	
    	
{2,3,0,1}
Returns: 9
3)	
    	
{2,3,0,1,0}
Returns: 18
4)	
    	
{2,3,0,1,0,4,5,2,3}
Returns: 288
5)	
    	
{29,34,40,17,16,12,0,40,20,35,5,13,27,7,29,13,14,39,42,9,30,38,27,40,34,33,42,20,29,42,12,29,30,21,4,5,7,25,24,17,39,32,9}
Returns: 6184752906240
"Watch out for integer overflow."
6)	
    	
{9,2,0,43,12,14,39,25,24,3,16,17,22,0,6,21,18,29,34,35,23,43,28,28,20,11,5,12,31,24,8,13,17,10,15,9,15,26,4,13,21,27,36,39}
Returns: 17317308137473
'''

'''Solution : https://apps.topcoder.com/wiki/display/tc/SRM+691'''
class Sunnygraphs2:
	def count(self, a):

		l= len(a)
		visited = [False] * (l)
		cycle =[]
		# find all cycles in graph and store their length in cycle 
		for i in range(l):
			if visited[i] == True : continue
			dest = a[i]; j = 0
			while i != dest and j < l:
				dest = a[dest]
				j += 1
			if i == dest:
				cycle_length = 1
				visited [i] = True
				dest = a[i]
				while i != dest:
					visited [dest] = True
					dest = a[dest]
					cycle_length += 1
				cycle.append(cycle_length)

		# find all non-cycle nodes		
		nodes_not_in_cycle = l - sum(cycle)

		# if only one cycle present that means nodes are already connected. Innext step we will do (2^ 1st cycle length -1)
		# However in one cycle case -1 is not required as we can select 0 nodes and still it will be connected
		# so we +1 for single cycle case
		res = 1 if len(cycle)==1 else 0

		# res = res * (2^ non_cycle_nodes) * (2^ 1st cycle length -1 ) * (2^ 2nd cycle length -1 ) * (2^ 3d cycle length -1 ) ....
		# selecting atleast one node from cycle is necessary so -1 to remove no node option
		res += (2 ** nodes_not_in_cycle) * reduce((lambda x, y : (2**x-1)* (2**y-1)), cycle,1)
		return res



s = Sunnygraphs2()

a = [9,2,0,43,12,14,39,25,24,3,16,17,22,0,6,21,18,29,34,35,23,43,28,28,20,11,5,12,31,24,8,13,17,10,15,9,15,26,4,13,21,27,36,39]

print s.count(a)