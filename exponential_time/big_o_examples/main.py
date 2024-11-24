# O(n) - Linear
# as the number of items increases so will the time it takes to finish, in a Linear Time
def get_products(nums):
    if len(nums) == 0:
        return 0
    product = 1
    for num in nums:
        prdouct *= num
    return product

# O(1) - Constant
# when using a constant time the size doesn't matter it will always be the same time.
def get_first_num(nums):
    if len(nums) == 0:
        return None
    return nums[0]

# O(n^2)- Squared
# Input Example: [1,2,3]
# Output Example: [1,2,3, 2,4,6, 3,6,9]
# Time Complexity: O(n²) - The function uses two nested loops, iterating over the input list twice,
# resulting in a quadratic growth of operations as the input size increases.
# Space Complexity: O(n²) - The output list grows quadratically as it stores all pairwise products.
def get_product_combos(nums):
    combos = []
    for num in nums:
        for second_num in nums:
            combos.append(num * second_num)
    return combos