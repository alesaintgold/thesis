class PatternAvoid():
	def __init__(self,n, pattern):
		if n <= 1:
			print("ERROR: expecting a whole number greater than 1 but got: " + str(n))
			exit()
		
		self.__n = n

		# checking if the argument really is a classical pattern
		pattern_list = [int(p) for p in pattern]
		if len(pattern) != max(pattern_list):
			print("ERROR: expected a pattern but got: " + str(pattern))
			exit()
		for i in range(1, len(pattern)):
			if i not in pattern_list:
				print("ERROR: expected a pattern but got: " + str(pattern))
				print("\nA pattern of lenght n must have all the numbers from 1 to n, " + str(i) + " not present")
				exit()

		# generating permutations
		permutations_list = list(permutations(range(1,n+1)))

		# declaring list fields
		self.__notcontaining = []
		self.__containing = []

		for p in permutations_list:
			if not self.contains(p,pattern):
				self.__notcontaining.append(p)
			else:
				self.__containing.append(p)

	# get the standard image of the number sequence:
	def patternize(self,pi):
		output = []
		id_ = sorted(pi)
		for p in pi:
			output.append(id_.index(p)+1)
		return output

	# check if a seqence contains the given pattern
	def contains(self, seq, pattern):
		if len(seq) < len(pattern):
			return False
		subseq = combinations(seq, len(pattern))
		for s in subseq:
			if list(self.patternize(s)) == list(pattern):
				return True
		return False

	def getNotContaining(self):
		return self.__notcontaining

	def getContaining(self):
		return self.__containing
