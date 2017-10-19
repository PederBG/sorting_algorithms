""" Radix Sort assumes that each element in the list A has the same number of digits d. Then it sorts the list by
sorting one digit at the time, starting from least significant digit. Here we use bucket sort to do the initial soring,
but any stable sorting algorithm will work (stable means that the algorithm preserves the initial order of two similar
numbers).
RUNTIME: Best: Ω(n*d),  Average: Θ(n*d),  Worst: O(n*d), where d is the number of digits.  (ish ?)"""

def RadixSort(A, d):
    for i in range(d-1, -1, -1):  # Iterating trough the digits starting from the least significant
        for j in range(0, len(A)):
            B = [[] for z in range(10)]

            for k in range(0, len(A)):  # Bucket sort for each digit in the elements from A
                    index = int(str(A[k])[i])
                    B[index].append(A[k])
            A = sum(B, [])  # Collapsing the sub lists (clever short method)
    return A
"""
import random
li = []
for x in range(0, 100):
    li.append(random.randint(100, 1000))

print(li)
print(RadixSort(li, 3))
"""