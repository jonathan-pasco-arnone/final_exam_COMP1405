""" Box counting program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

def box_weight(box):
    """ Determines the total number of all values, regardless of how many lists they are in """
    total_weight = 0
    for item in box:
        if isinstance(item, list):
            # Recursively go through each list to determine each value
            total_weight += box_weight(item)
        else:
            total_weight += item
    return total_weight
