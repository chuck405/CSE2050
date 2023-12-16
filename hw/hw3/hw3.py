import time

def find_pairs_naive(lst, target):
    """
    Function that iterates over the entire list using 2 nested loops to check for pairs that add up to the target
    """
    # Initializes an empty solution set
    solution_set = set()                                                            ## 2 - create, assign
    # Checks every integer in lst
    for i in lst:                                                                   ## n loops times:
        # If the integer is half of the target and appears more than once, adds a tuple to solution_set
        if ((2*i) == target) and (lst.count(i) > 1):                                ## 3 - artihmetic, compare, compare
                solution_set.add((i, i))                                            ## 1 - set addition
        # If the integer has a pair in lst that would add to the target and the 2 numbers have not already been used, adds a tuple to solution_set
        for j in lst:                                                               ## n loops times:
            if ((i + j) == target) and (i != j) and (j, i) not in solution_set:     ## 4 - arithmetic, compare, compare, membership testing
                solution_set.add((i, j))                                            ## 1 - set addition
    return solution_set                                                             ## 1 - return
                                                                                    ## ------------------------------------------------
                                                                                    ## (2 + n(3 + 1 + n(4 + 1)) + 1) = (5n^2 + 5n + 3) = O(n^2)
                                                                                    ## RESULTS: inefficient function that operates in quadratic time due to the use of 2 nested loops


def find_pairs_optimized(lst, target):
    """
    Function that uses a data structure to improve time complexity
    """
    # Initializes a set to store previously viewed values
    prev_values = set()                                                             ## 2 - create, assign
    # Initializes an empty solution set
    solution_set = set()                                                            ## 2 - create, assign
    # Checks every integer in lst
    for i in lst:                                                                   ## n loops times:
        # If the integer's pair has already been viewed, adds a tuple to solution_set
        if (target - i) in prev_values and (i, target - i) not in solution_set:     ## 4 - arithmetic, membership testing, arithmetic, membership testing
            solution_set.add((target - i, i))                                       ## 2 - set addition, arithmetic
        # Adds the integer that has just been checked to previously viewed values
        prev_values.add(i)                                                          ## 1 - set addition
    return solution_set                                                             ## 1 - return
                                                                                    ## ------------------------------------------------
                                                                                    ## (2 + 2 + n(4 + 2 + 1) + 1) = (7n + 5) = O(n)
                                                                                    ## RESULTS: optimized function that operates in linear time due to the use of only a singular loop and the use of the prev_values set


def measure_min_time(fn, args=()):
    """
    Function that measures the minimum time of 10 runs using the time module
    """
    # Initializes an empty list
    time_list = list()
    # Calls the function 10 times and adds the elapsed time for each trial to time_list
    for i in range(0,10):
        start = time.time()
        fn(*args)
        time_list.append(time.time() - start)
    # Sorts time_list from shortest to longest times so that the shortest time can be easily returned
    time_list.sort()
    return time_list[0]


# Prints out a table showing the time taken (in milliseconds) for both functions as n increases, rounding the times to 4 decimals
c1, c2, c3 = " n", "    naive", "   optimized"
print(f"{c1:3}{c2:10}{c3:10}\n" + "*"*27)
for n in [10, 50, 100, 150, 200, 300, 500]:
    print(f"{n:3}{1000*measure_min_time(find_pairs_naive, (list(range(n)), 1)):10.4f}{1000*measure_min_time(find_pairs_optimized, (list(range(n)), 1)):10.4f}")
print("*" * 27)