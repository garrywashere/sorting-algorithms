# Quick Sort Step-by-Step Explanation

## Objective

The objective of the quicksort algorithm is to sort an array in ascending order by selecting a pivot element, partitioning the array into two subarrays based on the pivot, and recursively applying the same process to the subarrays.

## Steps

### 1. Initialization

-   Select a pivot element from the array.
-   Partition the array into two subarrays: elements less than the pivot and elements greater than the pivot.

### 2. Recursive Quick Sort

-   Recursively apply quicksort to the two subarrays.
    -   Select pivots for each subarray and partition them.
    -   Continue this process until each subarray has one or zero elements.

### 3. Combine

-   As the recursion unwinds, combine the sorted subarrays to produce the fully sorted array.

## Example

Suppose we have an unsorted array `arr = [12, 8, 5, 23, 16, 38, 2, 50, 42]`.

-   Initial array: `[12, 8, 5, 23, 16, 38, 2, 50, 42]`.
-   Choose a pivot, say `16`.
-   Partition the array: `[12, 8, 5, 2]`, `16`, `[23, 38, 50, 42]`.
-   Recursive quicksort on the two subarrays:
    -   Subarray `[12, 8, 5, 2]`:
        -   Choose pivot `5`.
        -   Partition: `[2]`, `5`, `[8, 12]`.
    -   Subarray `[23, 38, 50, 42]`:
        -   Choose pivot `42`.
        -   Partition: `[23, 38]`, `42`, `[50]`.
-   Combine the sorted subarrays:
    -   Combine `[2]`, `5`, `[8, 12]` to form `[2, 5, 8, 12]`.
    -   Combine `[23, 38]`, `42`, `[50]` to form `[23, 38, 42, 50]`.
-   Combine the entire array: `[2, 5, 8, 12, 16, 23, 38, 42, 50]`.
