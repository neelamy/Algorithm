# Python program to find out whether a given graph is Bipartite or not

# This function returns true if graph is Bipartite, else false
def isBipartite(g):
	nodes = len(g)

	'''Create a color array to store colors assigned to all veritces. Vertex 
    number is used as index in this array. The value '-1' of  colorArr[i] 
    is used to indicate that no color is assigned to vertex 'i'.  The value 
    1 is used to indicate first color is assigned and value 0 indicates 
    second color is assigned.'''
	color = [-1] * nodes

	for i in range(nodes):
		for j in range(nodes):
			
			# An edge from i to j exists 
			if  i !=j  and g[i][j]:

				# If an edge from i to j exists and destination j is colored with
            	# different color as i then no change needed
				if color[i] != -1  and color[j] != -1 and color[i] != color[j] :
					continue

				# If an edge from i to j exists and destination j is colored with
            	# same color as i then return False
				elif color[i] != -1  and color[j] != -1 and color[i] == color[j] :
					return False

				else:
					# color i if not already colored
					if color[i] == -1:
						color[i] = 1
					# set alternate color to j
					color[j] = 1 - color[i]
						
	# If we reach here, then all adjacent vertices can be colored with 
    # alternate color	
	return True

G = [[0, 1, 0, 1],
   [1, 0, 1, 0],
   [0, 1, 0, 1],
   [1, 0, 1, 0]]

print "Yes" if isBipartite(G) else "No"