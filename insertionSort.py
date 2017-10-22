def insertionSort(myList):
   for i in range(1, len(myList)):
       j = i - 1
       while myList[j] > myList[j + 1] and j >= 0:
           myList[j], myList[j + 1] = myList[j + 1], myList[j]
           j -= 1

newList = [9,8,7,6,5,4,3,2,1]
insertionSort(newList)
print newList