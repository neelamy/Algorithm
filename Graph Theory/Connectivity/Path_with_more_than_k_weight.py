# Program to find if there is a simple path with
# weight more than k in undirected graph

from collections import defaultdict

#Class to represent a undirected graph
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
 
	# function to add an edge to graph
	def addEdge(self,u,v,w):
		self.graph[u].append((v,w))
		self.graph[v].append((u,w))

	# return True if path length more than k
	def pathMoreThanKUtil(self, u, k, path):

		# If k is negative, return true
		if k < 0 : return True

		# mark u as visited
		path[u] = True

		# Get all adjacent vertices of source vertex u and
    	# Recursively explore all paths from u.
		for v, w in self.graph[u]:

			# Take v if its not already in path
			if path[v] == False:
				# If weight of is more than k, return true
				if w > k : return True

				# If this adjacent can provide a path longer
        		# than k, return true
				if self.pathMoreThanKUtil(v, k-w, path):
					return True

		# Backtrack and remove the node from path			
		path[u] = False
		return False
		
	# Returns true if graph has path more than k length
	def pathMoreThanK(self, src, k):
		path = [False] * self.V
		return self.pathMoreThanKUtil(src, k, path)


g = Graph(9)
g.addEdge(0, 7, 8)
g.addEdge(0, 1, 4)
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
src = 0; k = 62;
print "Yes" if g.pathMoreThanK(src, k) else "No"

src = 0; k = 60;
print "Yes" if g.pathMoreThanK(src, k) else "No"

 