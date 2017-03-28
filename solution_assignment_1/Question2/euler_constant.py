# =============================================================================
# Author: Azizou Ogbone
# File: euler_constant.py
# Description: A program to compute the euler's constant 
# Date: March 28, 2017
# Version: 1.0
# =============================================================================

import math

def compute_e():
	current_e = 0
	old_e = -1 #Dummy value for sentinel that's different from result
	n = 0
	while old_e!= current_e:
		old_e = current_e
		current_e += 1/math.factorial(n)
		n += 1
	return n, current_e

if __name__ == '__main__':
	n, e = compute_e()
	print("{0:.11f}".format(e)) #11 decimal places
