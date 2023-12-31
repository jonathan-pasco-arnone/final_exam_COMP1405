""" Median program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

value_quantities = {}

def process(alist):
    """ Processes a dictionary from the list to be used in the within range function """
    value_quantities.clear()
    # Adds each key and value to the dictionary
    for value in alist:
        if value_quantities.get(value) is None:
            value_quantities[value] = 1
        else:
            value_quantities[value] += 1

def within_range(a, b):
    """ Finds the number of values within a given range of the previously computed list """
    total_values = 0
    counter = a
    # Adds each dictionary value individually
    while counter <= b:
        if value_quantities.get(counter) is not None:
            total_values += value_quantities[counter]
        counter += 1
    return total_values
