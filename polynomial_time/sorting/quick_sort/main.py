def quick_sort(nums, low, high):
    # If low is less than high, proceed with partitioning
    if low < high:
        # Partition the list and get the pivot index
        pivot_index = partition(nums, low, high)
        # Recursively apply quick_sort to the left of the pivot
        quick_sort(nums, low, pivot_index - 1)
        # Recursively apply quick_sort to the right of the pivot
        quick_sort(nums, pivot_index + 1, high)
        


def partition(nums, low, high):
    # Set pivot to the element at index high
    pivot = nums[high]
    i = low  # Pointer for the smaller element
    # Loop through the list from low to high-1
    for j in range(low, high):
        # If the current element is less than the pivot
        if nums[j] < pivot:
            # Swap elements at indices i and j
            nums[i], nums[j] = nums[j], nums[i]
            i += 1  # Move i to the right
    # Swap the pivot element with the element at index i
    nums[i], nums[high] = nums[high], nums[i]
    # Return the pivot index
    return i
