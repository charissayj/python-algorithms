# Write a function that takes in a list and a value, 
# and adds the value to the front of that list, 
# outputting the changed list. 
# This should be done in place 
# This means you should not create a new list, 
# but change the existing one. 

def push_front(arr, val):
    arr.insert(0,val)
    
    print arr
    
push_front([1,3,5], 7)