# Given an array of distinct integers and a sum value. Find count of triplets with sum smaller than given sum value. Expected Time Complexity is O(n2).
# https://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/

def countTriplets(arr, n, sum):
    
    ans = 0

    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] < sum:
                    ans += 1

    return ans



arr = [5, 1, 3, 4, 7]
n = len(arr)
sum = 12
print(countTriplets(arr, n, sum))
