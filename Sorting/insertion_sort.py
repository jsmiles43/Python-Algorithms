

def insertionSort(unsorted_list):
	for i,v in enumerate(unsorted_list):
		j = i
		while j > 0 and unsorted_list[j] < unsorted_list[j - 1]:
			temp = unsorted_list[j - 1]
			unsorted_list[j - 1] = unsorted_list[j]
			unsorted_list[j] = temp
			j -= 1
	return unsorted_list


