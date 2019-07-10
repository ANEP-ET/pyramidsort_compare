import math
import time
import random

"""
http://www.geekviewpoint.com/python/sorting/quicksort
"""

def quick_sort( aList ):
    _quick_sort( aList, 0, len( aList ) - 1 )
 
def _quick_sort( aList, first, last ):
    if first < last:
      pivot = partition( aList, first, last )
      _quick_sort( aList, first, pivot - 1 )
      _quick_sort( aList, pivot + 1, last )
 
 
def partition( aList, first, last ) :
    pivot = first + random.randrange( last - first + 1 )
    swap( aList, pivot, last )
    for i in range( first, last ):
      if aList[i] <= aList[last]:
        swap( aList, i, first )
        first += 1
 
    swap( aList, first, last )
    return first
 
def swap( A, x, y ):
  A[x],A[y]=A[y],A[x]



def merge_sort(sequence):
    """
    Sequence of numbers is taken as input, and is split into two halves, following which they are recursively sorted.
    """
    if len(sequence) < 2:
        return sequence

    mid = len(sequence) // 2     # note: 7//2 = 3, whereas 7/2 = 3.5

    left_sequence = merge_sort(sequence[:mid])
    right_sequence = merge_sort(sequence[mid:])

    return merge(left_sequence, right_sequence)

"""
https://stackoverflow.com/questions/18761766/mergesort-with-python
"""

def merge(left, right):
    """
    Traverse both sorted sub-arrays (left and right), and populate the result array
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result

"""
https://www.geeksforgeeks.org/python-program-for-bubble-sort/
"""

def bubble_sort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def pyramidize_min(h):
    if len(h) == 1 or len(h) == 0:
        return h
    h0 = int(math.log2(len(h)).floor()) + 1
    i = int(math.floor(len(h) / 2)) - 1
    while i != -1:
        heapify_min(h, i)
        i -= 1
    X = h
    for i in range(1, h0 + 1):
        pc1 = int(math.pow(2, i - 1))
        pc2 = pc1 << 1
        if i == h0:
            X[(pc1 - 1):(len(h))] = pyramidize_min(h[(pc1 - 1):(len(h))])
        else:
            X[(pc1 - 1):(pc2 - 1)] = pyramidize_min(h[(pc1 - 1):(pc2 - 1)])
    for i in range(1, h0):
        pc1 = int(math.pow(2, i - 1))
        pc2 = pc1 << 1
        pc3 = pc2 << 1
        if i == h0 - 1:
            M = merge_min(X[(pc1 - 1):(pc2 - 1)], X[(pc2 - 1):(len(h))])
            
            X[(pc1 - 1):(pc2 - 1)] = M[0:(pc2 - pc1)]
            X[(pc2 - 1):(len(h))] = M[(pc2 - pc1):(len(h) - pc1 + 1)]
        else:
            M = merge_min(X[(pc1 - 1):(pc2 - 1)], X[(pc2 - 1):(pc3 - 1)])
            X[(pc1 - 1):(pc2 - 1)] = M[0:(pc2 - pc1)]
            X[(pc2 - 1):(pc3 - 1)] = M[(pc2 - pc1):(pc3 - pc1)]
    return X

def heapify_min(h, i):
    least = i
    if 2*i + 1 < len(h) and h[least] > h[2*i + 1]:
        least = 2*i + 1
    if 2*i + 2 < len(h) and h[least] > h[2*i + 2]:
        least = 2*i + 2
    if i != least:
        tmp = h[least]
        h[least] = h[i]
        h[i] = tmp
        heapify_min(h, least)

def merge_min(x, y):
    if len(x) == 0:
        return y
    if len(y) == 0:
        return x
    if x[0] <= y[0]:
        return [x[0]] + merge_min(x[1:], y)
    else:
        return [y[0]] + merge_min(x, y[1:])

a = [1]
file1 = open("p.dat","w") 
file2 = open("m.dat","w")
file3 = open("q.dat","w")
file4 = open("b.dat","w")

for i in range (1, 1500):
    a.append(random.random() * 1500)
    tic = time.process_time()
    pyramidize_min(a)
    toc = time.process_time()
    file1.write(('{}, {}\n').format(i, toc - tic))

    tic = time.process_time()
    merge_sort(a)
    toc = time.process_time()
    file2.write(('{}, {}\n').format(i, toc - tic))

    tic = time.process_time()
    quick_sort(a)
    toc = time.process_time()
    file3.write(('{}, {}\n').format(i, toc - tic))

    tic = time.process_time()
    bubble_sort(a)
    toc = time.process_time()
    file4.write(('{}, {}\n').format(i, toc - tic))
