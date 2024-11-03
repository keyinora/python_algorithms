def insertion_sort(arr):
    # Iterate through each index in the list
    for i in range(1, len(arr)):
        j = i
        # While j is greater than 0 and the previous element is greater than the current element
        while j > 0 and arr[j - 1] > arr[j]:
            # Swap elements at j and j-1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            # Move one position to the left
            j -= 1
    # Return the sorted list
    return arr
