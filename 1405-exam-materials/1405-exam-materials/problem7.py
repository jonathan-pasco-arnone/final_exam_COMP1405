""" Median program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

def coldest_interval(temps, interval_length):
    """ Finds the average of the coldest interval of temperatures """
    coldest_average = None
    average = 0
    for index, temperature in enumerate(temps):
        if index >= interval_length:
            # Replaces the first value of the average with the latest value
            # This is done by first multiplying the average by the interval length
            # This changes it back to just the sums
            # Then we subtract the first value from the sum and add the new one
            # Finaly we divide by the interval length again to get the new average
            average = (average * interval_length - temps[index - interval_length]
                  + temps[index]) / interval_length
            if average < coldest_average:
                coldest_average = average

        # Keep adding values until the first average is calculated
        else:
            average += temperature

        # Calculate the first average
        # Which would be every number from the 0th index to the interval - 1 index
        if index == interval_length - 1:
            average = average / interval_length
            coldest_average = average

    return coldest_average
