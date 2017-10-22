def mergeSort(newList):
    mergeSort2(newList, 0, len(newList) - 1)
    
def mergeSort2(newList, first, last):
    if first < last:
        middle = (first + last)//2 
        mergeSort2(newList, first, middle)
        mergeSort2(newList, middle + 1, last)
        merge(newList, first, middle, last)
    
def merge(newList, first, middle, last):
    left = newList[first:middle]
    right = newList[middle: last + 1]
    left.append(999999999)
    right.append(999999999)
    i = j = 0
    for k in range(first, last + 1):
        if left[i] <= right[j]:
            newList[k] = left[i]
            i += 1
        else:
            newList[k] = right[j]
            j += 1
    
    
newList = [5,9,1,2,4,8,6,3,7]
print newList
mergeSort(newList)

print newList