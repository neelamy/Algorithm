# Program to print BFS traversal from a given source vertex. BFS(int s) 
# traverses vertices reachable from s.
 
from collections import defaultdict
 
#This class represents a directed graph using adjacency list representation
class Graph:
 
	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
 
	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
 
	def BFS(self,s):
		# Mark all the vertices as not visited
		visited =[False]*(self.V)
 
		#Create a queue for BFS
		queue=[]
 
		#Mark the source node as visited and enqueue it
		queue.append(s)
		visited[s] = True
 
		while queue:
			#Dequeue a vertex from queue and print it
			s = queue.pop(0)
			print s
 
			# Get all adjacent vertices of the dequeued vertex s
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True
 
 
# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print "Following is BFS from vertex 2 \n"
g.BFS(2)