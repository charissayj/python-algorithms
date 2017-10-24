#Create a function that accepts a number as an input. 
#Return a new array that counts down by one, 
#from the number(as the zeroth element) down to 0.
#Print array length

def countdown(num):
	nums = []
	for element in reversed(range(num + 1)):
	    nums.append(element)
	print nums

countdown(7)