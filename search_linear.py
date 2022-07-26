# linear search
def linear_search(arr, match_item):
    for i in range(0, len(arr)):
        if arr[i] == match_item:
            return f"Item available at index {i} value {arr[i]}"

    else:
        return f"Not found item {match_item}!"


result = linear_search([1, 5, 6, 4, 8, 9, 1, 2, 3], 3)


def multiple_linear_search(arr, match_item):
    matched_arr = []
    for i in range(0, len(arr)):
        if arr[i] == match_item:
            matched_arr.append(i)

    if len(matched_arr) > 0:
        return f"value matched at index {matched_arr} value {match_item}"
    else:
        return f"Not found item {match_item}!"


# result = multiple_linear_search([1, 5, 6, 4, 8, 9, 1, 2, 3], 10)
print(result)
