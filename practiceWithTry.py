import math

#not an algorithm, just having fun
anumber = -12
try:
	print(math.sqrt(anumber))
except:
	print("Bad value for square root")
	print("Using absolute value instead")
	print(math.sqrt(abs(anumber)))