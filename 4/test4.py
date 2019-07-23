import sys
import os
import math
import time
import random

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))
from Pyramid import pyramidize_min

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
