def binary_search(target, arr):
    # Initialize the low and high pointers.
    # 'low' starts at the beginning of the array (index 0).
    # 'high' starts at the last index of the array (len(arr) - 1).
    low = 0
    high = len(arr) - 1
    
    # Continue searching as long as the range [low, high] is valid.
    while low <= high:
        # Calculate the median index of the current range.
        # Use integer division (//) to ensure the result is an integer.
        median = (low + high) // 2
        
        # Check if the middle element matches the target.
        if arr[median] == target:
            return True  # Target is found; return True.
        
        # If the middle element is less than the target, discard the left half.
        # This is done by moving the 'low' pointer to 'median + 1'.
        elif arr[median] < target:
            low = median + 1
        
        # If the middle element is greater than the target, discard the right half.
        # This is done by moving the 'high' pointer to 'median - 1'.
        else:
            high = median - 1
    
    # If the loop exits without finding the target, return False.
    return False
