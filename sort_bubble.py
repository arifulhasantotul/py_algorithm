def bubble_sort(arr):
    for i in range(len(arr)):
        index_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index_min]:
                index_min = j

        if index_min != i:
            temp = arr[i]
            arr[i] = arr[index_min]
            arr[index_min] = temp


nums = [5, 2, 6, 3, 4]
bubble_sort(nums)
print(nums)
