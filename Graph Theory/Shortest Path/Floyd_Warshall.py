# Python program for Pfor Floyd Warshall Algorithm algorithm. 
# The program is for adjacency matrix representation of the graph
#Complexity : O(V^3)

from collections import defaultdict

#Class to represent a graph
class Graph:

	def __init__(self, vertices):
		self.V = vertices

	# A utility function to print the solution
	def printSolution(self, dist):
		print ("Following matrix shows the shortest distances "
 				"between every pair of vertices")
		for i in range(self.V):
			for j in range(self.V):
				if(dist[i][j] == INF):
					print "%7s\t" %("INF"),
				else:
					print "%7d\t" %(dist[i][j]),
			print ""
    
	
	# Solves the all-pairs shortest path problem using Floyd Warshall algorithm
	def floydWarshal(self,graph):
		'''dist[][] will be the output matrix that will finally
        have the shortest distances between every pair of vertices
    	initializing the solution matrix same as input graph matrix
    	OR we can say that the initial values of shortest distances
    	are based on shortest paths considerting no 
    	intermedidate vertices '''
		dist =[i[:] for i in graph]
		'''Add all vertices one by one to the set of intermediate
    	vertices.
     	---> Before start of a iteration, we have shortest distances
     	between all pairs of vertices such that the shortest
     	distances consider only the vertices in set 
    	{0, 1, 2, .. k-1} as intermediate vertices.
      	----> After the end of an iteration, vertex no. k is
     	added to the set of intermediate vertices and the 
    	set becomes {0, 1, 2, .. k}'''
		for k in range(self.V):
			# Pick all vertices as source one by one
			for i in range(self.V):
				# Pick all vertices as destination for the
            	# above picked source
				for j in range(self.V):
					# If vertex k is on the shortest path from 
               		# i to j, then update the value of dist[i][j]
					if dist[i][j] > dist[i][k] + dist[k][j]:
						dist[i][j] = dist[i][k] + dist[k][j]

		self.printSolution(dist)


g= Graph(4)

INF = 9999

graph = [[0,   5,  INF, 10],
         [INF, 0,   3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]]
        

#Print the solution
g.floydWarshal(graph)

 