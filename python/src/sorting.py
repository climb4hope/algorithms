"""
This module provides different sorting algorithms APIs.
    > Selection Sort (O(n^2)) - In-place sorting
        - compares the first element in the array with all
          the following elements and swaps them when the lowest
          is found.
        - typically this type of algorithms is unstable.
        - can be implemented as recursive or iterative

    > Insertion Sort - best case O(n), worst case O(n^2)
        - this algorithm is stable
        - used for small data sets sorting
        - often used for block building for more complex
        sorting algorithms

    > Quicksort - best case O(n * log(n)), worst case - O(n^2)
        - is a divide-and-conquer algorithm that involves choosing
          a pivot value from a data set and splitting the set into
          two subsets. The pivot/split process is recursively applied
          to each subset until there are no more subsets to split.
          The results are combined to  form the final sorted set.
        - best case is if pivot value is chosen such that it splits
          array into two nearly equal subsets.
        - most implementation of the quicksort are unstable

    > Merge Sort
        - Another divide-and-conquer algorithm that works by splitting a
          data set into two or more subsets, sorting the subsets and
          then merging them together into final sorted set.

    > Shell - best case O(n^(3/2)), worst - O(n^(4/3)) or O(n*lg^2(n))
        - Because shell sort is based on insertion sort, shell sort
          inherits insertion sort's adaptive properties. The adapation
          is not as dramatic because shell sort requires one pass through
          the data for each increment, but it is significant.

    The ideal sorting algorithm would have the following properties:
        > Stable: Equal keys aren't reordered.
        > Operates in place, requiring O(1) extra space.
        > Worst-case O(n * lg(n)) key comparisons.
        > Worst-case O(n) swaps.
        > Adaptive: Speeds up to O(n) when data is nearly sorted or when there are few unique keys.


    Algorithms summary:
    ----------------------------------------------------------------------------
    Sort Method       | Complexity | Stability  | Extra space | Best Application
    ----------------------------------------------------------------------------
    1. Selection      | O(n^2)     | Not stable |    O(1)     |  Non-adaptive
    2. Insertion      | O(n^2)     | Stable     |    O(1)     |  Nearly sorted
    3. Bubble         | O(n^2)     | Stable     |    O(1)     |  Nearly sorted
    4. Shell          | O(n^(3/2)) | Not stable |    O(1)     |  Nearly sorted
    5. Merge          | O(n*lg(n)) | Stable     |    O(n)     |  Non-adaptive
    6. Heap           | O(n*lg(n)) | Not Stable |    O(1)     |  Not really adaptive
    7. Quick          | O(n^2)     | Not stable |    O(lg(n)  |  Non-adaptive
    8. Quick 3        | O(n^2)     | Not stable |    O(lg(n)  |  Adaptive: O(n) time when O(1) unique keys
"""

import math


###############################################################
# Selection Sort Method                                       #
###############################################################
def SelectionSortIterative(data, current_index):
    """

    :param data: and array of data that has to be sorted
    :param current_index: starting element index
    :return:
    """
    for current_index in range(len(data)):
        Swap(data, current_index, FindMinElementIndex(data, current_index))

    return

def SelectionSortRecursive(data, current_index):
    """

    :param data: and array of data that has to be sorted
    :param current_index: starting element index
    :return:
    """
    if current_index < len(data) - 1:
        Swap(data, current_index, FindMinElementIndex(data, current_index))
        SelectionSortRecursive(data, current_index + 1)

    return


def Swap(data, current_index, new_index):
    """
    This is the helper function to swap
    two elements in the array.
    :param data:
    :param current_index:
    :param new_index:
    :return:
    """
    # Perform a swap if the index is different
    if new_index != current_index:
        tmp = data[current_index]
        data[current_index] = data[new_index]
        data[new_index] = tmp
    return


def FindMinElementIndex(data, current_index):
    """
    This is a helper function that finds a min
    element index in the array starting from
    current index
    :param data:
    :param current_index:
    :return:
    """
    min_idx = current_index
    for i in range(current_index + 1, len(data)):
        if data[i] < data[min_idx]:
            min_idx = i

    return min_idx

###############################################################
# Insertion Sort Method                                       #
###############################################################
def InsertionSort(data):
    """
    This is the insertion sort algorithm
    :param data:
    :return:
    """
    # Start with the second element
    for idx in range(1, len(data)):
        val = data[idx]

        # loop through all previous elements
        i = idx - 1
        while(i >= 0) and data[i] > val:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = val

    return


###############################################################
# QuickSort Method                                            #
###############################################################
def QuickSortSimple(data):
    """
    A Simple version of the recursive quicksort algorithm.
    :param data:
    :return:
    """
    n = len(data)

    # Stop is there is only one element
    if n < 2:
        return data

    pivot_index = n // 2
    pivot_value = data[pivot_index]

    left_count = 0
    # count how many are less than pivot
    for i in range(n):
        if data[i] < pivot_value:
            left_count += 1

    # Allocate the arrays and create the subset
    left = []
    right = []

    for i in range(n):
        # Skip the pivot element
        if i == pivot_index:
            continue

        # Create subsets
        val = data[i]
        if val < pivot_value:
            left.append(val)
        else:
            right.append(val)

    # Sort the subsets
    left = QuickSortSimple(left)
    right = QuickSortSimple(right)

    # Combine the sorted arrays and pivot back
    data = []
    data.extend(left)
    data.append(pivot_value)
    data.extend(right)

    return data


###############################################################
# MergeSort Method                                            #
###############################################################
def MergeSortSimple(data):
    """
    Recursive merge sort algorithm implementation
    :param data:
    :return:
    """
    n = len(data)

    # Stop if this is the only element in the array
    if n < 2:
        return data

    # Split the array into two sub-arrays of approximately the same size
    mid = n // 2
    left = []
    right = []

    # Copy the arrays
    left = data[:mid]
    right = data[mid:]

    # Sort each array and then merge them together
    MergeSortSimple(left)
    MergeSortSimple(right)

    return merge(data, left, right)


def merge(dest, left, right):
    """
    Helper function that merges two arrays together
    :param dest:
    :param left:
    :param right:
    :return:
    """
    data_idx = 0
    left_idx = 0
    right_idx = 0

    # merge arrays while there are elements in both
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            dest[data_idx] = left[left_idx]
            data_idx += 1
            left_idx += 1
        else:
            dest[data_idx] = right[right_idx]
            data_idx += 1
            right_idx += 1

    # Copy the rest of whichever array remains
    while left_idx < len(left):
        dest[data_idx] = left[left_idx]
        data_idx += 1
        left_idx += 1

    while right_idx < len(right):
        dest[data_idx] = right[right_idx]
        data_idx += 1
        right_idx += 1

    return dest


###############################################################
# ShellSort Method                                            #
###############################################################
def ShellSort(data):
    """
    Shell sort method
    :param data:
    :return:
    """
    n = len(data)

    # Generate increment sequence
    increment_sequence = generate_increments_sequence(n)

    # Loop through the increment sequence
    for incr in increment_sequence:
        # loop through each subset of the sequence
        for j in range(incr):
            # loop through each element in the subset
            for k in range(j, n, incr):
                guess = k
                # find the correct place for the element
                while guess >= incr and data[guess - incr] > data[guess]:
                    # swap two elements
                    data[guess], data[guess - incr] = data[guess - incr], data[guess]
                    guess -= incr

    return data


def generate_increments_sequence(length):
    """
    Helper frunction for Shell Sort algorithm.
    It generates the seqeunce equal to e^(n-2) + 1
    :param length:
    :return:
    """
    sequence = []
    idx = 0

    while True:
        idx += 1
        val = int(round(math.exp(idx - 2)) + 1)
        if val >= length:
            break
        sequence.append(val)

    return sequence


###############################################################
# Main Function
###############################################################
if __name__ == "__main__":
    #perform a test
    data_array = [1, 5, -5, 7, 12, 35, 3, -20, 7]

    print("Input Data = {0}".format(data_array))
    #SelectionSortRecursive(data_array, 0)
    #SelectionSortIterative(data_array, 0)
    #InsertionSort(data_array)
    #data_array = QuickSortSimple(data_array)
    #data_array = MergeSortSimple(data_array)
    data_array = ShellSort(data_array)

    print("Sorted Data = {0}".format(data_array))