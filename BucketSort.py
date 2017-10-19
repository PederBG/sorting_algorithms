""" Works good if the element values in the list is evenly distributed. Argument m is the value of the biggest element
 in the list. Works by calculating an index from each of the elements and putting it in the right "bucket". Then sort
 each bucket and collapse the sub lists.
 RUNTIME: Best: Ω(n + k),  Average: Θ(n + k),  Worst: O(n^2), where k is number of buckets. """

from algoritmer.InsertionSort import InsertionSort

def BucketSort(A, m):
    B = [[] for i in range(len(A))]  # Makes an empty list of lists

    for j in range(0, len(A)):  # Populate the new list
        index = (A[j] * len(A)) // (m + 1)
        B[index].append(A[j])

    for k in range(0, len(A)):  # Sort each list
        InsertionSort(B[k])

    return sum(B, [])  # Collapsing the sub lists (clever short method)

#  --------------------------------------------------------
A = [102, 32, 476, 468, 954, 200, 754, 333, 654, 1000]
A_sorted = BucketSort(A, 1000)
print(A_sorted)
