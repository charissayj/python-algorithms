def bubbleSort(myList):
    #outer for loop
    for i in range (0, len(myList) -1):
        #inner loop
        for j in range(0, len(myList) - 1 - i):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
    return myList
    
theList = [2, 5, 2, 3, 1, 6 ,7, 9, 1]
print bubbleSort(theList)