import sys
from permutasort.permutasort import *
from pattFinder.pattfinder import *

# allows to find out if the specified patterns cover all the permutations of lenght n
# that are not sortable by the specified sorting operator

if len(sys.argv) < 4:
	print("ERROR; requested at least 3 arguments but got: " + str(sys.argv[1:]))
	exit()

op = getOperator(sys.argv[1])
n = int(sys.argv[2])
av = sys.argv[3:]

print("Generating unsortable permutations")
unsortable = selectorPermutations(n,op).getUnsortable()

print("Verifying "+str(len(av))+" patterns")
for p in av:
	print("Verifying pattern " + p)
	# from the list of unsortable premutations the ones containing the specified patterns get removed
	pattern  = [int(char) for char in p]
	contains_p = PatternAvoid(n, pattern).getContaining()
	unsortable = list(set(unsortable).difference(set(contains_p)))

if(len(unsortable)==0):
	print("\nAll unsortable permutations contains some of the specified patterns\n")
else:
	print("\nThese permutations are not sorted by " + sys.argv[1]+" and not contain any specified pattern:")
	for x in unsortable:
		print(str(x))
	print("\n")
