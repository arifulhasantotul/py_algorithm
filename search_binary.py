# binary search

def binary_search(arr, match_item):
    left = 0
    right = len(arr) - 1
    for i in range(0, len(arr)):
        mid = (left + right) // 2
        if arr[mid] != match_item:
            if arr[mid] > match_item:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return f"Item {match_item} matched at index {mid}"
    else:
        return f"Item {match_item} not found!"


# result = binary_search([1, 4, 5, 6, 8, 9, 11, 22, 33], 14)

"""
To do binary search given array/list must be sorted
"""


def single_binary_search(arr, match_item):
    left_idx = 0
    right_idx = len(arr) - 1
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if arr[mid_idx] != match_item:
            if arr[mid_idx] > match_item:
                right_idx = mid_idx - 1
            else:
                left_idx = mid_idx + 1
        else:
            return f"Item {match_item} matched at index {mid_idx}"
    else:
        return f"Item {match_item} not found!"


# result = single_binary_search([1, 4, 5, 6, 6, 8, 9, 11, 22, 33], 6)


def multiple_binary_search(arr, match_item):
    l_idx = 0
    r_idx = len(arr) - 1
    matched_arr = []
    for i in range(0, len(arr)):
        m_idx = (l_idx + r_idx) // 2
        if arr[m_idx] != match_item:
            if arr[m_idx] > match_item:
                r_idx = m_idx - 1
            else:
                l_idx = m_idx + 1
        else:
            matched_arr.append(m_idx)

    if len(matched_arr) > 0:
        return f"Item {match_item} found at index {matched_arr}"
    else:
        return f"Item {match_item} not found!"


result = multiple_binary_search([1, 4, 5, 6, 6, 8, 9, 11, 22, 33], 33)
print(result)
