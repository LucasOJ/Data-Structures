#QUICKSORT

def partition(arr, lower, upper):
    i = lower
    pivot = arr[lower]
    for j in range(lower, upper):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    pivotIndex = i -1
    arr[lower], arr[pivotIndex] = arr[pivotIndex], arr[lower]

    return pivotIndex

def split(arr, lower, upper):
    if lower + 1 < upper:
       
        pivotIndex = partition(arr, lower, upper)
        split(arr, lower, pivotIndex)
        split(arr, pivotIndex + 1, upper)

    return arr

def quicksort(arr):
    return split(arr, 0, len(arr))

print(quicksort([56,4,2,35,53,6,2,3,768,3]))

#MERGESORT

def merge(arr1, arr2):
    mergedArr = []
    arr1Lenth, arr2Length = len(arr1), len(arr2)
    arr1Index, arr2Index = 0, 0
    while arr1Index < arr1Lenth and arr2Index < arr2Length:
        nextArr1, nextArr2 = arr1[arr1Index], arr2[arr2Index]
        if nextArr1 <= nextArr2: 
            mergedArr.append(nextArr1)
            arr1Index += 1
        else: 
            mergedArr.append(nextArr2)
            arr2Index += 1

    mergedArr.extend(arr1[arr1Index:])
    mergedArr.extend(arr2[arr2Index:])

    return mergedArr

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    splitIndex = len(arr) // 2
    leftArr = mergesort(arr[:splitIndex])
    rightArr = mergesort(arr[splitIndex:])
    return merge(leftArr, rightArr)

print(mergesort([56,4,2,35,53,6,2,3,768,3]))
