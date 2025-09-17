# Made with ❤️ by Garry
# 25/01/24

import random, time

from bubble_sort import bubble_sort_src
from merge_sort import merge_sort_src
from insertion_sort import insertion_sort_src
from quick_sort import quick_sort_src


def define():
    arraySize = int(input("How large would you like the array? "))
    array = []

    for x in range(arraySize):
        array.append(x + 1)

    random.shuffle(array)
    return array


def bubble(array):
    start = time.time()

    bubble_sort_src.sort(array)

    end = time.time()
    timeTaken = end - start

    return timeTaken


def merge(array):
    start = time.time()

    merge_sort_src.sort(array)

    end = time.time()
    timeTaken = end - start

    return timeTaken


def insertion(array):
    start = time.time()

    insertion_sort_src.sort(array)

    end = time.time()
    timeTaken = end - start

    return timeTaken


def quick(array):
    start = time.time()

    quick_sort_src.sort(array, 0, len(array) - 1)

    end = time.time()
    timeTaken = end - start

    return timeTaken


if __name__ == "__main__":
    array = define()

    print("\nBubble Sort:", str(bubble(array)))
    print("\nMerge Sort:", str(merge(array)))
    print("\nInsertion Sort:", str(insertion(array)))
    print("\nQuick Sort:", str(quick(array)))
    print("")
