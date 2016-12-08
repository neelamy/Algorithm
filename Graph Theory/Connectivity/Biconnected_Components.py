# Python program to find biconnected components in a given
#  undirected graph
#Complexity : O(V+E)

 
from collections import defaultdict
 
#This class represents an directed graph using adjacency list representation
class Graph:
 
	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
		self.Time = 0 # time is used to find discovery times
		self.count = 0 # Count is number of biconnected components
 
	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v) 
 		self.graph[v].append(u)

	'''A recursive function that finds and prints strongly connected
    components using DFS traversal
    u --> The vertex to be visited next
    disc[] --> Stores discovery times of visited vertices
    low[] -- >> earliest visited vertex (the vertex with minimum
               discovery time) that can be reached from subtree
               rooted with current vertex
    st -- >> To store visited edges
    result -->> To store all edges already printed
    '''
	def BCCUtil(self,u, parent, low, disc, st, result):

		#Count of children in current node 
		children =0

		# Initialize discovery time and low value
		disc[u] = self.Time
		low[u] = self.Time
		self.Time += 1


		#Recur for all the vertices adjacent to this vertex
		for v in self.graph[u]:
			# If v is not visited yet, then make it a child of u
        	# in DFS tree and recur for it
			if disc[v] == -1 :
				parent[v] = u
				children += 1
				st.append((u, v)) #store the edge in stack
				self.BCCUtil(v, parent, low, disc, st, result)

				# Check if the subtree rooted with v has a connection to
            	# one of the ancestors of u
            	# Case 1 -- per Strongly Connected Components Article
				low[u] = min(low[u], low[v])

				# If u is an articulation point,pop all edges from stack till (u, v)
				if parent[u] == -1 and children > 1 or parent[u] != -1 and low[v] >= disc[u]:
					self.count +=1 # increment count
					w = -1
					while w != (u,v):
						w = st.pop()
						result.append(w) # store output edges
						print w,
					print""
			
			elif v != parent[u]:
				#Update low value of 'u' only of 'v' is still in stack
				low[u] = min(low [u], disc[v])

				# add the edge if (u,v) and (v,u) are not already in stack
				# or result
				if ((u,v) not in st and (v,u) not in st and 
					(u,v) not in result and (v,u) not in result):
					st.append((u,v))


	#The function to do DFS traversal. It uses recursive BCCUtil()
	def BCC(self):
		
		# Initialize disc and low, and parent arrays
		disc = [-1] * (self.V)
		low = [-1] * (self.V)
		parent = [-1] * (self.V)
		st = []
		result = []

		# Call the recursive helper function to find articulation points
		# in DFS tree rooted with vertex 'i'
		for i in range(self.V):
			if disc[i] == -1:
				self.BCCUtil(i, parent, low, disc, st, result)

			#If stack is not empty, pop all edges from stack
			if st:
				self.count = self.count + 1

				while st:
					w = st.pop()
					result.append(w) # store output edges
					print w,
				print ""
		
 
# Create a graph given in the above diagram

g = Graph(12)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(3,4)
g.addEdge(1,5)
g.addEdge(0,6)
g.addEdge(5,6)
g.addEdge(5,7)
g.addEdge(5,8)
g.addEdge(7,8)
g.addEdge(8,9)
g.addEdge(10,11)

g.BCC();
print ("Above are %d biconnected components in graph" %(g.count));