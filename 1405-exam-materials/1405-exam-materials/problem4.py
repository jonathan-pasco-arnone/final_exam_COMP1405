""" Autoshow program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

FILE_PATH = "1405-exam-materials/"

def most_common_color(filename):
    """ Finds the most common color of the cars in a given file """
    file = open(FILE_PATH + filename, "r", encoding="utf8")
    contents = file.readlines()

    colors = {}
    common_color = ""

    # The first color is on line 3
    color_counter = 3
    # Record all the frequencies of the colors
    while color_counter < len(contents):
        current_color = contents[color_counter].strip()
        if colors.get(current_color) is None:
            colors[current_color] = 1
        else:
            colors[current_color] += 1

        # This is just to make sure that a color from the set will be recorded for later
        common_color = current_color

        # Each color is 5 lines apart
        color_counter += 5

    # Check which color has the most occurances
    for key, value in colors.items():
        if value > colors[common_color]:
            common_color = key
    return common_color

def sorted_prices(filename):
    """ Finds the prices of all the cars for sale """
    file = open(FILE_PATH + filename, "r", encoding="utf8")
    contents = file.readlines()

    prices = []

    # The first price is on line 4
    price_counter = 4
    while price_counter != len(contents) - 2:
        # If the car is for sale
        if contents[price_counter + 1] == "true\n":
            prices.append(contents[price_counter].strip())
        price_counter += 5

    # Bubble sorting to with some minor changes to make it go from largest -> smallest
    swapped = True
    while swapped:
        swapped = False
        index = len(prices) - 1
        while index != 0:
            if prices[index - 1] < prices[index]:
                swapped_value = prices[index]
                prices[index] = prices[index - 1]
                prices[index - 1] = swapped_value
                swapped = True
            index -= 1

    return prices
