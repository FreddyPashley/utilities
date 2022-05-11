version = "0.1"

def bubbleSort(iterable):
	for i in range(len(iterable)):
		for j in range(len(iterable) - 1):
			if iterable[j] > iterable[j+1]:
				iterable[j+1], iterable[j] = iterable[j], iterable[j+1]
	return iterable

