def merge_sort(nums):
    # Base case: If the list has 1 or no elements, it's already sorted
    if len(nums) <= 1:
        return nums
    
    # Find the midpoint and split the list into two halves
    mid = len(nums) // 2
    sorted_left_side = merge_sort(nums[:mid])
    sorted_right_side = merge_sort(nums[mid:])
    
    # Merge the sorted halves
    return merge(sorted_left_side, sorted_right_side)


def merge(first, second):
    final = []
    i = 0
    j = 0
    
    # Continue until one of the halves is exhausted
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    
    # Append any remaining elements
    final.extend(first[i:])
    final.extend(second[j:])
    
    return final
