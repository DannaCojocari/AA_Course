def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


def bucketSort(arr):
    if len(arr) == 0:
        return

    min_val, max_val = min(arr), max(arr)
    n = len(arr)

    if min_val == max_val:
        return

    bucket_range = (max_val - min_val) / n
    buckets = [[] for _ in range(n)]

    for num in arr:
        bi = int((num - min_val) / bucket_range)
        if bi == n:
            bi -= 1
        buckets[bi].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1
