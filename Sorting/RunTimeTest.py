import insertion_sort as sort


import time, random

def InsertionSortTestBest():
	a,b = [], []
	for i in range(1000):
		a.append(i)

	a.append(random.randint(0, 1000))		#insert random number so list is nearly sorted
	for i in range(2000):
		b.append(i)
	b.append(random.randint(0, 2000))
	timeNow = time.time()
	a = sort.insertionSort(a)
	print(round(time.time() - timeNow, 7))

	timeNow = time.time()
	b = sort.insertionSort(b)
	print(round(time.time() - timeNow, 7))

def InsertionSortTestWorst():
	a,b = [], []
	for i in range(1000):
		a.append(random.randint(0, 1000))

	for i in range(2000):
		b.append(random.randint(0, 2000))  
	

	timeNow = time.time()
	a = sort.insertionSort(a)
	print(round(time.time() - timeNow, 7))

	timeNow = time.time()
	b = sort.insertionSort(b)
	print(round(time.time() - timeNow, 7))















def main():
	print('Insertion Sort Test of Time Complexity on nearly sorted array: O(n)')
	InsertionSortTestBest()
	print('Insertion Sort Test of Time Complexity on unsorted array: O(n^2)')
	InsertionSortTestWorst()


main()