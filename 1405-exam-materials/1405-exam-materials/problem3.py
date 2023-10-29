""" Probability information program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

observations = {}
total = 0

def observe(number):
    """ Observes a number one time """
    if observations.get(number) is None:
        observations[number] = 1
    else:
        observations[number] += 1

    # Accesses the global variable "total"
    global total
    total += 1

def probability_of(number):
    """ Determines the probability of a number in the total observations so far """
    if observations.get(number) is None or total == 0:
        return 0
    return observations[number] / total

def reset():
    """ Resets the observations and total """
    # Accesses the global variable "total"
    global total
    total = 0
    observations.clear()
