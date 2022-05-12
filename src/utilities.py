version = "0.7"
DEBUG = False
GRAPH = False
from random import randint
if GRAPH: import matplotlib.pyplot as plt


if DEBUG:
	def makeTest(length,low,high):
		return [randint(low,high) for i in range(length)]

def is_sorted(iterable:list):
	"""
	Checks if a list is sorted.
	
	# Attributes
	
	iterable: `list`
	The object to iterate through.
	"""
	sorted = True
	for i in range(len(iterable)):
			if i < len(iterable)-1 and iterable[i] > iterable[i+1]:
			  sorted = False; break
	return sorted
	
	
def bubbleSort(iterable:list):
	"""
	Represents a bubble sort.
	
	This is best used on smaller iterables, and when the iterable is almost sorted already.
	
	# Attributes
	
	iterable: `list`
	The object to iterate through.
	"""
	while not is_sorted(iterable):
		for j in range(len(iterable) - 1):
			if iterable[j] > iterable[j+1]:
				if DEBUG:
					print("Bubbling "+str(j))
				iterable[j+1], iterable[j] = iterable[j], iterable[j+1]
	return iterable
	
	
def insertionSort(iterable:list):
	"""
	Represents an insertion sort.
	
	This is very efficient on small iterables, and is stable and quite fast when the iterable is nearly sorted.
	
	# Attributes
	
	iterable: `list`
	The object to iterate through.
	"""
	if not is_sorted(iterable):
		for i in range(1, len(iterable)):
			if DEBUG: print("Insertion index "+str(i)+" / "+str(len(iterable)))
			key = iterable[i]
			j = i-1
			while j >=0 and key < iterable[j]:
				if DEBUG:
					print("Finding place in sorted half")
				if GRAPH:
					plt.plot(iterable)
					plt.xlabel("Position in array")
					plt.ylabel("Value of number in position")
					plt.draw()
					plt.pause(0.0001)
					plt.clf()
				iterable[j+1] = iterable[j]
				j -= 1
				iterable[j+1] = key
	return iterable
	
	
def mergeSort(iterable:list, zero:int, iterable_length_minus_one:int):
	"""
	Represents a merge sort.
	
	# Attributes
	
	iterable: `list`
	The object to iterate through.
	
	zero: `int`
	Always pass 0 into the merge sort.
	
	iterable_length_minus_one: `int`
	Pass the length of the iterable minus 1 into the merge sort.
	"""
	def merge(arr, l, m, r):
		n1 = m - l + 1
		n2 = r - m
		L = [0] * (n1)
		R = [0] * (n2)
		for i in range(0, n1):
			L[i] = arr[l + i]
		for j in range(0, n2):
			R[j] = arr[m + 1 + j]
		i = 0
		j = 0
		k = l
		while i < n1 and j < n2:
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		while i < n1:
			arr[k] = L[i]
			i += 1
			k += 1
		while j < n2:
			arr[k] = R[j]
			j += 1
			k += 1
	def sort(arr, l, r):
		if l < r:
			m = l+(r-l)//2
			sort(arr, l, m)
			sort(arr, m+1, r)
			merge(arr, l, m, r)
			if GRAPH:
				plt.plot(iterable)
				plt.xlabel("Position in array")
				plt.ylabel("Value of number in position")
				plt.draw()
				plt.pause(0.0001)
				plt.clf()
		return arr
	if is_sorted(iterable):
		return iterable
	else:
		return sort(iterable, zero, length_minus_one)

	
def linearSearch(iterable:list, item):
	"""
	Checks if an item is in a list, by stepping through one item at a time and checking each item.
	
	# Attributes
	
	iterable: `list`
	The object to iterate through.
	
	item: `Any`
	The item to check for during the search.
	"""
	found = False
	for i in iterable:
		if i == item: found = True; break
	return found
	
	
def binarySearch(iterable:list, item):
	"""
	Checks if an item is in a list, by halving the list recursively until it narrows down to two items and then checks if the desired item is one of the two items remaining.
	
	# Attributes
	
	iterable: `list`
	The object to iterate through.
	
	item: `Any`
	The item to check for during the search.
	"""
	def binary(iterable, item):
		if DEBUG: print("Starting search")
		if len(iterable) > 2:
			m = len(iterable)//2
			if DEBUG: print("Middle index: "+str(m))
			if iterable[m] > item:
				return binary(iterable[:m],item)
			else:
				return binary(iterable[m:],item)
		else:
			if item in iterable: return True
			else: return False
	if not is_sorted(iterable):
		iterable = mergeSort(iterable, 0, len(iterable)-1)
		if DEBUG: print("Sorted binary list")
	return binary(iterable, item)

	
def largest(iterable:list):
	"""
	Calculates the largest number in the list.
	
	# Attributes
	
	iterable: `list`
	The list to iterate through.
	"""
	largest = 0
	for n in iterable:
		if n > largest: largest = n
	return largest
	
	
def smallest(iterable:list):
	"""
	Calculates the smallest number in the list.
	
	# Attributes
	
	iterable: `list`
	The list to iterate through.
	"""
	smallest = 0
	for n in iterable:
		if n < smallest: smallest = n
	return smallest
	
	
def evens(iterable:list):
	"""
	Finds all the even numbers in a list.
	
	# Attributes
	
	iterable: `list`
	The list to iterate through.
	"""
	return [n for n in iterable if n % 2 == 0]
	
	
def odds(iterable:list):
	"""
	Finds all the odd numbers in a list.
	
	# Attributes
	
	iterable: `list`
	The list to iterate through.
	"""
	return [n for n in iterable if n % 2 != 0]
	
	
def divisible(iterable:list, divider:int):
	"""
	Finds all the numbers in a list that are divisible by the number passed.
	
	# Attributes
	
	iterable: `list`
	The list to iterate through.
	
	divider: `int`
	The number to check if divisible by.
	"""
	return [n for n in iterable if n % divider == 0]
	
	
def not_divisible(iterable:list, divider:int):
	"""
	Finds all the numbers in a list that are not divisible by the number passed.
	
	# Attributes
	
	iterable: `list`
	The list to iterate through.
	
	divider: `int`
	The number to check if not divisible by.
	"""
	return [n for n in iterable if n % divider != 0]

def list2dict(iterable:list):
	"""
	Converts a list to a dictionary.

	The item and value should be passed as [i, v] as items in the list, for example `[[1,2], [3,4]]` where this would be converted to `{1:2, 3:4}`.

	# Attributes

	iterable: `list`
		The list to convert.
	"""
	return {i[0]:i[1] for i in iterable}

def list2tuple(iterable:list):
	"""
	Converts a list to a tuple.

	Items inside the list are also converted to tuples if they are a list.

	# Attributes

	iterable: `list`
		The list to convert.
	"""
	if type(iterable) != list: return iterable
	return tuple(list2tuple(i) for i in iterable)


def tuple2list(iterable:tuple):
	"""
	Converts a tuple to a list.

	Items inside the tuple are also converted to lists if they are a tuple.

	# Attributes

	iterable: `tuple`
		The tuple to convert.
	"""
	if type(iterable) != tuple: return iterable
	return list(tuple2list(i) for i in iterable)
	

def dict2list(dictionary:dict):
	"""
	Converts a dictionary to a list.

	The list is sorted based on the dictionary keys/items.

	# Attributes

	dictionary: `dict`
		The dictionary to convert.
	"""
	return [[i,dictionary[i]] for i in [x for x in insertionSort([i[0] for i in list(dictionary.items())])]]