# An Iterative python program to do DFS traversal from
# all vertices.Change node color from white to gray to black and
# also show their start and finish time 
 
from collections import defaultdict

class clr:
	WHITE = 0
	GREY = 1
	BLACK = 2
 
#This class represents a directed graph using adjacency list representation
class Graph:
 
	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
		self.time = 1
 
	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
 
	#A prints all not yet visited vertices reachable from v
	def DFSUtil(self, v, color, start_time, end_time):

		#print  v, color, start_time, end_time, time
		#Create a stack for DFS
		stack = []

		# For the first node only,
		# Mark the current node as visited and push it
		# set color and start time
		stack.append(v)
		color[v] = clr.GREY
		start_time[v] = self.time 
		self.time  = self.time  + 1

		while stack:

			s= stack[-1] #get top element

			# If s key exist in the dictionary and its value is not 
			# empty list
			if s in self.graph.keys() and self.graph[s] != []:

				# get the first adjacent vertex and remove it from the dictionary
				# mark it color and set start time
				i = self.graph[s][0] 
				del self.graph[s][0]
				if color[i] == clr.WHITE:
					color[i]= clr.GREY
					stack.append(i)
					start_time[i] = self.time  
					self.time  = self.time  + 1
			else:
				# This code is executed when s has no neighbours or
				# no white neighbours
				# Set the color and end time
				color[s] = clr.BLACK
				end_time[s] = self.time  
				self.time  = self.time  + 1

				# pop the last element as its done.
				# print the current state of start and end array
				print ("Node finished  :  %d " %stack.pop())
				print "Start array : " + str(start_time)
				print "Finish array : " + str(end_time)


	#prints all vertices in DFS manner
	def DFS(self):
 
		# Mark all the vertices as not visited by setting color to white
		# start time and end time of all node is set to Infinity
		color = [clr.WHITE] *(self.V)
		start_time = [float("Inf")]*(self.V)
		end_time = [float("Inf")]*(self.V)


		# Call the  helper function to print DFS traversal
        #starting from all vertices one by one
		for i in range(self.V):
			if color[i]==clr.WHITE:
				self.DFSUtil(i, color, start_time, end_time)

		#print color, start_time, end_time
 
# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(1, 3)

 
print "Following is Depth First Traversal \n"
g.DFS()