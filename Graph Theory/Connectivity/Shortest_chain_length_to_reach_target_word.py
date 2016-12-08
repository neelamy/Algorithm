# program to find length of the shortest chain transformation 
# from source to target

# To check if strings differ by exactly one character
def isadjacent(a, b):
	count = 0 # to store count of differences

	# itereate through all the characters in 'a'. If char is present in 'b'
	# then delete it from 'b' else increment count by 1
	for i in a:
		if i in b:
			b = b.replace(i,"",1)
		else: count +=1

	# return True if count is 1 and False otherwise
	return True if count ==1 else False
	

# Returns length of shortest chain to reach 'target' from 'start'
# using minimum number of adjacent moves.  D is dictionary
def shortestChainLen(start, target, D):
	
	N = len(D)

	# Initialize all words as not visited and distance for all words as -1
	visited = [False] * N
	Distance = [-1] * N

	# Create a queue for BFS and insert 'start' as source vertex
	queue = []
	queue. append(start)
	
	# While queue is not empty
	while queue:
		
		# Take the front word
		curr = queue.pop(0)

		# Go through all words of dictionary
		for ind, temp in enumerate(D):

			# Process a dictionary word if it is adjacent to current
            # word (or vertex) of BFS and is not yet visited
			if visited[ind] == False and isadjacent(curr, temp):
				
				# Add the dictionary word to queue
				queue. append(temp)
				visited[ind] = True

				# set distance of current word
				if curr == start:
					Distance[ind] = 2 # if it reaches from "start"
				else:
					 Distance[ind] = Distance[D.index(curr)] + 1

				# If we reached target
				if temp == target:
					print Distance[D.index(temp)]
					return


D = []
D.append("oonp")
D.append("plee")
D.append("same")
D.append("poie")
D.append("plie")
D.append("poin")
D.append("plea")
start = "toon"
target = "plea"
print "Length of shortest chain is: "
shortestChainLen(start, target, D)