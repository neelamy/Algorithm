# Python program for Prim's Minimum Spanning Tree (MST) algorithm. 
# The program is for adjacency list representation of the graph
# It uses min heap to store key values
#Complexity : O(V(V+E))

from collections import defaultdict
import heapq as h

#Class to represent a graph
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
 
	# function to add an edge to graph
	def addEdge(self,u,v,w):
		self.graph[u].append((v,w))
		self.graph[v].append((u,w))

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
	def primMST(self):


		#key = PriorityQueue()
		key =[]

		parent = [-1] * self.V
		connected = [-1] * self.V

		for i in range(self.V):
			h.heappush(key,(float("Inf"),i))

		key[0] = (112,0)

		print key[112]

		# while key:
		# 	d,u = h.heappop(key)
			
		# 	if connected[u]!= -1:

		# 		connected[u] == 1
		# 		for node, weight in self.graph[u]:
		# 			if key[node] > weight:
		# 				key[node] == weight
		# 				h.heappush(key,(weight,node))

		


		




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
g.primMST()

 