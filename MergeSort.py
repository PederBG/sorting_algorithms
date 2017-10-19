""" Sorting the list by splitting it in half until each divided list has length 1. Then merges them together recursively
or iteratively.
    RUNTIME: Best: Ω(n log(n)),  Average: Θ(n log(n)),  Worst: O(n log(n)) """

def MergeSort(A):
    if len(A) > 1:
        mid = int(len(A) / 2)
        lefthalf = A[:mid]
        righthalf = A[mid:]

        MergeSort(lefthalf)
        MergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                A[k] = lefthalf[i]
                i += 1
            else:
                A[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            A[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            A[k] = righthalf[j]
            j += 1
            k += 1
#  ------------------------------------------------
A = [54,26,93,17,77,31,44,55,20]
MergeSort(A)
print(A)