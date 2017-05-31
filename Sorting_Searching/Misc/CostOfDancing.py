'''
Keyword: TC, Topcoder ,SRM624, Sorting

Link:https://community.topcoder.com/stat?c=problem_statement&pm=13195

Problem Statement
    	
Gustavo studies at the Byteversity (one of the best universities in Byteland). He's also very keen on dancing, so he decided to enroll at a dance school.



The school offers many different courses, each teaching one dance. Different courses may have different costs. You are given a int[] danceCost. The elements of danceCost are the costs of all courses offered at the dance school.



Gustavo would like to learn exactly K of those dances. He is a poor student, so his only priority is to pay as little as possible for the courses.



You are given the int K and the int[] danceCost. Compute and return the smallest possible total cost of learning K dances.

 
Definition
    	
Class:	CostOfDancing
Method:	minimum
Parameters:	int, int[]
Returns:	int
Method signature:	int minimum(int K, int[] danceCost)
(be sure your method is public)
    
 
Constraints
-	danceCost will contain between 1 and 1,000 elements, inclusive.
-	Each element of danceCost will be between 1 and 1,000, inclusive.
-	K will be between 1 and the number of elements in danceCost, inclusive.
 
Examples
0)	
    	
2
{1, 5, 3, 4}
Returns: 4
Gustavo must pay for exactly two out of the four given courses. The cheapest possibility is to pay 1 for one course and then 3 for another course. The total cost is 1+3 = 4.
1)	
    	
3
{1, 5, 4}
Returns: 10
Gustavo has no choice here. He has to pay for all three courses, which costs 1+5+4 = 10.
2)	
    	
1
{2, 2, 4, 5, 3}
Returns: 2
Among all 5 possible courses he can take, the cheapest one is either the course #0 or course #1 (0-based).
3)	
    	
39
{973, 793, 722, 573, 521, 568, 845, 674, 595, 310, 284, 794, 913, 93, 129, 758, 108, 433, 181, 163, 96, 932,
 703, 989, 884, 420, 615, 991, 364, 657, 421, 336, 801, 142, 908, 321, 709, 752, 346, 656, 413, 629, 801}
Returns: 20431

'''


class CostOfDancing:
	def minimum(self,k,danceCost):
		return sum(sorted(danceCost)[:k])



t = CostOfDancing()
k = 39  	
danceCost = [973, 793, 722, 573, 521, 568, 845, 674, 595, 310, 284, 794, 913, 93, 129, 758, 108, 433, 181, 163, 96, 932, 703, 989, 884, 420, 615, 991, 364, 657, 421, 336, 801, 142, 908, 321, 709, 752, 346, 656, 413, 629, 801]


print t.minimum(k,danceCost)