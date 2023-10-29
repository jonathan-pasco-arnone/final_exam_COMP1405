""" Median program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

def median_word_length(link):
    """ Finds the median length of the words of a file """
    file = open(link, "r", encoding="utf8")
    contents = (file.read()).split()

    # Bubble Sorting
    swaped = True
    while swaped:
        swaped = False
        for index in range(1, len(contents) - 1):
            if len(contents[index - 1]) > len(contents[index]):
                swap_item = contents[index]
                contents[index] = contents[index - 1]
                contents[index - 1] = swap_item
                swaped = True

    median_length = ((len(contents[int(len(contents) / 2)])
          + len(contents[int(len(contents) / 2 - 0.5)])) / 2)
    return median_length
