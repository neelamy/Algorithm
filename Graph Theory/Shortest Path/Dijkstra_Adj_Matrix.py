# Python program for Dijkstra algorithm to find shortest path
# from source in undirected graph 
# The program is for adjacency matrix representation of the graph
#Complexity : O(V^2)

from collections import defaultdict

#Class to represent a graph
class Graph:

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
		for i in range(len(dist)):
			print("%d \t\t %d" % (i, dist[i]))

	
	# Function to construct and print MST for a graph represented using adjacency
	# matrix representation
	def dijkstra(self, graph, src):

		print "Edge \t\t Weight"

		row = len(graph)
		col = len(graph[0])

		# Initialize all distance as INFINITE
		dist = [float("Inf")] * row

		# Always include first 1st vertex in MST
		dist[src] = 0 # Make dist 0 so that this vertex is picked as first vertex
	
		# Add all vertices in queue
		queue = []
		for i in range(row):
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
			for i in range(col):
				if graph[u][i] and i in queue:
					if dist[u] + graph[u][i] < dist[i]:
						dist[i] = dist[u] + graph[u][i]


		# print all distance
		self.printSolution(dist)



g= Graph()

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]
		]

#Print the solution
g.dijkstra(graph,0)

 