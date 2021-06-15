
def insertionSort(arr, n):

    for i in range(1, n):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        print('i', i)
        while j >= 0 and key < arr[j]:
            print(" j", j)
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key




arr = [12, 11, 13, 5, 6]
n = len(arr)
insertionSort(arr, n)
for i in range(n):
    print(arr[i], end= " ")