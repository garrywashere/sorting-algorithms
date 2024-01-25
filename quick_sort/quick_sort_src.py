# Made with ❤️ by Garry
# 24/01/24

import sys

sys.setrecursionlimit(1000000)

def sort(array, low, high):
    if low < high:
        partition_index = partition(array, low, high) # Find the partition index

        # Recursively sort the subarrays on both sides of the partition
        sort(array, low, partition_index - 1)
        sort(array, partition_index + 1, high)

def partition(array, low, high):
    pivot = array[high]  # Choose the rightmost element as the pivot
    i = low - 1  # Index of the smaller element
    
    for j in range(low, high): # Iterate through the array and rearrange elements
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]  # Place the pivot element in its correct position

    return i + 1

if __name__ == "__main__":
    import random, time

    data = [1,2,3,4,5,6,7,8,9,0] # Define our data set
    random.shuffle(data) # Shuffle the data

    print("Our unsorted data:", str(data)) # Print our original unsorted/shuffled data

    start = time.time()

    sorted = sort(data, 0, len(data)-1)

    end = time.time()

    print("\nOur sorted data:", str(data)) # Print out the final sorted data
    print("Time taken:", str(end-start))