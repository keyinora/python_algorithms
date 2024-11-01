def median_followers(nums):
    if len(nums) == 0:
        return None
    nums = sorted(nums)
    n = len(nums)
    mid = n // 2
    if n % 2 == 1:
        return nums[mid]
    else:
        return (nums[mid - 1] + nums[mid]) / 2
