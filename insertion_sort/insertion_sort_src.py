# Made with ❤️ by Garry
# 23/01/24


def sort(array):
    for i in range(1, len(array)):  # Iterate through the array
        key = array[i]  # Current element to be compared

        j = i - 1
        while (
            j >= 0 and key < array[j]
        ):  # Move elements of array[0:i-1] that are greater than key to one position ahead of their current position
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key  # Place the current element at its correct position


if __name__ == "__main__":
    import random, time

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # Define our data set
    random.shuffle(data)  # Shuffle the data

    print("Our unsorted data:", str(data))  # Print our original unsorted/shuffled data

    start = time.time()

    sorted = sort(data)

    end = time.time()

    print("\nOur sorted data:", str(data))  # Print out the final sorted data
    print("Time taken:", str(end - start))
