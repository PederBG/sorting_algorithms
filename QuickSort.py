""" Sorting the list by dividing it up in two lists where all the elements in the first is smaller than the elements
in the second. Doing this recursively for smaller and smaller lists until length 1, then goes back and adding up the
lists.
    RUNTIME: Best: Ω(n log(n)),  Average: Θ(n log(n)),  Worst: O(n^2) """

def QuickSort(A):
    less = []
    equal = []
    greater = []
    if len(A) > 1:
        pivot = A[0]
        for x in A:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)
        return QuickSort(less) + equal + QuickSort(greater)
    else:
        return A