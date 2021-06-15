# Input arr[] = {3, 4, 5, 1, 2}
# 1) Find middle point mid = (l + h)/2
# 2) If key is present at middle point, return mid.
# 3) Else If arr[l..mid] is sorted
#     a) If key to be searched lies in range from arr[l]
#        to arr[mid], recur for arr[l..mid].
#     b) Else recur for arr[mid+1..h]
# 4) Else (arr[mid+1..h] must be sorted)
#     a) If key to be searched lies in range from arr[mid+1]
#        to arr[h], recur for arr[mid+1..h].
#     b) Else recur for arr[l..mid] 


def binary_search(arr, l, h, key):

    if l > h:
        return -1
    
    mid = (l + h) // 2

    if arr[mid] == key:
        return mid
    
    # if arr[l...mid] is sorted
    if arr[l] < arr[mid]:
        if key >= arr[l] and key <= arr[mid]:
            return binary_search(arr, l, mid-1, key)
        return binary_search(arr, mid+1, h, key)
    # if arr[l...mid] is not sirted, meaning arr[mid...r] must be sorted
    if key >= arr[mid] and key <= arr[h]:
        return binary_search(arr, mid+1, h, key)
    return binary_search(arr, l, mid-1, key)


arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
n = len(arr)
key = 6
res = binary_search(arr, 0, n-1, key)

if res != -1:
    print("Index is: ", res)
else:
    print("Key not found")