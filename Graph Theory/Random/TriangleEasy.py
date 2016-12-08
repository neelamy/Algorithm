'''
Topcoder : SRM693

Link:https://community.topcoder.com/stat?c=problem_statement&pm=14324&rd=16748
Problem:

Problem Statement
    	You are given an undirected graph with n vertices numbered 0 through n-1. For each valid i, there is an undirected edge connecting two different vertices x[i] and y[i]. No two edges connect the same pair of vertices.

A triangle is a set of three distinct vertices such that each pair of those vertices is connected by an edge. Formally, three distinct vertices u,v,w are a triangle if the graph contains the edges (u,v), (v,w), and (w,u).

You are given the description of the graph: the int n and the int[]s x and y. You are allowed to add edges to this graph. You may add as many edges as you want, and each of them may connect any two vertices. Your goal is to produce a graph that contains at least one triangle. Compute and return the smallest number of edges you need to add.

 
Definition
    	
Class:	TriangleEasy
Method:	find
Parameters:	int, int[], int[]
Returns:	int
Method signature:	int find(int n, int[] x, int[] y)
(be sure your method is public)
    
 
Constraints
-	n will be between 3 and 50, inclusive.
-	x will have between 0 and n*(n-1)/2 elements, inclusive.
-	y will have the same number of elements as x.
-	Each element of x and y will be between 0 and n-1, inclusive.
-	For each valid i, x[i] != y[i].
-	No two edges will connect the same pair of vertices.
 
Examples
0)	
    	
3
x={}
y={}
Returns: 3
The graph has three vertices but no edges. You need to add edges (0,1), (1,2), and (2,0) to make it a triangle.
1)	
    	
4
{0,2,1,2}
{3,0,2,3}
Returns: 0
Note that the edges are undirected. The graph already has a triangle: (2,0),(0,3),(2,3), so we don't have to add anything.
2)	
    	
6
{0,0,2}
{3,1,4}
Returns: 1
3)	
    	
4
{0,2}
{1,3}
Returns: 2
4)	
    	
20
{16,4,15,6,1,0,10,12,7,15,2,4,8,1,10,15,13,10,1,16,3,19,8,7,13,1,15,15,15,5,16,7,5,6,4,18,3,8,6,2,16,8,19,14,17,16,4,6,9,17,4,10,8,12,2,3,18,9,13,17,4,7,10,0,13,11,15,17,11,15,11,19,19,4,10,14,16,6,3,17,1,4,14,9,7,18,10,11,5,0,5,9,9,7,16,12,4,10,17,3}
{17,18,6,16,18,6,11,2,15,10,1,15,17,8,5,9,7,0,0,4,16,1,9,0,9,5,17,14,1,12,14,11,9,18,0,12,11,3,19,14,7,6,3,19,0,1,19,5,11,19,2,13,12,0,6,2,14,16,14,18,5,5,19,3,6,14,12,5,17,3,1,12,7,11,8,8,10,11,13,2,13,13,0,18,2,7,2,12,14,9,3,19,2,8,12,13,8,18,13,18}
Returns: 1




'''
class TriangleEasy:
	def find(self,n,x,y):
		edges ={};result=3
		for i in range(len(x)):
			edge1 = str(x[i]) +"-"+ str(y[i])
			edge2 = str(y[i]) +"-"+ str(x[i])
			#set the weight of edges as 1
			edges[edge1]=1
			edges[edge2]=1
			
		for i in range(0,n):
			for j in range(0,n):
				if i==j:
					continue
				for k in range(0,n):
					if i==k or k==j:
						continue
					ij= str(i) +"-"+ str(j)
					jk= str(j) +"-"+ str(k)
					ki= str(k) +"-"+ str(i)
					connection = edges.get(ij,0)+edges.get(jk,0)+edges.get(ki,0)
					if connection ==3:
						return 0
					else:
						result = min(3-connection , result)
		return result


test = TriangleEasy()
n=20
x =[16,4,15,6,1,0,10,12,7,15,2,4,8,1,10,15,13,10,1,16,3,19,8,7,13,1,15,15,15,5,16,7,5,6,4,18,3,8,6,2,16,8,19,14,17,16,4,6,9,17,4,10,8,12,2,3,18,9,13,17,4,7,10,0,13,11,15,17,11,15,11,19,19,4,10,14,16,6,3,17,1,4,14,9,7,18,10,11,5,0,5,9,9,7,16,12,4,10,17,3]
y =[17,18,6,16,18,6,11,2,15,10,1,15,17,8,5,9,7,0,0,4,16,1,9,0,9,5,17,14,1,12,14,11,9,18,0,12,11,3,19,14,7,6,3,19,0,1,19,5,11,19,2,13,12,0,6,2,14,16,14,18,5,5,19,3,6,14,12,5,17,3,1,12,7,11,8,8,10,11,13,2,13,13,0,18,2,7,2,12,14,9,3,19,2,8,12,13,8,18,13,18]


print (test.find(n,x,y))