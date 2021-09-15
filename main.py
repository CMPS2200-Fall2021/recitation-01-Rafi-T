"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###



def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
        if right >= left:
                middle = int ((left + right)/2)
                if mylist[middle]== key:
                        return middle
                elif mylist[middle] > key:
                        return _binary_search(mylist, key,left, middle - 1, )
                elif mylist[middle] < key:
                        return _binary_search(mylist, key, middle + 1, right)
        else:
                return -1

def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	assert binary_search([7,10,11,12,13], 10) == 1
	assert binary_search([5,4,20,9,6], 5) == 0
	pass


def time_search(search_fn, mylist, key):

        secs = time.time()
        search_fn(mylist, key)
        secs = time.time() - secs
        return secs*1000
	




def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
      
        key = -1
        mylist = []
        for size in sizes:
                linear_search_time = time_search(linear_search, range(int(size)), key)
                binary_search_time = time_search(binary_search, range(int(size)), key)
                t = (size,linear_search_time,binary_search_time)
                mylist.append(t)
        return mylist

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
		headers=['n', 'linear', 'binary'],
		floatfmt=".3f",
		tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1


