# Python program for Dijkstra algorithm to find shortest path
# from source in undirected graph 
# The program is for adjacency list representation of the graph
#Complexity : O(V(V+E))

from collections import defaultdict

#Class to represent a graph
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
 
	# function to add an edge to graph
	def addEdge(self,u,v,w):
		self.graph[u].append((v,w))
		self.graph[v].append((u,w))

	# A utility function to find the vertex with minimum dist value, from
	# the set of vertices still in queue
	def get_min(self,dist,queue):

		# Initialize min value and index as -1
		minimum = float("Inf")
		index =-1

		#from the dist array,pick one which has min value and is till in queue
		for i in range(len(dist)):
			if dist[i] < minimum and i in queue:
				minimum = dist[i]
				index =i
		return index

	# print the solution
	def printSolution(self, dist):
		print("Vertex   Distance from Source")
		for i in range(self.V):
			print("%d \t\t %d" % (i, dist[i]))
	
	# Function to construct and print MST for a graph represented using adjacency
	# matrix representation
	def dijkstra(self, src):

		# Initialize all dist/distance as INFINITE
		dist = [float("Inf")] * self.V

		# Always include first 1st vertex in MST
		dist[src] = 0 # Make dist 0 so that this vertex is picked as first vertex

		# Add all vertices in queue
		queue = []

		for i in range(self.V):
			queue.append(i)		

		while queue:

			# Pick the minimum dist vertex from the set of vertices
        	# still in queue
			u = self.get_min(dist,queue)	

			# remove min element and print it	
			queue.remove(u)

			# Update dist value and parent index of the adjacent vertices of
        	# the picked vertex. Consider only those vertices which are still in
        	# queue
			for node,weight in self.graph[u]:
				if node in queue and dist[u] + weight < dist[node]:
						dist[node] = dist[u] + weight
						
		# print all distance
		self.printSolution(dist)


g = Graph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

#Print the solution
g.dijkstra(0)

 