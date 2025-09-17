# Insertion Sort Step-by-Step Explanation

## Objective

The objective of the insertion sort algorithm is to sort an array in ascending order by iteratively building a sorted portion of the array.

## Steps

### 1. Initialization

-   Start with the second element of the array (index 1).
-   Define a variable `n` to represent the length of the array.

### 2. Outer Loop

-   Start an outer loop that iterates from the second element to the last element of the array.

### 3. Inner Loop

-   Within the outer loop, start an inner loop that iterates backward from the current element to the beginning of the sorted portion of the array.
-   Compare each element with its adjacent predecessor.
    -   If the element is smaller, swap it with the predecessor.

### 4. Build the Sorted Portion

-   After each pass of the inner loop, the sorted portion of the array is extended by one element.

### 5. Repeat

-   Repeat steps 2-4 until the entire array is sorted.

### 6. Exit Outer Loop

-   Once the outer loop completes, the array is sorted.

## Example

Suppose we have an unsorted array `arr = [12, 8, 5, 23, 16, 38, 2, 50, 42]`.

-   Initial array: `[12, 8, 5, 23, 16, 38, 2, 50, 42]`.
-   First pass (start with index 1):
    -   Compare and swap elements: `[8, 12, 5, 23, 16, 38, 2, 50, 42]`.
-   Second pass (start with index 2):
    -   Compare and swap: `[5, 8, 12, 23, 16, 38, 2, 50, 42]`.
-   Repeat until the entire array is sorted.

Sorted array: `[2, 5, 8, 12, 16, 23, 38, 42, 50]`.
