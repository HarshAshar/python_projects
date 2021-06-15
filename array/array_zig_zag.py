
def zigZag(arr, n):
    
    if len(arr) <= 1:
        print(arr)
        return
    # Flag true indicates relation "<" is expected,
    # else ">" is expected.
    # The first expected relation is "<"
    flag = True
    for i in range(0, n-1):
        if flag is True:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        
        flag = bool(1-flag)

    print(arr)

arr = [4, 3, 7, 8, 6, 2, 1]
n = len(arr)
zigZag(arr, n)