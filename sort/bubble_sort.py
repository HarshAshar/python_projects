
def bubbleSort(arr, n):
    
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped is False:
            break


arr = [90, 64, 34, 25, 12, 22, 11]
n = len(arr)
bubbleSort(arr, n)
print("Sorted array is: ")
for i in range(n):
    print(arr[i], end=" ")