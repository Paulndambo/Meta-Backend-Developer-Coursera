def heap_sort_descending(arr):
    n = len(arr)

    # Build a min heap from the input array
    for i in range(n // 2 - 1, -1, -1):
        heapify_descending(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move the root element to the end of the array
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the reduced heap
        heapify_descending(arr, i, 0)

    return arr

def heapify_descending(arr, n, i):
    smallest = i  # Initialize smallest as root
    left = 2 * i + 1  # left child
    right = 2 * i + 2  # right child

    # If left child is smaller than root
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # If right child is smaller than smallest so far
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If smallest is not root
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Swap
        # Recursively heapify the affected sub-tree
        heapify_descending(arr, n, smallest)


# Example usage
arr = [2, 28, 45, 3, 7, 9, 12]
result = heap_sort_descending(arr)
print(arr)
