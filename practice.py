import array as arr
from random import shuffle
import random
import functools

my_array = arr.array('i', [1,2,3,4,5])

# Reverse an array
print(my_array[::-1])

list1 = [1,2,3,4]
list2 = ['hello', 'my', 'name', 'is']

# Reverse a list
print(list(reversed(list1)))
print(list(reversed(list2)))

# Randomize a list or array
shuffle(list2)
print(list2)

# generate random numbers in float between 0 & 1
print(random.random())

# loop through a range (start, stop, step)
x = range(25, 35, 3)

for n in x:
    print(n)

# To upper case or lower case
string1 = 'abcd'
string2 = 'XYZ'

print(string1.upper())
print(string2.lower())

# Capitalize the first letter of a string

name = 'marina'
print(name.capitalize())

# define a dict

dict = {'Country': 'India', 'Capital': 'New Delhi'}

print(dict['Country'])
print(dict['Capital'])

# find the length
print(len(name))

#Reduce

print("Reduce : ")

def add(x, y):
    print(x, y)
    return x+y

print(functools.reduce(add, range(1, 5)))

print("Reduce end.")

def even(k):
    for i in range(k):
        if i % 2 != 0:
            yield i

print(even(20))

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

print("check for palindrome")

def palindrome(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        print(s[:i], s[i+1:])
        if t == t[::-1]: return True
    return s == s[::-1]
    
palindrome("radkar")

#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of the non-zero elements.

print("moveZeroes")

array1 = [0, 1, 0, 3, 12]

def moveZeroes(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums

print(moveZeroes(array1))

#Given two sentences, return an array that has the words that appear in one sentence and not the other and an array with the words in common. 

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def solution(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())

    return sorted(list(set1^set2)), sorted(list(set1&set2))

print(solution(sentence1, sentence2))

# 