from quickSort import *
from mergeSort import *
from heapSort import *
from bucketSort import *
import random
import time
import matplotlib.pyplot as plt


def sortQuick(array, method, execution):
    start = time.perf_counter()
    quickSort(array)
    execution[method].append(time.perf_counter() - start)


def sortMerge(array, method, execution):
    start = time.perf_counter()
    mergeSort(array)
    execution[method].append(time.perf_counter() - start)


def sortHeap(array, method, execution):
    start = time.perf_counter()
    heapSort(array)
    execution[method].append(time.perf_counter() - start)


def sortBucket(array, method, execution):
    start = time.perf_counter()
    bucketSort(array)
    execution[method].append(time.perf_counter() - start)


if __name__ == '__main__':

    # Quick Sort
    execution = {
        "Sorted Array": [],
        "Random Array": [],
        "Negative Array": [],
        "Mixed Array": []
    }

    sortedSmallArray = sorted(random.sample(range(1, 10000), 20))
    randomSmallArray = random.sample(range(1, 10000), 20)
    negativeSmallArray = random.sample(range(-10000, 0), 20)
    mixedSmallArray = random.sample(range(-5000, 5000), 20)

    sortedMediumArray = sorted(random.sample(range(1, 10000), 100))
    randomMediumArray = random.sample(range(1, 10000), 100)
    negativeMediumArray = random.sample(range(-10000, 0), 100)
    mixedMediumArray = random.sample(range(-5000, 5000), 100)

    sortedMediumLargeArray = sorted(random.sample(range(1, 10000), 500))
    randomMediumLargeArray = random.sample(range(1, 10000), 500)
    negativeMediumLargeArray = random.sample(range(-10000, 0), 500)
    mixedMediumLargeArray = random.sample(range(-5000, 5000), 500)

    sortedLargeArray = sorted(random.sample(range(1, 10000), 998))
    randomLargeArray = random.sample(range(1, 10000), 998)
    negativeLargeArray = random.sample(range(-10000, 0), 998)
    mixedLargeArray = random.sample(range(-5000, 5000), 998)

    for size, arrays in [
        ("Small", [sortedSmallArray, randomSmallArray, negativeSmallArray, mixedSmallArray]),
        ("Medium", [sortedMediumArray, randomMediumArray, negativeMediumArray, mixedMediumArray]),
        ("Medium Large",
         [sortedMediumLargeArray, randomMediumLargeArray, negativeMediumLargeArray, mixedMediumLargeArray]),
        ("Large", [sortedLargeArray, randomLargeArray, negativeLargeArray, mixedLargeArray])
    ]:
        for key, array in zip(execution.keys(), arrays):
            sortQuick(array, key, execution)

    plt.figure(figsize=(10, 6))
    for method, times in execution.items():
        plt.plot(["Small (50)", "Medium (200)", "Medium Large (1000)", "Large (5000)"], times, marker='o', label=method)

    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Quick Sort")
    plt.legend()
    plt.grid()
    plt.show()


    # Merge Sort
    execution = {
        "Sorted Array": [],
        "Random Array": [],
        "Negative Array": [],
        "Mixed Array": []
    }

    sortedSmallArray = sorted(random.sample(range(1, 10000), 50))
    randomSmallArray = random.sample(range(1, 10000), 50)
    negativeSmallArray = random.sample(range(-10000, 0), 50)
    mixedSmallArray = random.sample(range(-5000, 5000), 50)

    sortedMediumArray = sorted(random.sample(range(1, 10000), 200))
    randomMediumArray = random.sample(range(1, 10000), 200)
    negativeMediumArray = random.sample(range(-10000, 0), 200)
    mixedMediumArray = random.sample(range(-5000, 5000), 200)

    sortedMediumLargeArray = sorted(random.sample(range(1, 10000), 1000))
    randomMediumLargeArray = random.sample(range(1, 10000), 1000)
    negativeMediumLargeArray = random.sample(range(-10000, 0), 1000)
    mixedMediumLargeArray = random.sample(range(-5000, 5000), 1000)

    sortedLargeArray = sorted(random.sample(range(1, 10000), 5000))
    randomLargeArray = random.sample(range(1, 10000), 5000)
    negativeLargeArray = random.sample(range(-10000, 0), 5000)
    mixedLargeArray = random.sample(range(-5000, 5000), 5000)

    for size, arrays in [
        ("Small", [sortedSmallArray, randomSmallArray, negativeSmallArray, mixedSmallArray]),
        ("Medium", [sortedMediumArray, randomMediumArray, negativeMediumArray, mixedMediumArray]),
        ("Medium Large",
         [sortedMediumLargeArray, randomMediumLargeArray, negativeMediumLargeArray, mixedMediumLargeArray]),
        ("Large", [sortedLargeArray, randomLargeArray, negativeLargeArray, mixedLargeArray])
    ]:
        for key, array in zip(execution.keys(), arrays):
            sortMerge(array, key, execution)

    plt.figure(figsize=(10, 6))
    for method, times in execution.items():
        plt.plot(["Small (50)", "Medium (200)", "Medium Large (1000)", "Large (5000)"], times, marker='o', label=method)

    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Merge Sort")
    plt.legend()
    plt.grid()
    plt.show()


    # Heap Sort
    execution = {
        "Sorted Array": [],
        "Random Array": [],
        "Negative Array": [],
        "Mixed Array": []
    }

    sortedSmallArray = sorted(random.sample(range(1, 10000), 50))
    randomSmallArray = random.sample(range(1, 10000), 50)
    negativeSmallArray = random.sample(range(-10000, 0), 50)
    mixedSmallArray = random.sample(range(-5000, 5000), 50)

    sortedMediumArray = sorted(random.sample(range(1, 10000), 200))
    randomMediumArray = random.sample(range(1, 10000), 200)
    negativeMediumArray = random.sample(range(-10000, 0), 200)
    mixedMediumArray = random.sample(range(-5000, 5000), 200)

    sortedMediumLargeArray = sorted(random.sample(range(1, 10000), 1000))
    randomMediumLargeArray = random.sample(range(1, 10000), 1000)
    negativeMediumLargeArray = random.sample(range(-10000, 0), 1000)
    mixedMediumLargeArray = random.sample(range(-5000, 5000), 1000)

    sortedLargeArray = sorted(random.sample(range(1, 10000), 5000))
    randomLargeArray = random.sample(range(1, 10000), 5000)
    negativeLargeArray = random.sample(range(-10000, 0), 5000)
    mixedLargeArray = random.sample(range(-5000, 5000), 5000)

    for size, arrays in [
        ("Small", [sortedSmallArray, randomSmallArray, negativeSmallArray, mixedSmallArray]),
        ("Medium", [sortedMediumArray, randomMediumArray, negativeMediumArray, mixedMediumArray]),
        ("Medium Large",
         [sortedMediumLargeArray, randomMediumLargeArray, negativeMediumLargeArray, mixedMediumLargeArray]),
        ("Large", [sortedLargeArray, randomLargeArray, negativeLargeArray, mixedLargeArray])
    ]:
        for key, array in zip(execution.keys(), arrays):
            sortHeap(array, key, execution)

    plt.figure(figsize=(10, 6))
    for method, times in execution.items():
        plt.plot(["Small (50)", "Medium (200)", "Medium Large (1000)", "Large (5000)"], times, marker='o', label=method)

    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Heap Sort")
    plt.legend()
    plt.grid()
    plt.show()


    # Heap Sort
    execution = {
        "Sorted Array": [],
        "Random Array": [],
        "Negative Array": [],
        "Mixed Array": []
    }

    sortedSmallArray = sorted(random.sample(range(1, 10000), 50))
    randomSmallArray = random.sample(range(1, 10000), 50)
    negativeSmallArray = random.sample(range(-10000, 0), 50)
    mixedSmallArray = random.sample(range(-5000, 5000), 50)

    sortedMediumArray = sorted(random.sample(range(1, 10000), 200))
    randomMediumArray = random.sample(range(1, 10000), 200)
    negativeMediumArray = random.sample(range(-10000, 0), 200)
    mixedMediumArray = random.sample(range(-5000, 5000), 200)

    sortedMediumLargeArray = sorted(random.sample(range(1, 10000), 1000))
    randomMediumLargeArray = random.sample(range(1, 10000), 1000)
    negativeMediumLargeArray = random.sample(range(-10000, 0), 1000)
    mixedMediumLargeArray = random.sample(range(-5000, 5000), 1000)

    sortedLargeArray = sorted(random.sample(range(1, 10000), 5000))
    randomLargeArray = random.sample(range(1, 10000), 5000)
    negativeLargeArray = random.sample(range(-10000, 0), 5000)
    mixedLargeArray = random.sample(range(-5000, 5000), 5000)

    for size, arrays in [
        ("Small", [sortedSmallArray, randomSmallArray, negativeSmallArray, mixedSmallArray]),
        ("Medium", [sortedMediumArray, randomMediumArray, negativeMediumArray, mixedMediumArray]),
        ("Medium Large",
         [sortedMediumLargeArray, randomMediumLargeArray, negativeMediumLargeArray, mixedMediumLargeArray]),
        ("Large", [sortedLargeArray, randomLargeArray, negativeLargeArray, mixedLargeArray])
    ]:
        for key, array in zip(execution.keys(), arrays):
            sortBucket(array, key, execution)

    plt.figure(figsize=(10, 6))
    for method, times in execution.items():
        plt.plot(["Small (50)", "Medium (200)", "Medium Large (1000)", "Large (5000)"], times, marker='o', label=method)

    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Bucket Sort")
    plt.legend()
    plt.grid()
    plt.show()

    sortedArray = sorted(random.sample(range(1, 10000), 990))
    randomArray = random.sample(range(1, 10000), 990)
    negativeArray = random.sample(range(-10000, 0), 990)
    mixedArray = random.sample(range(-5000, 5000), 990)

    array_types = ["Sorted", "Random", "Negative", "Mixed"]
    arrays = [sortedArray, randomArray, negativeArray, mixedArray]

    execution_times = {
        "Quick Sort": [],
        "Merge Sort": [],
        "Heap Sort": [],
        "Bucket Sort": []
    }

    for arr in arrays:
        arr_copy = arr[:]

        start = time.perf_counter()
        quickSort(arr_copy)
        execution_times["Quick Sort"].append(time.perf_counter() - start)

        arr_copy = arr[:]
        start = time.perf_counter()
        mergeSort(arr_copy)
        execution_times["Merge Sort"].append(time.perf_counter() - start)

        arr_copy = arr[:]
        start = time.perf_counter()
        heapSort(arr_copy)
        execution_times["Heap Sort"].append(time.perf_counter() - start)

        arr_copy = arr[:]
        start = time.perf_counter()
        bucketSort(arr_copy)
        execution_times["Bucket Sort"].append(time.perf_counter() - start)

    plt.figure(figsize=(10, 6))

    for method, times in execution_times.items():
        plt.plot(array_types, times, marker='o', label=method)

    plt.xlabel("Arrays")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Sorting Algorithms Performance Comparison")
    plt.legend()
    plt.grid()
    plt.show()