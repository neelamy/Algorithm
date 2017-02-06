
# http://www.geeksforgeeks.org/find-maximum-dot-product-two-arrays-insertion-0s/

# Complexity : (n * m)

class DotProduct:

	def Add_zero(self,dp, i, j):

		# if len(A) < i or len(B) < j then return 0
		if i >= len(self.A) or j >= len(self.B):return 0

		if dp[i][j]: 
			return dp[i][j]

		# if remaning length is equal then return the product of all digits from i till end
		if len(self.A)-i == len(self.B)-j : 

			return reduce(lambda x, y: x + (y[0] * y[1]),zip(self.A[i:],self.B[j:]),0)

		# case 1: considering B[i] = 0 i.e ignoring A[i] and then recurse for remaining numbers
		sum1 = self.Add_zero(dp,i + 1, j)
	
		# case 2 : Multiply by A[i] * B[i] and then recurse for remaining numbers
		sum2 = self.A[i] * self.B[j] + self.Add_zero(dp,i + 1, j + 1)

		# select maximum of two and assign it to dp[i][j]
		dp[i][j] =  max(sum1, sum2)

		return dp[i][j]



	def Maximize_Dot_Prod(self):
		m = len(self.A)

		n = len(self.B)
		
		dp =[[0 for j in range(n)] for i in range(m)]
		
		print self.Add_zero(dp,0, 0)

		
def main():
	o = DotProduct()
	
	o.A = [2, 3 , 1, 7, 8]
	
	o.B = [3, 6, 7]
	
	o.Maximize_Dot_Prod()



if __name__ == '__main__':
	main()
