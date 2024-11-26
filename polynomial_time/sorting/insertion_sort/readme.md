
# Insertion Sort Implementation

## Overview
Insertion Sort is a simple sorting algorithm that builds the final sorted list one element at a time. While it is less efficient than algorithms like merge sort or quicksort for large datasets (**O(n²)** in worst-case time complexity), it is more efficient for smaller datasets due to its low overhead.

This implementation is used to sort a list of affiliate deals by revenue, as influencers typically have only a few hundred deals, making insertion sort a practical and memory-efficient choice.

---

## Code

### Implementation
```python
def insertion_sort(nums):
    for i, value in enumerate(nums):  # Iterate through the list with indices and values
        j = i  # Start with the current index
        while j > 0 and nums[j - 1] > nums[j]:  # Compare with the previous elements
            nums[j], nums[j - 1] = nums[j - 1], nums[j]  # Swap elements if out of order
            j -= 1  # Move one step back
    return nums  # Return the sorted list
```

---

## How It Works

1. **Outer Loop**: The loop `for i, value in enumerate(nums)` iterates through the entire list, with `i` representing the current index and `value` the current element.
2. **Inner Loop**:
   - For each index `i`, the variable `j` starts at `i`.
   - The `while` loop checks if `j > 0` (to ensure we don't go out of bounds) and if the previous element (`nums[j-1]`) is greater than the current element (`nums[j]`).
   - If the condition is true, the two elements are swapped, and `j` is decremented to compare the current element with the previous elements.
3. **Sorting Process**:
   - The algorithm repeatedly moves smaller elements to the left until they are in the correct position.
   - Larger elements are shifted to the right to make room.

---

## Example Execution

### Input:
```python
nums = [5, 3, 8, 6, 2]
sorted_nums = insertion_sort(nums)
print(sorted_nums)
```

### Execution Steps:
1. Start with `[5, 3, 8, 6, 2]`.
2. Compare `5` and `3`, swap them: `[3, 5, 8, 6, 2]`.
3. Move to `8`, no change: `[3, 5, 8, 6, 2]`.
4. Compare `8` and `6`, swap them: `[3, 5, 6, 8, 2]`.
5. Compare `8` and `2`, swap them repeatedly until `2` is in the correct position: `[2, 3, 5, 6, 8]`.

### Output:
```python
[2, 3, 5, 6, 8]
```

---

## Time Complexity
- **Best Case**: **O(n)** (the list is already sorted).
- **Worst Case**: **O(n²)** (the list is sorted in reverse order).
- **Average Case**: **O(n²)**.

## Space Complexity
- **O(1)**: The algorithm sorts the list in place and uses no extra memory.

---

## Interview Explanation
When discussing this implementation in an interview:
1. **Highlight Simplicity**: Explain how insertion sort works by moving elements one at a time to their correct position.
2. **Small Input Optimization**: Emphasize its efficiency for small datasets and how it uses less memory compared to divide-and-conquer algorithms.
3. **Real-world Use**: Mention scenarios like sorting small datasets or partially sorted lists.
4. **Edge Cases**: Point out it handles empty lists (`[]`) and single-element lists (`[x]`) gracefully.

---

## Final Thoughts
Insertion sort may not be suitable for large datasets due to its **O(n²)** time complexity, but for small or nearly sorted datasets, it can be an effective and memory-efficient choice. This makes it a great candidate for specific use cases like sorting affiliate deals.

