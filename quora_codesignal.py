
# 1. threeCharsDistinct
# Given a string s, count the number of indices such that s[i], s[i+1] and s[i+2] are all distinct.


s = "abcdaaae"

def distinctThreeChars(str):

    total = 0

    if len(str) < 3:
        return total

    for x in range(2, len(s)):
        if str[x] != str[x-1] and str[x-1] != str[x-2] and str[x] != str[x-2]:
            total += 1

    return total

print('Distinct three chars:', distinctThreeChars(s))


# 2. brokenKeyboard
# Some of keys of your keyboard are broken so you can only type a limited set of chars. You are given the array of those chars and you are also given a string consisting of space separated words. You need to count how many words you can fully type.

keys = ['a', 'b', 'c', 'd', 'e', 'o', 'g', 'h', 's', 'p', 'i', 't', 'm', 'n', 'z', 'r']
words = ['dog', 'man', 'hospital', 'zebra', 'animal']

def possibleWords(keys, words):
    count = 0
    for word in words:
        possible = True
        for x in range(len(word)):
            if word[x] not in keys:
                possible = False
        if possible:
            count += 1
    return count

print('Pssible words:', possibleWords(keys, words))

# 3. bestRhombicAreaFrame
# Given an m x n matrix and a radius value, find the top 3 distinct rhombic frame areas (= sum of numbers on the frame) of that radius.

matrix = [ 
[1, 2, 3, 4, 5, 6],
[7, 8, 9, 10, 11, 12],
[13, 14, 15, 16, 17, 18],
[19, 20, 21, 22, 23, 24],
[25, 26, 27, 28, 29, 30 ]]

def rhombusArea(matrix, i, j, radius):
    if radius == 0:
        return matrix[i][j]

    sum = 0

    # Left corner
    row = i
    col = j - radius
    for x in range(0, radius + 1):
        sum += matrix[row][col]
        
        row -= 1
        col += 1

    # Top corner
    row = i - radius
    col = j
    for x in range(0, radius + 1):
        sum += matrix[row][col]
        
        row += 1
        col += 1

    # Right corner
    row = i
    col = j + radius
    for x in range(0, radius + 1):
        sum += matrix[row][col]
        
        row += 1
        col -= 1

    # Bottom corner
    row = i + radius
    col = j
    for x in range(0, radius + 1):
        sum += matrix[row][col]
        
        row -= 1
        col -= 1

    # Since corners get double counted
    sum -= matrix[i][j-1] + matrix[i-1][j] + matrix[i+1][j] + matrix[i][j+1]

    return sum

def top3RhombicFrameAreas(matrix, radius):
    radius -= 1
    listOfUniqueSums = []

    i = 0
    while i+2*radius < len(matrix):
        j = 0
        while j+2*radius < len(matrix[i]):
            sum = rhombusArea(matrix, i + radius, j + radius, radius)
            if sum not in listOfUniqueSums:
                listOfUniqueSums.append(sum)

            j += 1
        i += 1
    return listOfUniqueSums




print('Top three rhombic frames:', top3RhombicFrameAreas(matrix, 2))

# 4. arrayAdditionAndSum
# Given two integer arrays a and b and a list of queries of 2 type.

# You are given two arrays A, B and a list of queries - q. There are two types of queries - type 1: (1,i,x) where you set B[i] = x and type 2: (0, x) where you must calculate all pairs in A, B such that a[i] + b[j] == x. You must return a list of length equal to the number of type 2 queries. Keep in mind that after a type 1 query your B is now different.
# example: A = [1,2], B = [3,4,5]. If the first query is (0, 5) you want to append the number 2 to your answer array because 1 + 4 = 5 and 2 + 3 = 5. (This is just the first query and there may be many more)

A = [1, 2]
B = [3, 4, 5]
queries = [
    [0,5],
    [1, 1, 5],
    [0, 6],
    [1, 2, 4]]

def executeQueries(A, B, queries):
    result = []

    for q in queries:
        if q[0] == 1:
            i = q[1]
            x = q[2]
            B[i] = x
        elif q[0] == 0 and len(A) < len(B):
            result.append(countPairs(A, B, q[1]))
        else:
            result.append(countPairs(B, A, q[1]))

    return result

def countPairs(A, B, x):
    count = 0
    for e in A:
        if (x-e) in B:
            count += 1
    return count
    
print('Queries executed:', executeQueries(A, B, queries))
