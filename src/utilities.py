version = "1.0"
DEBUG = False
GRAPH = False
from random import randint
import time
import matplotlib.pyplot as plt
import math


if DEBUG:
	def makeTest(length,low,high,timer=False):
		t = Timer()
		r = [randint(low,high) for i in range(length)]
		t.stop()
		if timer or DEBUG: return t.return_result(r)
		else: return r

class Timer():
	def __init__(self):
		self.start()

	def start(self):
		self.time1 = time.time()

	def stop(self, decimal_places=None):
		self.time2 = time.time()
		self.result = self.time2 - self.time1 if decimal_places is None else round(self.time2 - self.time1, decimal_places)
		return self.result

	def return_result(self, result):
		return result, self.result

def is_sorted(iterable:list, timer=False):
	"""
	Checks if a list is sorted.
	
	# Attributes
	
	iterable: `list`
	The object to iterate through.
	"""
	sorted = True
	t = Timer()
	for i in range(len(iterable)):
		if i < len(iterable)-1 and iterable[i] > iterable[i+1]:
		  sorted = False; break
	t.stop()
	if timer or DEBUG: return t.return_result(sorted)[0]
	else: return sorted
	
	
def bubbleSort(iterable:list, timer=False):
	"""
	Represents a bubble sort.
	
	This is best used on smaller iterables, and when the iterable is almost sorted already.
	
	# Attributes
	
	iterable: `list`
	The object to iterate through.
	"""
	t = Timer()
	while not is_sorted(iterable):
		for j in range(len(iterable) - 1):
			if iterable[j] > iterable[j+1]:
				if DEBUG: print("Swapping "+str([iterable[j],iterable[j+1]]))
				iterable[j+1], iterable[j] = iterable[j], iterable[j+1]
			if GRAPH: #note: i have experimented with using a bar chart, however i found that a line graph looks a lot better
				plt.plot(iterable)
				plt.xlabel("Position in array")
				plt.ylabel("Value of number in position")
				plt.draw()
				plt.pause(0.0001)
				plt.clf()
	t.stop()
	if timer or DEBUG: return t.return_result(iterable)
	return iterable

	
def insertionSort(iterable:list, timer=False):
	"""
	Represents an insertion sort.
	
	This is very efficient on small iterables, and is stable and quite fast when the iterable is nearly sorted.
	
	# Attributes
	
	iterable: `list`
	The object to iterate through.
	"""
	t = Timer()
	while not is_sorted(iterable):
		for i in range(1, len(iterable)):
			if DEBUG: print("Insertion index "+str(i)+" / "+str(len(iterable)))
			key = iterable[i]
			j = i-1
			while j >=0 and key < iterable[j]:
				if DEBUG:
					print("Finding place in sorted half")
				iterable[j+1] = iterable[j]
				j -= 1
				iterable[j+1] = key
			if GRAPH:
				plt.plot(iterable)
				plt.xlabel("Position in array")
				plt.ylabel("Value of number in position")
				plt.draw()
				plt.pause(0.0001)
				plt.clf()
	t.stop()
	if timer or DEBUG: return t.return_result(iterable)
	else: return iterable

	
def mergeSort(iterable:list, timer=False):
	"""
	Represents a merge sort.
	
	# Attributes
	
	iterable: `list`
	The object to iterate through.sort.
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
	t = Timer()
	while not is_sorted(iterable):
		if is_sorted(iterable): break
		else:
			sort(iterable, 0, len(iterable)-1)
	t.stop()
	if timer or DEBUG: return t.return_result(iterable)
	else: return iterable

	
def linearSearch(iterable:list, item, timer=False):
	"""
	Checks if an item is in a list, by stepping through one item at a time and checking each item.
	
	# Attributes
	
	iterable: `list`
	The object to iterate through.
	
	item: `Any`
	The item to check for during the search.
	"""
	found = False
	t = Timer()
	for i in iterable:
		if i == item: found = True; break
	t.stop()
	if timer or DEBUG: return t.return_result(found)
	else: found
	

def binarySearch(iterable:list, item, timer=False):
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
	t = Timer()
	if not is_sorted(iterable):
		iterable = mergeSort(iterable, 0, len(iterable)-1)
		if DEBUG: print("Sorted binary list")
	r = binary(iterable, item)
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r

	
def largest(iterable:list, timer=False):
	"""
	Calculates the largest number in the list.
	
	# Attributes
	
	iterable: `list`
	The list to iterate through.
	"""
	largest = 0
	t = Timer()
	for n in iterable:
		if n > largest: largest = n
	t.stop()
	if timer or DEBUG: return t.return_result(largest)
	else: return largest
	
	
def smallest(iterable:list, timer=False):
	"""
	Calculates the smallest number in the list.
	
	# Attributes
	
	iterable: `list`
	The list to iterate through.
	"""
	smallest = 0
	t = Timer()
	for n in iterable:
		if n < smallest: smallest = n
	t.stop()
	if timer or DEBUG: return t.return_result(smallest)
	else: return smallest
	
	
def evens(iterable:list, timer=False):
	"""
	Finds all the even numbers in a list.
	
	# Attributes
	
	iterable: `list`
	The list to iterate through.
	"""
	t = Timer()
	r = [n for n in iterable if n % 2 == 0]
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r
	
	
def odds(iterable:list, timer=False):
	"""
	Finds all the odd numbers in a list.
	
	# Attributes
	
	iterable: `list`
	The list to iterate through.
	"""
	t = Timer()
	r = [n for n in iterable if n % 2 != 0]
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r
	
	
def divisible(iterable:list, divider:int, timer=False):
	"""
	Finds all the numbers in a list that are divisible by the number passed.
	
	# Attributes
	
	iterable: `list`
	The list to iterate through.
	
	divider: `int`
	The number to check if divisible by.
	"""
	t = Timer()
	r = [n for n in iterable if n % divider == 0]
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r
	
	
def not_divisible(iterable:list, divider:int, timer=False):
	"""
	Finds all the numbers in a list that are not divisible by the number passed.
	
	# Attributes
	
	iterable: `list`
	The list to iterate through.
	
	divider: `int`
	The number to check if not divisible by.
	"""
	t = Timer()
	r = [n for n in iterable if n % divider != 0]
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r

def list2dict(iterable:list, timer=False):
	"""
	Converts a list to a dictionary.

	The item and value should be passed as [i, v] as items in the list, for example `[[1,2], [3,4]]` where this would be converted to `{1:2, 3:4}`.

	# Attributes

	iterable: `list`
		The list to convert.
	"""
	t = Timer()
	r = {i[0]:i[1] for i in iterable}
	if timer or DEBUG: return t.return_result(r)
	else: return r

def list2tuple(iterable:list, timer=False):
	"""
	Converts a list to a tuple.

	Items inside the list are also converted to tuples if they are a list.

	# Attributes

	iterable: `list`
		The list to convert.
	"""
	t = Timer()
	if type(iterable) != list:
		t.stop()
		if timer or DEBUG: return iterable, t.result
		else: return iterable
	r = tuple(list2tuple(i) for i in iterable)
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r


def tuple2list(iterable:tuple, timer=False):
	"""
	Converts a tuple to a list.

	Items inside the tuple are also converted to lists if they are a tuple.

	# Attributes

	iterable: `tuple`
		The tuple to convert.
	"""
	if type(iterable) != tuple: return iterable
	return list(tuple2list(i) for i in iterable)
	t = Timer()
	if type(iterable) != tuple:
		t.stop()
		if timer or DEBUG: return iterable, t.result
		else: return iterable
	r = list(tuple2list(i) for i in iterable)
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r
	

def dict2list(dictionary:dict, timer=False):
	"""
	Converts a dictionary to a list.

	The list is sorted based on the dictionary keys/items.

	# Attributes

	dictionary: `dict`
		The dictionary to convert.
	"""
	t = Timer()
	r = [[i,dictionary[i]] for i in [x for x in insertionSort([i[0] for i in list(dictionary.items())])]]
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r


def reverse(iterable:list, timer=False):
	"""
	Reverses the order of items in a list.

	# Attributes

	iterable: `list`
		The list of items to reverse.
	"""
	t = Timer()
	r = [iterable[len(iterable)-i-1] for i in range(len(iterable))]
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r


def secs2mins(duration:float, decimals:int=0, timer=False):
	"""
	Converts a number from seconds to minutes by dividing by 60.

	The result can be rounded to a certain number of decimal places (defaults to a whole number).

	# Attributes

	duration: `float`
		The seconds to convert into minutes.

	decimals: `int`
		Number of decimal places to round the result to.
	"""
	t = Timer()
	r = duration/60 if decimals < 0 else round(duration/60,decimals)
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r


def mins2hour(duration:float, decimals:int=0, timer=False):
	"""
	Converts a number from minutes to hours by dividing by 60.

	The result can be rounded to a certain number of decimal places (defaults to a whole number).

	# Attributes

	duration: `float`
		The seconds to convert into hours.

	decimals: `int`
		Number of decimal places to round the result to.
	"""
	t = Timer()
	r = duration/60 if decimals < 0 else round(duration/60,decimals)
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r


def add(*nums, timer=False):
	"""
	Adds an unlimited amount of numbers together.

	If you want to pass a list instead of a set of numbers separated by commas, then use `*` - for example `add(*nums)` where nums is a list of numbers.

	For normal use, do `add(1,2)` which would return 3.

	# Attributes
	
	*nums: `tuple`
		The list of numbers as explained in the main description.
	"""
	total = 0
	t = Timer()
	for n in nums: total += n
	t.stop()
	if timer or DEBUG: return t.return_result(total)
	else: return total


def subtract(*nums, timer=False):
	"""
	Subtracts an unlimited amount of numbers together.

	If you want to pass a list instead of a set of numbers separated by commas, then use `*` - for example `subtract(*nums)` where nums is a list of numbers.

	For normal use, do `subtract(4,1)` which would return 3.

	# Attributes
	
	*nums: `tuple`
		The list of numbers as explained in the main description.
	"""
	total = 0
	t = Timer()
	for n in nums: total -= n
	t.stop()
	if timer or DEBUG: return t.return_result(total)
	else: return total


def multiply(*nums, timer=False):
	"""
	Multiplies an unlimited amount of numbers together.

	If you want to pass a list instead of a set of numbers separated by commas, then use `*` - for example `multiply(*nums)` where nums is a list of numbers.

	For normal use, do `multiply(3,2)` which would return 6.

	# Attributes
	
	*nums: `tuple`
		The list of numbers as explained in the main description.
	"""
	total = 1
	t = Timer()
	for n in nums: total *= n
	t.stop()
	if timer or DEBUG: return t.return_result(total)
	else: return total


def divide(*nums, timer=False):
	"""
	Divides an unlimited amount of numbers together.

	If you want to pass a list instead of a set of numbers separated by commas, then use `*` - for example `divide(*nums)` where nums is a list of numbers.

	For normal use, do `divide(3,2)` which would return 1.5.

	# Attributes
	
	*nums: `tuple`
		The list of numbers as explained in the main description.
	"""
	total = nums[0]
	t = Timer()
	if len(nums) > 1:
		for n in nums[1:]: total /= n
	t.stop()
	if timer or DEBUG: return t.return_result(total)
	else: return total


def generate(start:int,end:int=None, timer=False):
	"""
	"""
	if end is None: limit, start= start, 0
	else: limit, start = end, start
	t = Timer()
	r = [n for n in range(start, limit)]
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r


def pi(decimal:int=9,timer=False):
	k = 1
	# Initialize sum
	s = 0
	for i in range(1000000):
	    # even index elements are positive
	    if i % 2 == 0:
	        s += 4/k
	    else:
	        # odd index elements are negative
	        s -= 4/k
	    # denominator is odd
	    k += 2
	return s


def factorial(value:int, timer=False):
	"""
	Calculates the factorial value of a number.

	This is calculated with the formula: `n! = n x (n-1) x (n-2) ... 3 x 2 x 1`. `!` represents factorial.

	# Attributes

	value: `int`
		The value to calculate the factorial of.
	"""
	r = value
	t = Timer()
	for i in reversed(list(range(1,value))): r *= i
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r


def sin(value:float, timer=False):
	"""
	Calculates the sine of a value.

	# Attributes

	value: `float`
		The value to calculate the sine of.
	"""
	t = Timer()
	r = math.sin(math.radians(value))
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r


def cos(value:float, timer=False):
	"""
	Calculates the cosine of a value.

	# Attributes

	value: `float`
		The value to calculate the cosine of.
	"""
	t = Timer()
	r = math.cos(math.radians(value))
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r


def tan(value:float, timer=False):
	"""
	Calculates the tangent of a value.

	# Attributes

	value: `float`
		The value to calculate the tangent of.
	"""
	t = Timer()
	r = math.tan(math.radians(value))
	t.stop()
	if timer or DEBUG: return t.return_result(r)
	else: return r


def mean(iterable:list, timer=False):
	"""
	Calculates the mean average of a list of items.

	# Attributes

	iterable: `list`
		The list of items to find the average of.
	"""
	t = Timer()
	total = 0
	for i in iterable: total += i
	total /= len(iterable)
	t.stop()
	if timer or DEBUG: return t.return_result(total)
	else: return total


def median(iterable:list, timer=False):
	"""
	Calculates the middle number of the list of items.

	If the length of the list is even, it calculates the middle of the two middle numbers.

	# Attributes

	iterable: `list`
		The list of items to find the middle of.
	"""
	t = Timer()
	two = True if len(iterable)%2==0 else False
	if two:
		firstindex = int(len(iterable)/2)-1
		secondindex = firstindex + 1
		middle = iterable[secondindex]-((iterable[secondindex] - iterable[firstindex])/2)
	else:
		middle = iterable[len(iterable)//2]
	t.stop()
	if timer or DEBUG: return t.return_result(middle)
	else: return middle


def mode(iterable:list, timer=False):
	"""
	Calculates the most common number out of the list of items.

	If there are two or more items that appear the same amount of time, then a `list` of those items is returned. Otherwise, the item is returned as its own data type.

	# Attributes

	iterable: `list`
		The list of items to find the most common number from.
	"""
	t = Timer()
	r = {i:0 for i in iterable}
	for i in iterable: r[i] += 1
	highest = []
	for counted in r:
		if len(highest) == 0: highest.append(counted)
		else:
			if r[counted] > r[highest[0]]:
				highest = [counted]
			elif r[counted] == r[highest[0]]:
				highest.append(counted)
	t.stop()
	if len(highest) == 1: highest = highest[0]
	if timer or DEBUG: return t.return_result(highest)
	else: return highest