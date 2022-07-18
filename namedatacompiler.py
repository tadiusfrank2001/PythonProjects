
"""

    Author: Tadius Frank

    The goal of this assignment is to design a program that's able to compile data about a
    given name from the SS database of names in the U.S.A.
"""
import matplotlib.pyplot as plt
import sys

def parse_names(fname):
    """
    parse a name file

    :param fname: (str) name (full path) of the file to read and parse

    :return d: (dict) a name dictionary
    """

    # open file for reading
    file_in = open(fname, "r")

    # initialize empty dictionaries 
    year_name_dict = {} # outer dictionary
    
    # iterate through lines in file, extract useful information, add to dictionaries
    for lines in file_in.readlines():
        name_data_list = lines.strip().split(",")
        year = int(name_data_list[2])
        person_name = name_data_list[3]
        count = int(name_data_list[4])

        # add new year key if does not exist, add new name/count pair if does
        if not year in year_name_dict.keys():
            year_name_dict[year] = {person_name : count}
        else:
            # add count, or update count if name already existed for a certain year
            if not person_name in year_name_dict[year].keys():
                year_name_dict[year][person_name] = count
            else:
                year_name_dict[year][person_name] += count

    # close file
    file_in.close()

    return year_name_dict

def extract_data(name_dict, match_string):
    """
    Takes a name dictionary  { year : {name : count}} and a string to match (strings like abc* are special case)
    and creates a result dictionary { year : count }

    :param name_dict: (str) name dictionary
    :param match_string: (str) string to match

    :return: (dict) a dictionary of form { year : count } that has number of instances of match_string
    """
    result_year_count = dict() # initializes a dictionary 

    index_of_star = len(match_string) - 1 # finds the index of a star if a partial match is desired

    # loops through each year in the dictionary keys
    for year in name_dict.keys():

        # finds corner case when there are no years 
        if year not in result_year_count:
            result_year_count[year] = 0

        # loops through each name in they keys of each year in the dictionary and checks if the match string is a name, part of a name or none of a name
        for name in name_dict[year].keys():

            # matches a full name
            if match_string == name:
                result_year_count[year] = name_dict[year][name]

            # matches all names
            elif match_string == "*":
                result_year_count[year] += name_dict[year][name]

            # matches part of a name to all matches
            elif name[:index_of_star] == match_string[:index_of_star]:
                result_year_count[year] += name_dict[year][name]

    return result_year_count 

def normalize_data(data):
    """
    Normalize data by dividing by average value computed over years

    :param data: (dict) a dictionary with the data
    """

    # initialize counter and the number of years
    count = 0
    years = len(data)
        
    # loops through the years in the keys of the dictionary of data, and set adds 1 to the value
    for year in data.keys():
        count += data[year]

    # make sure not to divide by zero!
    if years != 0:
        avg = count/years
        
        # loops through year in the keys of the dictionary of data, and sets the value to the count of year values in the dict divided by the average count per year 
        for year in data.keys():
            if avg != 0:
                data[year] = data[year] / avg

def scatter_plot(data, format, name):
    """
    creates a scatterplot (but doesn't draw the final plot) (he plotted data will need to have been normalized)

    :param data: (dict) a dictionary of the form { year : count }
    :param format: (str) format string for matplotlib
    :param name: (str) name of this plot for legend
    """

    # initializes the x and y axes values
    x = data.keys()
    y = data.values()

    # actually plots points 
    plt.plot(x, y, format, label = name)

def close_plot(title):
    """
    this function should add the legend, title, and labels to the graph

    :param title: (str) title for whole plot
    """

    # sets legend, labels, and title for the graph
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Normalized count")
    plt.title(title)

def main(filedir):
    """
    Interactive input to specify plot
    Creates plots for the requested pattern for each of the 
    requested states
    :param filedir: the path to directory with data files
    """

    # list of valid state abbreviations to check user input against
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    # the criteria 
    match_pattern = input("Enter a pattern to match: \n\t")

    user_states = [] # initialized list of user-generated state names 

    # loop to get state inputs and ensure they are valid
    for state_abreviations in range(4):
        state_chosen = input("Enter a two letter abbreviation for a state: \n\t")

        # ensures a valid input of a state name or an empty string
        while not(state_chosen in states or state_chosen == ""):
            state_chosen = input("Not quite. Enter a two letter abbreviation for a state: \n\t")
        
        # adds the current user-generated state name to a list of user-generated state names to iterate through later
        if state_chosen in states:
            user_states.append(state_chosen)
        else:
            break # breaks out of the for loop if the user 
    
    # markers = [".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "s", "p" "*", "h", "H", "+", "x", "D", "d", "|", "_"] (possible markers for format)
    # colors = ["b", "g", "r", "c", "m", "y", "k", "w"] (possible colors for format)

    format_list = ["bx", "r4", "g+", "k|"] # the list of formats we (arbitrarily) chose
    
    count = 0 # initialize which plot we're working on
    
    # loops through each or the user's input states, extracts the data, normalizes the data, and plots the data
    for state in user_states:
        extracted_data = extract_data(parse_names(filedir + state + '.TXT'), match_pattern)
        normalize_data(extracted_data)
        plot_format = format_list[count] # chooses different color/state for different states for clarity
        count += 1 # keeps track of which format to use
        scatter_plot(extracted_data, plot_format, state)

    # closes the plot for viewing 
    close_plot(match_pattern)


if __name__ == '__main__':   
    main('namesbystate/')
    # plt.show is here so you don't need to call it in your code
    plt.show()
    
