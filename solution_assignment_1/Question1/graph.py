# =============================================================================
# Author: Azizou Ogbone
# File: graph.py
# Description: A program to produce text based graph of a one-variable function
# Date: March 28, 2017
# Version: 1.0
# =============================================================================

from math import * # to plot other function, that uses function defined in the 
# math library directly

def get_graph(axis_length,fx):
	""" A function to produce a text based graph of the one variable functon fx of x
		axis_length: represent the size of the grid the plot will be on.
		fx: the function to be plotted. This must be s function of x.

		result: A string representation of the final grid including o's for the graph/curve of fx
	"""
	result = ""
	for y in range(axis_length//2, -(axis_length//2+1),-1):
		for x in range(-axis_length//2, axis_length//2+1):
			if eval(fx)==y:
				result += 'o'
			else:
				if x == 0: #Horizontal_line
					if y== 0: #Origin
						result += '+'
					else:
						result += '|'
				else:
					if y== 0:#Vertical_line
						result += '-'
					else:
						result += ' '
		result += "\n"	#New row, nouvelle ligne
	return result

def main():
	# Get input values from the user
	#The function of x:
	fx = input("Enter a function fx: (e.g. 3*x+1)")

	#Default grid size
	grid_size = 20

	#Get the graph as a string
	graph = get_graph(grid_size, fx)

	#Print it
	print(graph)

#Only execute if the file was executed directly and 
# not imported into other programs
if __name__ == '__main__':
	main()