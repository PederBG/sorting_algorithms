""" Sorting the list by iterating upwards and moving each element back in the list until it's sorted with respect on
the elements that comes before.
    RUNTIME: Best: Ω(n),  Average: Θ(n^2),  Worst: O(n^2) """

def InsertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j > -1 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
#  ---------------------------------------
"""
l = [4, 3, 2, 6, 1]
InsertionSort(l)
print(l)
"""