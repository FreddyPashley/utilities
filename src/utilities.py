version = "0.1"

def bubbleSort(iterable):
	for i in range(len(iterable)):
		for j in range(len(iterable) - 1):
			if iterable[j] > iterable[j+1]:
				iterable[j+1], iterable[j] = iterable[j], iterable[j+1]
	return iterable


def insertionSort(iterable):
	for i in range(1, len(iterable)):
		key = iterable[i]
		j = i-1
		while j >=0 and key < iterable[j] :
				iterable[j+1] = iterable[j]
				j -= 1
		iterable[j+1] = key
	return iterable