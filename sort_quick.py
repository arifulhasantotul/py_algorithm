def quick_sort(arr):
    if len(arr) < 1:
        return arr
    else:
        pivot_value = arr.pop()

        lower_items = []
        greater_items = []

        for item in arr:
            if item > pivot_value:
                greater_items.append(item)
            else:
                lower_items.append(item)

        return quick_sort(lower_items) + [pivot_value] + quick_sort(greater_items)


nums = [0, 9, 3, 8, 2, 7]
result = quick_sort(nums)
print(result)
