#quickSort algorithm

import random

def quickSort(lst):
    """ sorting algorithm geared to run in O(n_log_n) runtime,
    with worst case of O(n^2)
    """
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        less = []
        greater = []
        for i in range(1,len(lst)):
            if lst[i] <= pivot:
                less += [lst[i]]
            else:
                greater += [lst[i]]
                    
    return quickSort(less) + [pivot] + quickSort(greater)

