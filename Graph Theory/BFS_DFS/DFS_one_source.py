# Python program to print DFS traversal from a given given graph
 
from collections import defaultdict
 
#This class represents a directed graph using adjacency list representation
class Graph:
 
	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
 
	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
 
	#A function used by DFS
	def DFSUtil(self,v,visited):
		# Mark the current node as visited and print it
		visited[v]= True
		print v
		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.DFSUtil(i,visited)
 
 
	#The function to do DFS traversal. It uses recursive DFSUtil()
	def DFS(self,v):
		# Mark all the vertices as not visited
		visited =[False]*(self.V)
		# Call the recursive helper function to print DFS traversal
		self.DFSUtil(v,visited)
 
 
 
# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print "Following is DFS from vertex 2 \n"
g.DFS(2)