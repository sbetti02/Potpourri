import random

def _merge(left, right):
    """Merge the left and right sides together"""
    merged = []
    left_ind = 0
    right_ind = 0
    left_len = len(left)
    right_len = len(right)
    while left_ind < left_len and right_ind < right_len:
        if left[left_ind] < right[right_ind]:
            merged.append(left[left_ind])
            left_ind += 1
        else:
            merged.append(right[right_ind])
            right_ind += 1
    while left_ind < left_len:
        merged.append(left[left_ind])
        left_ind += 1
    while right_ind < right_len:
        merged.append(right[right_ind])
        right_ind += 1
    return merged

def mergesort(list):
    """
        Basic merge sort algorithm.  
        Recursively break into 2 sides and merge them together
    """
    num_elems = len(list)
    if num_elems <= 1:
        return list
    left = mergesort(list[:num_elems/2])
    right = mergesort(list[(num_elems/2):])
    return _merge(left, right)

def quicksort(list):
    """
        Basic quicksort algorithm.
        Partition elements with first element, recurse on both halves
    """
    num_elems = len(list)
    if num_elems <= 1:
        return list
    left = []
    right = []
    parts = []
    partition = list[0]
    for num in list:
        if num < partition:
            left.append(num)
        elif num > partition:
            right.append(num)
        else:
            parts.append(num)
    sorted_elems = quicksort(left) + parts + quicksort(right)
    return sorted_elems

def _swap(list, i, j):
    """Swap under assumption that i and j are in bounds of the array"""
    if i >= j:
        return
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def inplace_quicksort(list, i, j):
    """
        Quicksort algorithm without using extra space
    """
    # Swap partition with last element
    # Two pointers, one at beginning and end of index, other at end
    # Find i where list[i] > partition and list[j] < partition, swap i and j
    # Swap partition with location i
    # recurse excluding partition
    if i >= j:
        return
    init_i = i
    init_j = j
    partition = list[init_i]
    _swap(list, init_i, init_j)
    j -= 1
    while i<=j:
        while i<=j and list[i] < partition:
            i += 1
        while j>=i and list[j] >= partition:
            j -= 1
        if i<j:
            _swap(list, i, j)
            i += 1
            j -= 1
    _swap(list, i, init_j)
    inplace_quicksort(list, init_i, i-1)
    inplace_quicksort(list, i+1, init_j)
    return list



def main():
    unsorted = random.sample(xrange(100), 10)
    print unsorted
    print mergesort(unsorted)
    print quicksort(unsorted)
    print "running in place quicksort"
    print inplace_quicksort(unsorted, 0, 9)
    print inplace_quicksort([23, 9, 10, 63, 82, 64, 60, 37, 58, 95], 0, 9)
    print inplace_quicksort([3,2,3], 0, 2)

if __name__ == "__main__":
    main()


