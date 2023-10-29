""" Median program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

FILE_PATH = "1405-exam-materials/"

def median_word_length(filename):
    """ Finds the median length of the words of a file """
    file = open(FILE_PATH + filename, "r", encoding="utf8")
    contents = (file.read()).split()

    # Bubble Sorting
    swapped = True
    while swapped:
        swapped = False
        for index in range(1, len(contents)):
            if len(contents[index - 1]) > len(contents[index]):
                swap_item = contents[index]
                contents[index] = contents[index - 1]
                contents[index - 1] = swap_item
                swapped = True

    # Calculates the median length of the middle number and the number 0.5 index's below
    # Both indexs are rounded down to account for both even and odd quantities
    median_length = ((len(contents[int(len(contents) / 2)])
          + len(contents[int(len(contents) / 2 - 0.5)])) / 2)

    return median_length
