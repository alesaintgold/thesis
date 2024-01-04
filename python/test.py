import sys
from permutasort.permutasort import *
from pattFinder.pattfinder import *

# allows to find out if the specified patterns cover all the permutations of lenght n
# that are not sortable by the specified sorting operator

if __name__ == '__main__':

	if len(sys.argv) < 4:
		print("ERROR; requested at least 3 arguments but got: " + str(sys.argv[1:]))
		exit()

	op = getOperator(sys.argv[1])
	n = int(sys.argv[2])
	av = sys.argv[3:]

	print("Generating permutations: ")
	unsortable = selectorPermutations(n,op).getUnsortable()
	result = unsortable
	print("\tfound " + str(len(unsortable)) + " unsortable permutations\n")
	
	print("Verifying "+str(len(av))+" patterns:\n")
	for p in av:
		print("Verifying pattern " + p+":")
		# from the list of unsortable premutations the ones containing the specified patterns get removed
		pattern  = [int(char) for char in p]
		contains_p = PatternAvoid(n, pattern).getContaining()
		result  = list(set(result).difference(set(contains_p)))
		print("\tfound "+str(len(set(contains_p).intersection(set(unsortable)))) + " matches\n")

	n_uns = len(result)
	if(n_uns==0):
		print("All unsortable permutations contains some of the specified patterns\n")
	else:
		print("These "+str(n_uns)+" permutations are not sorted by " + sys.argv[1]+" but not contain any specified pattern:")
		print(printlist(result))

