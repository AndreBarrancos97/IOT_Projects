
#If elif else example
value = 10
x = 10
if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
	print('It is Zero')
elif x == 1:
	print('It is One')
else:
	print('It is More than one')


#for range example
for i in range(1, 10, 2):
    print(i)

# Count the letters in some strings:
words = ['car', 'skate', 'bicycle']
for w in words:
	print(w, len(w))


# Create a new Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
	
# Can build up a dict by starting with the the empty dict {}
# and storing key/value pairs into the dict like this:
# dict[key] = value-for-that-key
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print (dict)  # {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print (dict['a'])     # Simple lookup, returns 'alpha'
dict['a'] = 6       # Put new key/value into dict
'a' in dict         # True
# print dict['z']                  # Throws KeyError
if 'z' in dict: print (dict['z'] )    # Avoid KeyError
print (dict.get('z'))  # None (instead of KeyError)

# By default, iterating over a dict iterates over its keys.
# Note that the keys are in a random order.
for key in dict: print (key)
# prints a g o
  
# Exactly the same as above
for key in dict.keys(): print (key)
for aux in dict.values(): print(aux)
# Get the .keys() list:
print (dict.keys() ) # ['a', 'o', 'g']

# Likewise, there's a .values() list of values
print (dict.values())  # ['alpha', 'omega', 'gamma']

# Common case -- loop over the keys in sorted order,
# accessing each key/value
for key in sorted(dict.keys()):
	print (key, dict[key])
  
# .items() is the dict expressed as (key, value) tuples
print (dict.items() )  # [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

# This loop syntax accesses the whole dict by looping
# over the .items() tuple list, accessing one (key, value)
# pair on each iteration.
for k, v in dict.items(): print (k, '>', v)
# a > alpha    o > omega     g > gamma


def fib(n):    # write Fibonacci series up to n
	a, b = 0, 1
	while a < n:
		#print(a, end=' ',"\n")
		print(a, "\n")
		a, b = b, a+b
	print(a,' e ',b,'\n')

fib (2)
#numpy array creation with elements
import numpy as np
a = np.arange(15).reshape(3, 5)

#array([[ 0,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9],
#       [10, 11, 12, 13, 14]])
