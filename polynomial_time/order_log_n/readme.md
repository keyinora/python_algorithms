# Binary Search Implementation in Python

## Overview

This script implements the **binary search** algorithm, an efficient method to search for a target element in a sorted array. The key idea of binary search is to repeatedly divide the search range in half until the target is found or the range becomes invalid.

---

## Function: `binary_search`

### Code:
```python
def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False
```

---

## Explanation

### 1. **Initialization**
We define two pointers:
- `low` starts at the beginning of the array (`0`).
- `high` starts at the last index of the array (`len(arr) - 1`).

These pointers represent the current range of indices being searched.

---

### 2. **The While Loop**
The loop runs as long as `low <= high`, meaning there is still a valid range to search.

---

### 3. **Calculate the Median**
The median index of the current range is calculated as:

```python
median = (low + high) // 2
```

This divides the range into two halves. Integer division ensures the result is an integer.

---

### 4. **Comparison Logic**
We compare the value at the median index, `arr[median]`, with the target:
- If `arr[median] == target`, we return `True` (the target is found).
- If `arr[median] < target`, the target must be in the right half, so we set:

```python
low = median + 1
```

- If `arr[median] > target`, the target must be in the left half, so we set:

```python
high = median - 1
```

---

### 5. **Exit Condition**
If `low` becomes greater than `high`, the loop ends. This means the target is not in the array, and the function returns `False`.

---

## Complexity Analysis

- **Time Complexity**:  
  O(log n) — The search range is halved in each iteration, resulting in logarithmic growth with respect to the array size.

- **Space Complexity**:  
  O(1) — The function uses only a few variables (`low`, `high`, `median`) and no additional data structures.

---

## Edge Cases

1. **Empty Array**:  
   If the array is empty (`arr = []`), `high = -1`, and the loop doesn't run. The function correctly returns `False`.

2. **Single Element**:  
   For arrays with one element (`arr = [target]` or `arr = [other]`), the function checks the single element and returns the appropriate result.

3. **Target Not in Array**:  
   If the target is not present, the loop narrows the range to an invalid state, and the function returns `False` as expected.

---

## Example Usage

```python
arr = [1, 3, 5, 7, 9]
print(binary_search(5, arr))  # Output: True
print(binary_search(2, arr))  # Output: False
```

---

## Summary

This binary search implementation is a classic example of the **divide-and-conquer** paradigm. It efficiently finds a target element in a sorted array, with optimal time and space complexity. The algorithm is robust and handles edge cases like empty arrays or single-element arrays gracefully.
