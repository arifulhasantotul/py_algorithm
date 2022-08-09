def insertion_sort(arr):
    for i in range(1, len(arr)):
        while arr[i - 1] > arr[i] and i > 0:
            # temp = arr[i]
            # arr[i] = arr[i - 1]
            # arr[i - 1] = temp
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i = i - 1
        return arr


nums = [5, 2, 6, 3, 4]
result = insertion_sort(nums)
print(result)
