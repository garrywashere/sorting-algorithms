# Made with ❤️ by Garry
# 24/01/24

import random, time

data = [1,2,3,4,5,6,7,8,9,0] # Define our data set
random.shuffle(data) # Shuffle the data

print("Our unsorted data:", str(data)) # Print our original unsorted/shuffled data

start = time.time()

def quickSort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high) # Find the partition index

        # Recursively sort the subarrays on both sides of the partition
        quickSort(arr, low, partition_index - 1)
        quickSort(arr, partition_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choose the rightmost element as the pivot
    i = low - 1  # Index of the smaller element
    
    for j in range(low, high): # Iterate through the array and rearrange elements
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place the pivot element in its correct position

    return i + 1


quickSort(data, 0, len(data)-1)

end = time.time()

print("\nSorted data:", str(data))
print("Time taken:", str(end-start)+"s")