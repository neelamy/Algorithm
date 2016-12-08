
# Python program to count walks from u to v with exactly k edges

class Graph:

	def __init__(self, graph):
		self.graph = graph
	
	#  A naive recursive function to count walks from u to v with k edges
	def countwalks(self, u, v, k):	
		# Base cases	
		if k == 0 and u == v : return 1
		if k < 0 : return 0

		# Initialize result
		count = 0

		# Go to all adjacents of u and recur
		for index, value in enumerate(self.graph[u]):
		 	if value == 1 :
		 		count =  count + self.countwalks(index, v, k-1)
		return count

# Let us create the graph shown in above diagram
graph =	[[1, 1, 1, 1],
		[1, 0, 0, 1],
		[0, 1, 1, 1],
		[0, 1, 1, 0]]

g =  Graph(graph)

u = 0; v = 3; k = 2

print g.countwalks(u, v, k)