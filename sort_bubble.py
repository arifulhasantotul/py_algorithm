def bubble_sort(arr):
    # range(startIndex, lastIndex, iterationOrder)
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                # arr[i + 1], arr[i] = arr[i], arr[i + 1]
        # print(arr)


nums = [5, 2, 6, 3, 4]
bubble_sort(nums)
print(nums)
