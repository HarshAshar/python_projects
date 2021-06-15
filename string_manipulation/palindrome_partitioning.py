

def isPalindrome(x):
    return x == x[::-1]

def minPalPartition(string, i, j):
    if i >= j or isPalindrome(string[i:j+1]):
        return 0
    ans = float('inf')
    for k in range(i, j):
        count = 1 + minPalPartition(string, i, k) + minPalPartition(string, k + 1, j)
        ans = min(ans, count)
    return ans

string = 'ababbbabbababa'
string2 = 'abacd'

print("Min cuts needed for palindrome partitioning is ", minPalPartition(string, 0, len(string)-1))
