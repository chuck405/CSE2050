from math import log2

# initializes the algorithms set in the global scope, allowing any function to modify it
algorithms = set()

def linear_scan(L):
    """Function that identifies certain edge cases in a list"""
    # checks each item and compares it to the item after
    errors = 0
    for i in range(len(L)-1):
        if L[i+1] < L[i]: errors += 1
        
    # depending on how many items are out of place, returns an optimal algorithm to sort the list
    if errors == 0: return None
    elif errors == len(L)-1: return "reverse_list"
    elif errors <= 5: return "insertionsort"
    else: return "quicksort"

def reverse_list(L):
    """Function that sorts a reverse sorted list"""
    L.reverse()

    # adds "reverse_list" to the set of algorithms used
    algorithms.add("reverse_list")

def insertionsort(L, left=None, right=None):
    """Function that sorts a sub-list using the insertion algorithm"""
    if left == None: left = 0
    if right == None: right = len(L)

    # repeatedly checks the last i values of the sub-list - swaps the positions if they are out of order
    for i in range(left, right):
        j = right+left-i

    # performs swaps only if needed to remain time-efficient
        while j < right and L[j-1] > L[j]:
            L[j-1], L[j] = L[j], L[j-1]
            j += 1

    # adds "insertionsort" to the set of algorithms used
    algorithms.add("insertionsort")

def quicksort(L, left=None, right=None, depth=0):
    """Function that sorts a list using the quick algorithm"""
    # keeps track of recursive depth and best-case maxmimum depth
    depth += 1
    max_depth = log2(len(L)) + 1
    # if recursive depth reaches twice the best-case maximum depth, falls back to mergesort to sort the list
    if depth > (2*max_depth): 
        mergesort(L)
        return
    if left == None: left = 0
    if right == None: right = len(L)
    # base case
    if right - left <= 1: return

    # divides the list by the pivot into sublists
    pivot = partition(L, left, right)

    # sorts sublists - when the sublists drop to 16 or fewer items, sorts the sublists using insertion sort instead
    if (pivot - left) <= 16: insertionsort(L, left, pivot)
    else: quicksort(L, left, pivot, depth)
    if (right - pivot + 1) <= 16: insertionsort(L, left, pivot)
    else: quicksort(L, pivot+1, right, depth)

    # adds "quicksort" to the set of algorithms used
    algorithms.add("quicksort")
    return

def partition(L, i, j):
    """Function used for quick sorting"""
    pivot = j - 1
    j = pivot - 1

    # pivots all items between left and right
    while i < j:
        while L[i] < L[pivot]:
            i += 1
        while i < j and L[j] >= L[pivot]:
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]

    # swaps pivot and i
    if L[i] >= L[pivot]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    return pivot


def mergesort(L):
    """Function that sorts a list using the merge algorithm"""
    # base case
    if len(L) < 2: return

    # divides the list into sublists
    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]

    # sorts sublists - when the sublists drop to 16 or fewer items, sorts the sublists using insertion sort instead
    if len(A) <= 16: insertionsort(A, 0, len(A))
    else: mergesort(A)
    if len(B) <= 16: insertionsort(B, 0, len(B))
    else: mergesort(B)
    
    # combines the sublists back together
    merge(L, A, B)
    
    # adds "mergesort" to the set of algorithms used
    algorithms.add("mergesort")
    return

def merge(L, A, B):
    """Function used for merge sorting"""
    # index into A and B
    i, j = 0, 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[i+j] = A[i]
            i += 1
        else:
            L[i+j] = B[j]
            j += 1
    
    # add any remaining elements once one list is empty
    L[i+j:] = A[i:] + B[j:]

def magic_sort(L):
    """Function that sorts a list using a combination of insertion, quick, and merge sorting to achieve optimal sorting efficiency"""
    algorithms.clear()
    
    # chooses an optimal sorting algorithm to start with based on the results of a linear scan
    if linear_scan(L) == None: algorithms.add("None")
    elif linear_scan(L) == "reverse_list": reverse_list(L)
    elif linear_scan(L) == "insertionsort": insertionsort(L, 0, len(L))
    elif linear_scan(L) == "quicksort": quicksort(L, 0, len(L))
    
    # returns a set containing which algorithms were used to sort the list
    return algorithms
