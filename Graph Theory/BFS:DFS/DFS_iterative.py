# An Iterative python program to do DFS traversal from
# all vertices. 
 
from collections import defaultdict
 
#This class represents a directed graph using adjacency list representation
class Graph:
 
	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
 
	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
 
	#A prints all not yet visited vertices reachable from v
	def DFSUtil(self,v,visited):

		#Create a stack for DFS
		stack = []

		#Mark the current node as visited and push it
		visited[v]= True
		stack.append(v)

		while stack:

			s= stack.pop()
			print s,

			# Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then mark it
            # visited and push it to the stack
			for i in self.graph[s]:
				if visited[i] == False:
					visited[i]= True
					stack.append(i)


	#prints all vertices in DFS manner
	def DFS(self):
 
		# Mark all the vertices as not visited
		visited =[False]*(self.V)

		
		
		# Call the  helper function to print DFS traversal
        #starting from all vertices one by one
		for i in range(self.V):
			if visited[i]==False:
				self.DFSUtil(i,visited)

 
# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(2, 1)
g.addEdge(3, 4)
g.addEdge(4, 0)
 
print "Following is Depth First Traversal \n"
g.DFS()