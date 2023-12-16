import time

def time_function(func, args, n_trials=10):
    time_list = []
    for i in range(0, n_trials):
        start = time.time()
        func(args)
        time_list.append(time.time() - start)
    time_list.sort()
    return time_list[0]

    
def time_function_flexible(f, args=(), n_trials=10):
    time_list = []
    for i in range(0,n_trials):
        start = time.time()
        f(*args)
        time_list.append(time.time() - start)
    time_list.sort()
    return time_list[0]


if __name__ == '__main__':
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)]
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))