# Python program to to detect cycle in a directed graph
#Complexity : O(ELogV).
 
from collections import defaultdict
 
#This class represents a directed graph using adjacency list representation
class Graph:
 
	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph

 
	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)	

 
	#This function is a variation of DFSUytil()
	def isCyclicUtil(self,v,visited,recStack):

		#Mark the current node as visited and part of recursion stack
		recStack[v] = True
		visited[v]= True

		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
				# If the node is not visited then recurse on it
				if  visited[i]==False and (self.isCyclicUtil(i,visited,recStack))==True:
					return True
				# if neighbor has been visited check if it is ancestor of v
				# i is ansector of v if its in stack
				elif recStack[i]==True :
					return True

		#remove the vertex from recursion stack
		recStack[v] = False
		return False
 		
 
	#Returns true if the graph contains a cycle, else false.
	def isCyclic(self):
		# Mark all the vertices as not visited and not part of recursion
        # stack
		visited =[False]*(self.V)
		recStack =[False]*(self.V)

		# Call the recursive helper function to detect cycle in different
        #DFS trees
		for i in range(self.V):
			if visited[i] ==False:
				if(self.isCyclicUtil(i,visited,recStack))== True:
					return True
		return False
 
 
 
# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 

if g.isCyclic():
	print "Graph contains cycle"
else :
	print "Graph does not contain cycle "
 