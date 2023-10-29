""" Median program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

FILE_PATH = "1405-exam-materials/"

def sort_volumes(filename):
    """ Sorts all the volumes by ID """
    file = open(FILE_PATH + filename, "r", encoding="utf8")
    contents = file.readlines()

    volume_order = []
    id_order = []

    # The first id is on line 0
    id_counter = 0
    while id_counter != len(contents):
        # Calculate the volume
        volume_order.append(int(contents[id_counter + 1]) * int(contents[id_counter + 2])
              * int(contents[id_counter + 3]))
        id_order.append(int(contents[id_counter]))

        # IDs iterate every 4 lines
        id_counter += 4

    # Bubble Sorting
    swapped = True
    while swapped:
        swapped = False
        index = len(volume_order) - 1
        while index != 0:
            if volume_order[index - 1] < volume_order[index]:
                # Swap the volumes
                swap_volume = volume_order[index]
                volume_order[index] = volume_order[index - 1]
                volume_order[index - 1] = swap_volume

                # Swap the IDs
                swap_id = id_order[index]
                id_order[index] = id_order[index - 1]
                id_order[index - 1] = swap_id

                swapped = True
            index -= 1

    return id_order
