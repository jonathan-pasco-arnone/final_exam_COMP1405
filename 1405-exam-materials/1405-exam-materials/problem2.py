""" Counting letters program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

def count(list1, list2):
    """ Determines the amount of times a list appears in another list """
    total = 0

    for index in range(len(list1)):
        # If there are not enough elements left for list2 to check
        if index + len(list2) > len(list1):
            break

        check = False
        for counter, value in enumerate(list2):
            # If it has failed
            if list1[index + counter] != value:
                break
            # If at end of list and every character has matched
            if counter == len(list2) - 1:
                check = True
        if check:
            total += 1
    return total
