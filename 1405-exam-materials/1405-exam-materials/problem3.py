""" Probability information program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

observations = {}

def observe(number):
    """ Observes a number one time """
    # Adds the new number or adds 1 to the existing number
    if observations.get(number) is None:
        observations[number] = 1
    else:
        observations[number] += 1

    # Adds to the total number of observations
    if observations.get("total") is None:
        observations["total"] = 1
    else:
        observations["total"] += 1

def probability_of(number):
    """ Determines the probability of a number in the total observations so far """
    if observations.get(number) is None or observations["total"] == 0:
        return 0
    return observations[number] / observations["total"]

def reset():
    """ Resets the observations and total """
    observations.clear()
