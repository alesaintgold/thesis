import sys
import tkinter as tk
import itertools

from src.operators import *

class selectorPermutations:
	def __init__(self,num,op):
		self.sortable = []
		self.unsortable = []
		self.possible_outcomes = []

		if num <=0:
			print("ERROR: was expecting a positive integer but got "  +str(num))
		else:
			perms = list(itertools.permutations(range(1,num+1)))
			for P in perms:
				sorted_P = op(P)
				#adding outcome to the list
				if sorted_P not in self.possible_outcomes:
						self.possible_outcomes.append(sorted_P)
				#adding permutations to the right list
				if sorted_P == sorted(P):
					self.sortable.append(P)
				else:
					self.unsortable.append(P)

	def sortable_permutations(self):
		return self.sortable

	def unsortable_permutations(self):
		return self.unsortable

	def outcomes(self):
		return self.possible_outcomes

def printlist(list):
	result = ""
	for item in list:
		result = result +(str(item) + "\n")
	return result


if __name__ == '__main__':
	
	narg = len(sys.argv)
	
	if narg not in (1,3):
		print("ERROR: expected 2 arguments or none, but got: " + str(sys.argv[1:]))
		exit()

	elif narg == 3:
		# command line
		n = sys.argv[1]
		op = sys.argv[2]

		ps = selectorPermutations(int(n), getOperator(op))

		sortable = ps.sortable_permutations()
		unsortable = ps.unsortable_permutations()
		outcomes = ps.outcomes()

		sortable_str = "The following " + str(len(sortable)) +" "+str(n)+"-permutations are sortable with the operator "+op+":\n" + printlist(sortable)
		unsortable_str = "The following " + str(len(unsortable)) +" "+str(n)+"-permutations are not sortable with the operator "+op+":\n" + printlist(unsortable)
		outcomes_str = "The operator "+op+" can give the following "+ str(len(outcomes))+" results when applied to " + str(n) + "-permutations:\n" + printlist(outcomes)

		print('\n'+sortable_str)
		print(unsortable_str)
		print(outcomes_str)

		file_sortable = open("./log/"+n+op+"sortable.txt", "w")
		file_sortable.write(str(sortable_str) + "\n")
		file_sortable.close()

		file_unsortable = open( "./log/"+n+op+"unsortable.txt","w")
		file_unsortable.write(str(unsortable_str) + "\n")
		file_unsortable.close()

		file_outcome = open("./log/"+n+op+"outcome.txt","w")
		file_outcome.write(str(outcomes_str) + "\n")
		file_outcome.close()
	else:
		#gui
		PermutaSortGUI()

class PermutaSortGUI:
	def __init__(self):
		self.window = tk.Tk(	)
		self.window.geometry("300x200")

		label1 = tk.Label(text="Selecting which n-permutations\nare sortable or unsortable for the\nspecified sorting operator")
		label1.pack()

		n_frame = tk.Frame()
		n_label = tk.Label(master = n_frame, text = "\nn = ") 
		n_label.pack()
		self.n_box = tk.Entry(master = n_frame, width = 10)
		self.n_box.pack()
		n_frame.pack()

		o_frame = tk.Frame()
		o_label = tk.Label(master = o_frame, text = "operator: ")
		o_label.pack()
		self.o_box = tk.Entry(master=o_frame, width = 10)
		self.o_box.pack()
		o_frame.pack()

		button = tk.Button(text = "Calculate", width = 25, command = self.calculate)
		button.pack()

		self.window.mainloop()

	def calculate(self):
		n = self.n_box.get()
		op = self.o_box.get()

		ps = selectorPermutations(int(n), getOperator(op))

		sortable = ps.sortable_permutations()
		unsortable = ps.unsortable_permutations()
		outcomes = ps.outcomes()

		self.displayList(sortable, "The " +n+"-permutations sortable by "+op+" are the following "+str(len(sortable))+":")
		self.displayList(unsortable, "The " +n+"-permutations not sortable by "+op+" are the following "+str(len(unsortable))+":")
		self.displayList(outcomes, "Applying "+op+" to " + n + "-permutations can generate the following outcomes:")

		file_sortable = open("./log/"+n+op+"sortable.txt", "w")
		file_sortable.write(str(sortable_str) + "\n")
		file_sortable.close()

		file_unsortable = open( "./log/"+n+op+"unsortable.txt","w")
		file_unsortable.write(str(unsortable_str) + "\n")
		file_unsortable.close()

		file_outcome = open("./log/"+n+op+"outcome.txt","w")
		file_outcome.write(str(outcomes_str) + "\n")
		file_outcome.close()

	def displayList(self, list, message):
		new_window = tk.Toplevel(self.window)

		label = tk.Label(new_window, text=message + "\n")
		label.pack()
		str_list = tk.Label(new_window, text=printlist(list))
		str_list.pack()

		new_window.grab_set()

