""" Starts by presuming that all the elements in the list is an integer with a value between 0 and k. Then makes a new
list C that keeps track of how many elements there is of each value. Goes then backwards through list C and using it to
place elements from the start list A into the result list B.
    RUNTIME: Best: Ω(n + k),  Average: Θ(n + k),  Worst: O(n + k) """

def CountingSort(A, B, k):
    C = [0] * (k+1)
    for j in range(0, len(A)):
        C[A[j]] += 1  # C keeps track of how many elements C[i] that is equal to the index i.
    for i in range(1, k+1):
        C[i] = (C[i] + C[i - 1])  # C now keeps track of how many elements C[i] that is smaller or equal to the index i.
    for l in range(len(A)-1, -1, -1):
        B[C[A[l]] - 1] = A[l]
        C[A[l]] -= 1
    return B

# ------------------------------------------------
print( CountingSort([2, 5, 3, 0, 2, 3, 0, 3], [0]*8, 5) )
