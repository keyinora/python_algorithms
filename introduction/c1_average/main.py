def average_followers(nums):
    average = 0
    if len(nums) == 0:
        return None
    for num in nums:
        average += num
    return average / len(nums)
