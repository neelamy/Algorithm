'''
Keyword : TC, Topcoder, SRM479,Simple search, Iteration

Link: https://community.topcoder.com/stat?c=problem_statement&pm=11031

Problem Statement
    	John and Brus have their own airplane. They are going to take several consecutive flights. The i-th element of flights is the number of liters of fuel needed for the i-th flight. The flights can be performed only in the same order as they are described in flights. 



Initially there are fuel liters of fuel in the airplane. In order to perform a flight, the amount of fuel in the airplane must be at least as much as the amount of fuel needed for this flight. Return the maximum number of flights they will be able to make without a refuel.
 
Definition
    	
Class:	TheAirTripDivTwo
Method:	find
Parameters:	int[], int
Returns:	int
Method signature:	int find(int[] flights, int fuel)
(be sure your method is public)
    
 
Constraints
-	flights will contain between 1 and 47 elements, inclusive.
-	Each element of flights will be between 1 and 1000, inclusive.
-	fuel will be between 1 and 1000, inclusive.
 
Examples
0)	
    	
{1, 2, 3, 4, 5, 6, 7}
10
Returns: 4
Exactly 10 liters of fuel are required to perform the first four flights.
1)	
    	
{7, 6, 5, 4, 3, 2, 1}
10
Returns: 1
These are the same flights as in the previous example, but in different order.
2)	
    	
{1}
1000
Returns: 1
A single flight here.
3)	
    	
{8, 7, 7, 1, 5, 7, 9}
21
Returns: 2

'''

class TheAirTripDivTwo:
	def find(self,flights,fuel):
		for count,fuel_needed in enumerate(flights):
			if fuel >= fuel_needed:
				fuel = fuel - fuel_needed
			else:
				# If sufficient fuel is not available then return count ( actual value is count-1 but 
				# we are returning count+1 as count start from 0 and not 1
				return count

		# If fuel available for all flight then return count+1 as count starts from 0
		return count+1



t= TheAirTripDivTwo()
flights = [1, 2, 3, 4, 5, 6, 7]
fuel = 10

print t.find(flights,fuel)