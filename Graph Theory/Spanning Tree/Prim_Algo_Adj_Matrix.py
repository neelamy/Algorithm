# Python program for Prim's Minimum Spanning Tree (MST) algorithm. 
# The program is for adjacency matrix representation of the graph
#Complexity : O(V^2)

from collections import defaultdict

#Class to represent a graph
class Graph:

	# A utility function to find the vertex with minimum key value, from
	# the set of vertices still in queue
	def get_min(self,key,queue):

		# Initialize min value and index as -1
		minimum = float("Inf")
		index =-1

		#from the key array,pick one which has min value and is till in queue
		for i in range(len(key)):
			if key[i] < minimum and i in queue:
				minimum = key[i]
				index =i
		return index

	
	# Function to construct and print MST for a graph represented using adjacency
	# matrix representation
	def primMST(self,graph):

		print "Edge \t\t Weight"

		row = len(graph)
		col = len(graph[0])

		# Initialize all distance as INFINITE
		key = [float("Inf")] * row

		# Always include first 1st vertex in MST
		key[0] = 0 # Make key 0 so that this vertex is picked as first vertex

		# Array to store constructed MST
		parent = [-1] * row
		parent[0] = 0 # First node is always root of MST
		
		# Add all vertices in queue
		queue = []
		for i in range(row):
			queue.append(i)
			

		while queue:

			# Pick the minimum key vertex from the set of vertices
        	# still in queue
			u = self.get_min(key,queue)	

			# remove min element and print it	
			queue.remove(u)
			print str(parent[u]) + "-" + str(u) + "\t\t" + str(graph[parent[u]][u])

			# Update key value and parent index of the adjacent vertices of
        	# the picked vertex. Consider only those vertices which are still in
        	# queue
			for i in range(col):
				if graph[u][i] and i in queue:
					if graph[u][i] < key[i]:
						key[i] = graph[u][i]
						parent[i] =u

		# print total distance
		print sum(key)


g= Graph()

graph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]

#Print the solution
g.primMST(graph)

 