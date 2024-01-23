# Made with ❤️ by Garry
# 23/01/24

import random, time

data = [1,2,3,4,5,6,7,8,9,0] # Define our data set
random.shuffle(data) # Shuffle the data

print("Our unsorted data:", str(data)) # Print our original unsorted/shuffled data

start = time.time()

def insertionSort(arr):
    for i in range(1, len(arr)): # Iterate through the array
        key = arr[i]  # Current element to be compared

        j = i - 1
        while j >= 0 and key < arr[j]: # Move elements of arr[0:i-1] that are greater than key to one position ahead of their current position
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key # Place the current element at its correct position

insertionSort(data)

end = time.time()

print("\nSorted data:", str(data))
print("Time taken:", str(end-start)+"s")