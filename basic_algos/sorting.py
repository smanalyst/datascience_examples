#bubble sort
def bubble_sort(foo):
    def swap(i, j):
        foo[i], foo[j] = foo[j], foo[i]

    n = len(foo)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if foo[i - 1] > foo[i]:
                swap(i - 1, i)
                swapped = True
                    
    return foo


#selection sort
def selection_sort(foo):        
    for i in range(len(foo)):
        minimum = i
        
        for j in range(i + 1, len(foo)):

            if foo[j] < foo[minimum]:
                minimum = j

        foo[minimum], foo[i] = foo[i], foo[minimum]
            
    return foo


#insertion sort
def insertion_sort(foo):
        
    for i in range(len(foo)):
        cursor = foo[i]
        pos = i
        
        while pos > 0 and foo[pos - 1] > cursor:

            foo[pos] = foo[pos - 1]
            pos = pos - 1

        foo[pos] = cursor

    return foo

#quick sort
def partition(array, start_point, end_point):
    pivot_idx = start_point
    for i in xrange(start_point+1, end_point+1):
        if array[i] <= array[start_point]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[start_point] = array[start_point], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, start_point, end_point):
    if start_point >= end_point:
        return
    pivot_idx = partition(array, start_point, end_point)
    quick_sort_recursion(array, start_point, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end_point)

def quick_sort(array, start_point=0, end_point=None):
    if end_point is None:
        end_point = len(array) - 1
    
    return quick_sort_recursion(array, start_point, end_point)