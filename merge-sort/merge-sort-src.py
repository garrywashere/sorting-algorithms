# Made with ❤️ by Garry
# 23/01/24

import random, time

data = [1,2,3,4,5,6,7,8,9,0] # Define our data set
random.shuffle(data) # Shuffle the data

print("Our unsorted data:", str(data)) # Print our original unsorted/shuffled data

start = time.time()

def mergeSort(arr):
    if len(arr) > 1: # Check that there are more than 1 elements in the array
        middle = len(arr) // 2 # Take an integer divison of the number of elements in the array to determine the middle
        leftHalf = arr[:middle] # Split the array for left only
        rightHalf = arr[middle:] # Split the array for right only

        mergeSort(leftHalf) # Run routine recursively for the left half
        mergeSort(rightHalf) # Run routine recursively for the right half

        merge(arr, leftHalf, rightHalf) # Run the merge function

def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right): # Compare and merge values within the array
        if left[i] < right[j]: # Swap values if one is bigger than the other
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left): # Merge the left part of the array
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right): # Merge the right part of the array
        arr[k] = right[j]
        j += 1
        k += 1

mergeSort(data)

end = time.time()

print("\nSorted data:", str(data)) # Print out the final sorted data
print("Time taken:", str(end-start)+"s")