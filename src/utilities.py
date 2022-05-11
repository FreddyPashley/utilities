version = "0.4"


def bubbleSort(iterable:list):
	"""
	Represents a bubble sort.

	This is best used on smaller iterables, and when the iterable is almost sorted already.

	# Attributes

	iterable: `list`
		The object to iterable through.
	"""
	for i in range(len(iterable)):
		for j in range(len(iterable) - 1):
			if iterable[j] > iterable[j+1]:
				iterable[j+1], iterable[j] = iterable[j], iterable[j+1]
	return iterable


def insertionSort(iterable:list):
	"""
	Represents an insertion sort.

	This is very efficient on small iterables, and is stable and quite fast when the iterable is nearly sorted.

	# Attributes

	iterable: `list`
		The object to iterable through.
	"""
	for i in range(1, len(iterable)):
		key = iterable[i]
		j = i-1
		while j >=0 and key < iterable[j] :
				iterable[j+1] = iterable[j]
				j -= 1
		iterable[j+1] = key
	return iterable


def mergeSort(iterable:list, zero:int, length_minus_one:int):
	"""
	Represents a merge sort.

	# Attributes

	iterable: `list`
		The object to iterable through.

	zero: `int`
		Always pass 0 into the merge sort.

	length_minus_one: `int`
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
		return arr
	return sort(iterable, zero, length_minus_one)


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