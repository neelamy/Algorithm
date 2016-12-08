
from collections import defaultdict

#Class to represent a graph
class Graph:


	# A naive recursive function to count walks from u to v with k edges
	def shortestPath(self, graph, u, v, k):	
		print u,v,k	
		if k==0 and u == v : return 0 #K==0 as we need exactly k edges
		if k == 1 : return graph[u][v]
		if k <= 0 : return float("Inf")
		res = float("Inf")
		for i in range(len(graph[u])):
			if graph[u][i] != float("Inf") and u!=i and v!=i :
				rec_res = self.shortestPath(graph, i, v, k-1)
				if rec_res != float("Inf") :
					res = min(res, graph[u][i] + rec_res)

		return res




g= Graph()

INF = float("Inf")

graph = [[0, 10, 3, 2],
		[INF, 0, INF, 7],
		[INF, INF, 0, 6],
		[INF, INF, INF, 0],
		]
u = 0
v = 3
k = 2
#Print the solution
print ("Weight of the shortest path is %d " %g.shortestPath(graph, u, v, k))
