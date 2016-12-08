
# Python program to count triangles in a graph.  The program is
# for adjacency matrix representation of the graph.


# function to calculate the number of triangles in a simple
# directed/undirected graph.
# isDirected is true if the graph is directed, its false otherwise
def countTriangle(g, isDirected):
	nodes = len(g)
	count_Triangle = 0 #Initialize result
	# Consider every possible triplet of edges in graph
	for i in range(nodes):
		for j in range(nodes):
			for k in range(nodes):
				# check the triplet if it satisfies the condition
				if( i!=j and i !=k and j !=k and 
						g[i][j] and g[j][k] and g[k][i]):
					count_Triangle += 1
	# if there is a triangle 0->1->2 then it is counted 3 times 0->1->2, 1->2->0 and
	# 2->1->0 so divide total count by 3			
	# if graph is directed , division is done by 3
    # else division by 6 is done
	return count_Triangle/3 if isDirected else count_Triangle/6

# Create adjacency matrix of an undirected graph
graph = [[0, 1, 1, 0],
       [1, 0, 1, 1],
       [1, 1, 0, 1],
       [0, 1, 1, 0 ]]
# Create adjacency matrix of a directed graph
digraph = [[0, 0, 1, 0],
       	  [1, 0, 0, 1],
          [0, 1, 0, 0],
          [0, 0, 1, 0 ]]

print ("The Number of triangles in undirected graph : %d" %countTriangle(graph, False))

print ("The Number of triangles in directed graph : %d" %countTriangle(digraph, True))
