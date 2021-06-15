#Approach 1
# brute force
# Check all the substring one by one to see if it has no duplicate character.

def lengthOfLongestSubscring(str):
    
    n = len(str)
    res = 0
    
    for i in range(n):
        for j in range(i, n):
            if checkUnique(str, i, j):
                res = max(res, j-i+1)

    return res

def checkUnique(s, start, end):

    chars = [0] * 128
    for i in range(start, end + 1):
        c = s[i]
        if chars[ord(c)] == 1:
            return False
        else:
            chars[ord(c)] += 1
    return True


str = 'abcabcbb'
print('lengthOfLongestSubscring', lengthOfLongestSubscring(str))

# Approach 2
# Sliding Window

def lengthOfLongestSubscring_slidingWindow(str):

    chars = [0] * 128
    left = right = 0
    res = 0

    while right < len(str):
        r = str[right]
        chars[ord(r)] += 1

        while chars[ord(r)] > 1:
            l = str[left]
            chars[ord(l)] -= 1
            left += 1

        res = max(res, right - left + 1)

        right += 1
    return res

print('lengthOfLongestSubscring_slidingWindow', lengthOfLongestSubscring_slidingWindow(str))

# Approach 3
# Sliding window optimized

def lengthOfLongestSubscring_slidingWindow_optimized(str):
    
    n = len(str)
    res = 0
    # mp stores the current index of a character
    mp = {}

    i = 0
    for j in range(n):
        if str[j] in mp:
            i = max(i, mp[str[j]])

        res = max(res, j-i+1)
        mp[str[j]] = j+1
    
    return res

print('lengthOfLongestSubscring_slidingWindow_optimized', lengthOfLongestSubscring_slidingWindow_optimized(str))