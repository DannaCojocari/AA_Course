def heapify(arr, n, i):
    maximum = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        maximum = left

    if right < n and arr[maximum] < arr[right]:
        maximum = right

    if maximum != i:
        arr[i], arr[maximum] = arr[maximum], arr[i]
        heapify(arr, n, maximum)


def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
