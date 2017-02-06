
class DoubleWeights:
	def minimalCost(self, w1, w2):
		w1 = list(w1); w2 = list(w2)
	
		for ind, i in enumerate(w1):
			i = map(lambda x : 0 if x=='.' else int(x),list(i))
			w1[ind] = i

		for ind, i in enumerate(w2):
			i = map(lambda x : 0 if x=='.' else int(x),list(i))
			w2[ind] = i

		key = [(100, 100)] * len(w1)

		queue = [i for i in range(len(w1)) ]

		key[0] = (0,0)

		while(queue):

			print queue

			n = self.find_min(key,queue, w1, w2)

			queue.remove(n)

			for ind, val in enumerate(w1[n]):
				
				if val <= 0 : continue
				
				a,b = key[ind]
				a = a + w1[n][ind] if a != 100 else w1[n][ind]
				b  = b+ w2[n][ind] if b != 100 else w2[n][ind]
				key[ind] = (a,b)
				print n, key



		print key
		return key[1][0] * key[1][1]

	def find_min(self, key, queue, w1, w2):
		min_val = 10000000000
		for ind, val in enumerate(key):
			
			if (val[0]* val[1] ) < min_val and ind in queue:
				min_ind = ind
				min_val = val[0]* val[1]

		return min_ind



d = DoubleWeights()
#w1 =[".....9","..9...",".9.9..","..9.9.","...9.9","9...9."]
#w2 = [".....9","..9...",".9.9..","..9.9.","...9.9","9...9."]

w1 = ["..14","..94","19..","44.."]
w2 = ["..94","..14","91..","44.."]


print d.minimalCost(w1, w2)
