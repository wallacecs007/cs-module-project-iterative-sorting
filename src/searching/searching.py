def linear_search(arr, target):
    # Your code here
    for num in range(0, len(arr)):
        if arr[num] == target:
            return num

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = (len(arr) - 1)

    while end >= start:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        else:
            if target < arr[mid]:
                end = mid - 1
            if target > arr[mid]:
                start = mid + 1

    return -1  # not found
