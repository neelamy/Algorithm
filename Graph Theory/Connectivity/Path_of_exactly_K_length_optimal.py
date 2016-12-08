'''
Python program to count all possible walks from a source to a destination with exactly k edges

If Adj Matrix is 'g' then path with exact k length = A^k
Instead of multiplying k times , we can get the result in O(log k) time.
This is called divide and conquer method.
Eg. 2^ 16 = (2^8)* (2^8) = (2^4)*(2^4)= (2^2)*(2^2)= (2^1)*(2^1)
SO instead of 16 times, we just have to multiply 4 times (4 = log 16)

Complexity : O(V^3 * log k)

Complexity of 1 matrix multiplication = O(V^3). Multiplication is done
log K times so total complexity = O(V^3 * log K)

Link: http://faculty.simpson.edu/lydia.sinapova/www/cmsc250/LN250_Tremblay/L16-ConnectedGraphs.htm

To print path :http://www.perlmonks.org/?node_id=522270

'''


def multiplication(a, b):
	row_a= len(a)
	col_a = len(a[0])
	col_b = len(b[0])
	c = [[0 for j in range(col_b)] for i in range(row_a)]
	for i in range(row_a):
		for j in range(col_b):
			for k in range(col_a):
				c[i][j] += a[i][k] * b[k][j]
	return c

def mat_power(g, k):
	if k == 1:
		return g
	res = mat_power(g, k / 2)
	res = multiplication(res, res)
	if k % 2 == 0:
		return res
	else:
		return multiplication(res, g)


graph = [[0,1,1,0,1,0,0,0],
		 [0,0,0,0,1,1,0,0],
		 [0,0,0,1,0,0,0,0],
		 [0,0,0,0,0,1,1,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,1,0,0,0],
		 [1,0,1,0,0,0,0,0],
		 [0,0,0,1,0,0,0,0]]

u = 6; v = 1

for i in range(1,10):
	print ("No of paths of length %d between %d and %d is :" % (i, u, v)),
	print mat_power(graph, i)[u][v]



