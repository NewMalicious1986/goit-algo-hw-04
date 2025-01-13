import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

sizes = [10, 100, 1000, 5000]
test_arrays = {size: [random.randint(1, 10000) for _ in range(size)] for size in sizes}

def benchmark_sorting():
    for size, data in test_arrays.items():
        print(f"Array size: {size}")

        insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        print(f"  Insertion sort time: {insertion_time:.6f} seconds")

        merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
        print(f"  Merge sort time: {merge_time:.6f} seconds")

        timsort_time = timeit.timeit(lambda: sorted(data), number=1)
        print(f"  Timsort time: {timsort_time:.6f} seconds")
        print()

benchmark_sorting()