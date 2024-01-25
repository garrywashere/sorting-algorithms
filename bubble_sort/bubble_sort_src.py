# Made with ❤️ by Garry
# 22/01/24

def sort(array):
    lengthOfData = len(array) # Determine the length of our array (Data)

    for _pass in range(lengthOfData): # Iterate through our array, these will be our "passes"

        for value in range(lengthOfData-_pass-1): # Iterate through the unsorted portion of the array, excluding the last _pass elements as they are already sorted.

            if array[value] > array[value+1]: # Compare two values and if the first one is larger than the second:
                array[value], array[value+1] = array[value+1], array[value] # Swap the first and second values

            else: # If the first value is not larger than the second value:
                pass # Do nothing

    return array

if __name__ == "__main__":
    import random, time

    data = [1,2,3,4,5,6,7,8,9,0] # Define our data set
    random.shuffle(data) # Shuffle the data

    print("Our unsorted data:", str(data)) # Print our original unsorted/shuffled data

    start = time.time()

    sorted = sort(data)

    end = time.time()

    print("\nOur sorted data:", str(data)) # Print out the final sorted data
    print("Time taken:", str(end-start))