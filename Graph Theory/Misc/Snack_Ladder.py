# Pythn program to find minimum number of dice throws required to
# reach last cell from first cell of a given snake and ladder
# board
# Complexity :O(V+E)


# This function returns minimum number of dice throws required to
# Reach last cell from 0'th cell in a snake and ladder game.
# move[] is an array of size N where N is no. of cells on board
# If there is no snake or ladder from cell i, then move[i] is -1
# Otherwise move[i] contains cell to which snake or ladder at i
# takes to.
def getMinDiceThrows(moves, N):

	#The graph has N vertices. Mark all the vertices as
    # not visited and length as -1
	visited = [False] * N
	Length = [-1] * N

	# Mark the node 0 as visited and enqueue it.
	source = 0
	queue = [source]
	visited[source] = True
	Length[source] = 0
	
	# Do a BFS starting from vertex at index 0
	while queue:
		u = queue.pop(0)
		#If front vertex is the destination vertex,
        # we are done
		if u == N - 1 : break
		# Otherwise dequeue the front vertex and enqueue
        # its adjacent vertices (or cell numbers reachable
        # through a dice throw)
		for i in range(u + 1, u + 7):
			# If this cell is already visited, then ignore
			if i < N and visited[i] == False:
				# Otherwise calculate its distance and mark it
                # as visited
				visited[i] = True
				# Check if there a snake or ladder at 'j'
                # then tail of snake or top o
				if moves[i] != -1 :
					visited[moves[i]] = True
					queue.append(moves[i])
					Length[moves[i]] = Length[u] + 1
				else:
					queue.append(i)
					Length[i] = Length[u] + 1
	
	return Length[N-1]	

N = 30

moves = [-1] * N
# Ladders
moves[2] = 21;
moves[4] = 7;
moves[10] = 25;
moves[19] = 28;

# Snakes
moves[26] = 0;
moves[20] = 8;
moves[16] = 3;
moves[18] = 6;

print ("Min Dice throws required is :  %d" % getMinDiceThrows(moves ,N))

