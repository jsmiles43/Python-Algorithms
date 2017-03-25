


def insertionSort(unsorted_list):
	for i,v in enumerate(unsorted_list):
		j = i
		while j > 0:
			if unsorted_list[j] < unsorted_list[j - 1]:
				temp = unsorted_list[j - 1]
				unsorted_list[j - 1] = unsorted_list[j]
				unsorted_list[j] = temp
			j -= 1
	return unsorted_list

print(insertionSort([7,3,21,4,9,1, 1001, 25, 43, 56, 78]))