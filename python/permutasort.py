import sys
from itertools import permutations

from src.operators import *
from src.utils import *

class selectorPermutations:
	def __init__(self,num,op):
		if num <=0:
			print("ERROR: was expecting a positive integer but got "  +str(num))
			exit()

		# initialization of lists
		self.__sortable = []
		self.__unsortable = []
		self.__outcomes = []

		# generation of permutations
		permutations_list = list(permutations(range(1,num+1)))
		
		for P in permutations_list:

			# applying the operator to the permutation
			op_P_ = op(P)
			
			# adding outcome to the list
			if op_P_ not in self.__outcomes:
				self.__outcomes.append(op_P_)
			
			# adding permutations to the right list
			if isIdentityPermutation(op_P_):
				self.__sortable.append(P)
			else:
				self.__unsortable.append(P)
		
	def getSortable(self):
		return self.__sortable

	def getUnsortable(self):
		return self.__unsortable

	def getOutcomes(self):
		return self.__outcomes

# more lines present in the original file  are omitted 
# from this one due to excessive lenght since it's not of our 
# interest to show further in the thesis