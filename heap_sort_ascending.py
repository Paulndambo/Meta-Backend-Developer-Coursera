def heap_sort_ascending(arr):
    n = len(arr)

    # Build a max heap from the input array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move the root element to the end of the array
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the reduced heap
        heapify(arr, i, 0)

    return arr

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child
    right = 2 * i + 2  # right child

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)


arr = [2, 28, 45, 3, 7, 9, 12]
sorted_arr_ascending = heap_sort_ascending(arr)
print(sorted_arr_ascending)