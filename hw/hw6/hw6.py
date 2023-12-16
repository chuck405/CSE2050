# TODO: implement the 4 functions (as always, include docstrings & comments)

def find_zero(L):
    """Function that finds the zero index of a half-sorted list"""
    # initializes low and high to represent the bounds of the list
    low, high = 0, len(L)
    # edge case for empty lists
    if high == 0: raise RuntimeError("list is empty")
    # edge case for lists that contains 2 elements
    if high == 2:
        if L[0] == 0: return 0
        else: return 1
    # repeatedly slices the list in half until the middle is equal to 0
    while low <= high:
        mid = (low + high) // 2
        if L[mid] == 0: return mid
        elif L[mid] < 0: low = mid
        else: high = mid

def bubble(L, left, right):
    """Function that sorts a sub-list using the bubble algorithm"""
    # repeatedly checks every value and compares it to the value directly after - swaps the positions if the first is greater than the second
    swap = True
    while (swap):
        # sets swap to False since if the sub-list is passed through with no swaps made, no further sorting is required
        swap = False
        for i in range(left, right-1):
            if L[i] > L[i+1]: 
                L[i], L[i+1] = L[i+1], L[i]
                swap = True

def selection(L, left, right):
    """Function that sorts a sub-list using the selection algorithm"""
    # repeatedly checks for the next greatest value, then moves it towards the end of the sub-list
    for i in range(left, right-1):
        max_index = left
        for j in range(left, right+left-i):
            if L[j] > L[max_index]: max_index = j
        L[right+left-i-1], L[max_index] = L[max_index], L[right+left-i-1]            

def insertion(L, left, right):
    """Function that sorts a sub-list using the insertion algorithm"""
    # repeatedly checks the last i values of the sub-list - swaps the positions if they are out of order
    for i in range(left, right):
        j = right+left-i
        # performs swaps only if needed to remain time-efficient
        while j < right and L[j-1] > L[j]:
            L[j-1], L[j] = L[j], L[j-1]
            j += 1

def sort_halfsorted(L, sort):
    '''Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items
    
        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            >>> L = [-1, -2, -3, 0, 3, 2, 1]
            >>> sort_halfsorted(L, bubble)
            >>> print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    '''

    idx_zero = find_zero(L)     # find the 0 index 
    sort(L, 0, idx_zero)        # sort left half
    sort(L, idx_zero+1, len(L)) # sort right half