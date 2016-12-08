# Python program to find maximal Bipartite matching.
# Complexity : (E*(V^3))
# Total augmenting path = VE and BFS with adj matrix takes :V^2 times
 
from collections import defaultdict
 
#This class represents a directed graph using adjacency matrix representation
class Graph:
 
	def __init__(self,graph):
		self.graph = graph # residual graph
			
 
	'''Returns true if there is a path from source 's' to sink 't' in
	residual graph. Also fills parent[] to store the path '''
	def BFS(self,s, t, parent):

		# Mark all the vertices as not visited
		visited =[False] * len(self.graph)

		# Create a queue for BFS
		queue=[]
		
		# Mark the source node as visited and enqueue it
		queue.append(s)
		visited[s] = True
 		
 		# Standard BFS Loop
		while queue:

			#Dequeue a vertex from queue and print it
			u = queue.pop(0)
		
			# Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
			for ind, val in enumerate(self.graph[u]):
				if visited[ind] == False and val > 0 :
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u

		# If we reached sink in BFS starting from source, then return
    	# true, else false
		return True if visited[t] else False
			
	
	# Returns maximum number of matching from M to N
	def maxBPM(self):

		ppl = len(self.graph)
		jobs = len(self.graph[0])
		nodes = jobs + ppl + 2

		'''
		Now we need to create new graph of size (M + N + 2) * (M + N + 2)
		Row 0-5 : ppl, Row 6-11 : jobs, Row 12 : source, Row 13 : sink
		'''
		gr = [[0 for j in range(nodes)] for i in range(nodes)]
		source = nodes - 2 # as nodes starts from 0
		sink = nodes - 1 # as nodes starts from 0

		# connect source(node 12) to all ppl(0 to 5)
		for i in range(ppl):
			gr[source][i] = 1

		# connect all jobs(node 6 to 12) to sink (node 13)
		for i in range(ppl,nodes - 2):
			gr[i][sink] = 1

		# now connect ppl to jobs as per original graph
		for i in range(len(self.graph)):
			for j in range(len(self.graph[0])):
				if self.graph[i][j]:
					gr[i][ j + ppl ] = 1

		self.graph = gr

		# Now perform normal Ford-Fulkerson

		# This array is filled by BFS and to store path
		parent = [-1] * len(self.graph)

		max_flow = 0 # There is no flow initially

		# Augment the flow while there is path from source to sink
		while self.BFS(source, sink, parent) :

			# Find minimum residual capacity of the edges along the
        	# path filled by BFS. Or we can say find the maximum flow
        	# through the path found.
			path_flow = float("Inf")
			s = sink
			while(s !=  source):
				path_flow = min (path_flow, self.graph[parent[s]][s])
				s = parent[s]

			# Add path flow to overall flow
			max_flow +=  path_flow

			# update residual capacities of the edges and reverse edges
        	# along the path
			v = sink
			while(v !=  source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]

		print max_flow
	
 
# Create a graph given in the above diagram

bpGraph =[[0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1]]

g = Graph(bpGraph)

print ("Maximum number of applicants that can get job is")
g.maxBPM()
 