str1 = 'hello'
str2 = 'world'

# No. of letters in the Alphabet
maxChars = 26


def smallestCommonSubstring(str1, str2):
    
    v = [0] * maxChars

    for i in range(len(str1)):
        v[ord(str1[i]) - ord('a')] = True

    for i in range(len(str2)):
        if ( v[ ord(str2[i]) - ord('a') ]):
            return True

    return False

if smallestCommonSubstring(str1, str2):
    print('Yes')
else:
    print('No')