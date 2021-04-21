import array as arr
from random import shuffle
import random

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

