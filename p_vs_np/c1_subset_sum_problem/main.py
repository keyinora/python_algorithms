def subset_sum(nums, target):
    # Start the helper function with the last index
    return find_subset_sum(nums, target, len(nums) - 1)

def find_subset_sum(nums, target, index):
    # Base case: If the target is 0, we found a subset that adds up to the target
    if target == 0:
        return True
    # If the index is less than 0 and the target is not 0, no subset was found
    if index < 0 and target != 0:
        return False
    # If the current element is greater than the target, skip it
    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    # Recursive cases: 
    # 1. Exclude the current element
    exclude = find_subset_sum(nums, target, index - 1)
    # 2. Include the current element and reduce the target
    include = find_subset_sum(nums, target - nums[index], index - 1)
    # If either recursive call returns True, we found a subset
    return exclude or include
