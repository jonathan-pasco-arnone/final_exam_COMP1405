""" Median program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

FILE_PATH = "1405-exam-materials/"

def find_largest_distance(filename):
    """ Finds the largest distance between two cities """
    file = open(FILE_PATH + filename, "r", encoding="utf8")
    contents = file.readlines()

    largest_distance = 0
    city_num = 0
    # Iterates through the cities
    while city_num <= len(contents) - 3:
        second_city_num = city_num + 3
        # Iterates through the cities not including the current city, or any
        # previous ones, in the outter while loop
        while second_city_num <= len(contents) - 3:
            distance = (abs(int(contents[city_num + 1]) - int(contents[second_city_num + 1]))
                  + abs(int(contents[city_num + 2]) - int(contents[second_city_num + 2])))
            if distance > largest_distance:
                largest_distance = distance

            second_city_num += 3
        city_num += 3

    return largest_distance
