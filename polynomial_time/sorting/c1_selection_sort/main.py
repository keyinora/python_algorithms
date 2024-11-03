def selection_sort(nums):
    # Iterate through each index in the list
    for i in range(len(nums)):
        # Assume the smallest element is at the current index
        smallest_idx = i
        # Check the rest of the list to find the smallest element
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        # Swap the current element with the smallest element found
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    # Return the sorted list
    return nums
