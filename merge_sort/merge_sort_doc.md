# Merge Sort Step-by-Step Explanation

## Objective
The objective of the merge sort algorithm is to sort an array in ascending order by recursively dividing the array into halves, sorting each half, and merging them back together.

## Steps

### 1. Initialization
- Start with the entire unsorted array.
- Define a function to perform the merge operation.

### 2. Recursive Divide
- Recursively divide the array into halves until each subarray contains only one element.

### 3. Merge
- Merge the divided subarrays in a sorted manner.
  - Compare the elements of the two subarrays and merge them into a new sorted subarray.

### 4. Repeat
- Repeat steps 2-3 until the entire array is merged and sorted.

### 5. Exit Recursion
- Once the recursion reaches subarrays with one element, start merging them back up the recursive call stack.

### 6. Final Merge
- The final merge operation combines the two halves of the array into a fully sorted array.

## Example
Suppose we have an unsorted array `arr = [12, 8, 5, 23, 16, 38, 2, 50, 42]`.

- Initial array: `[12, 8, 5, 23, 16, 38, 2, 50, 42]`.
- Recursive divide:
  - Split into two halves: `[12, 8, 5, 23]` and `[16, 38, 2, 50, 42]`.
  - Further split: `[12, 8]`, `[5, 23]`, `[16, 38]`, `[2, 50, 42]`.
  - Continue until each subarray contains only one element.
- Merge:
  - Merge `[12, 8]` into `[8, 12]`.
  - Merge `[5, 23]` into `[5, 23]`.
  - Merge `[16, 38]` into `[16, 38]`.
  - Merge `[2, 50, 42]` into `[2, 42, 50]`.
- Final merges:
  - Merge `[8, 12]` and `[5, 23]` into `[5, 8, 12, 23]`.
  - Merge `[16, 38]` and `[2, 42, 50]` into `[2, 16, 38, 42, 50]`.
  - Merge the two sorted halves into the fully sorted array: `[2, 5, 8, 12, 16, 23, 38, 42, 50]`.