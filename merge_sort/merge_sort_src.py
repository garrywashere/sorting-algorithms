# Made with ❤️ by Garry
# 23/01/24


def sort(array):
    if len(array) > 1:  # Check that there are more than 1 elements in the array
        middle = (
            len(array) // 2
        )  # Take an integer divison of the number of elements in the array to determine the middle
        leftHalf = array[:middle]  # Split the array for left only
        rightHalf = array[middle:]  # Split the array for right only

        sort(leftHalf)  # Run routine recursively for the left half
        sort(rightHalf)  # Run routine recursively for the right half

        merge(array, leftHalf, rightHalf)  # Run the merge function


def merge(array, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):  # Compare and merge values within the array
        if left[i] < right[j]:  # Swap values if one is bigger than the other
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):  # Merge the left part of the array
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):  # Merge the right part of the array
        array[k] = right[j]
        j += 1
        k += 1


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
