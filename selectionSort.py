def selectionSort(alist):
    for i in range (0, len(alist) -1):
        minIndex = i 
        for j in range (i + 1, len(alist)):
            if alist[j] < alist[minIndex]:
                minIndex = j 
            if minIndex != i:
                alist[i], alist[minIndex] = alist[minIndex], alist[i]
                

myList = [1,3,5,2,3,7,4,8]
selectionSort(myList)
print myList