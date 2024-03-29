def mergeSort(arr):
    # no sorting needed for array with single element
    if len(arr) > 1:
        # find the middle floor index
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # for the remaining indices
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print("Sorted array is: ", end="\n")
printList(arr)