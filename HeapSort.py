
def MaxHeapify(A, i): # RUNTIME: Θ(log(n))
    print(A)
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, largest)

def BuildMaxHeap(A): # RUNTIME: Θ(n)
    for i in range(len(A) // 2, -1, -1):
        MaxHeapify(A, i)

def HeapSort(A):  # DOES NOT WORK MADDAFAKKA
    BuildMaxHeap(A)
    print("--------")
    for i in range(len(A)-1, 1, -1):
        top = A[0]
        A[0] = A[i]
        A[i] = top
        MaxHeapify(A[0:i], 0)


#  ---------------------------------------------

alist = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
blist = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

HeapSort(blist)
print(blist)