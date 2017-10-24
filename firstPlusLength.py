# Given an array, return the sum of the first value in the array, 
# plus the array's length.
# Test for cases where the first value is not an integer

def firstPlusLength(arr):
    if isinstance(arr[0], int):
        sum = arr[0] - len(arr) - 1
        print sum
    else:
        print "First array value is not a number"
        
firstPlusLength([1,2,4])
firstPlusLength(['a',2,3])