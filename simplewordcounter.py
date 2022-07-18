
"""

    Author: Tadius Frank


    The goal of this assignment is to give you more practice about sorting.
"""

# import desired modules 
import matplotlib.pyplot as plt
import string  
import sys
import time


def create_dict(filename):
    """
    This fuunction takes a file as input and returns a dictionary in the form {word : frequency}
    
    :param filename: (str) a file name that corresponds to a file with information we want to create our dictionary from

    :return word_count_dict: (dict) the dictionary in the form {word : frequency} from information from the file we input the name for
    """
    # initialize our word-count dictionary
    word_count_dict = {}

    # open desired file for reading
    in_file = open(filename, 'r')
    words_string = in_file.read() # reads in entire file as a string
    words_list = words_string.split() # splits string along whitespaces into "words"

    # makes each word in file lowercase, strips leading/tailing punctuation
    for word in words_list:
        word = word.lower().strip(string.punctuation)

        # appends words that start with letters to new_word_list
        if len(word) > 0 and word[0] in string.ascii_letters:

            # either updates or adds new key-value pair
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1

    # closes file 
    in_file.close()

    return word_count_dict


def convert_dict_to_list(word_dict):
    """
    This funtion takes a dictionary and returns a list that represents it

    :param word_dict: (dict) a dictionary of the form {word : frequency}

    :return: (list) a list of tuples in the form (word, frequency) 
    """
    # initializes the list we want to append to
    word_list = []

    # loops through each key in the dict and appends a touple of (key, value) to a list
    for item in word_dict:
        word_list.append((item, word_dict[item]))

    return word_list


def cmp_words_ascend(l,r):
    """
    This is a comparison function that will be used by the sorting algorithm that compares whether a word is "smaller" than another word (python can do this beacuse of ascii)

    :param l: (str) the "left" word we want to compare to another word (see param r)
    :param r: (str) the "right" word we want to compare to another word (see param l)

    :return: (bool) whether or not the value of l (left string) is smaller than value of r (right string)
    """

    # simply returns boolean
    return l[0] < r[0]
 

def cmp_counts_descend(l,r):
    """
    This is a comparison function that will be used by the sorting algorithm that compares whether a numerical value, an int, is larger than another

    :param l: (int) the "left" number we want to compare to another number (see param r)
    :param r: (int) the "right" number we want to compare to another number (see param l)

    :return: (bool) whether or not the value of l (left string) is larger than value of r (right string)
    """

    # simply returns boolean
    return r[1] < l[1]


def insert(data, start, end, val, cmp_fun):
    """
    Helper function for insertion_sort

    :param data: (list) our word data in the form of a list of tuiples (word, frequency)
    :param start: (int) starting index for sorting
    :param end: (int) ending index for sorting 
    :param val: (int) index for current position
    :param cpm_fun: (func) a function that compares two values according to what we wish to sort; returns a Boolean value
    """

    # initializes current position
    current_pos = end + 1

    # tells us the value of data at the current position after looping through all the data
    while current_pos > start and cmp_fun(val, data[current_pos - 1]):
        data[current_pos] = data[current_pos - 1]
        current_pos -= 1

    data[current_pos] = val

def insertion_sort(cmp_fun, data):
    """
    This function takes a list that can be generated by the convert_dict_to_list function.
    And creates a sorted list in the format of (word, frequency)

    :param cmp_fun: (func) a function that compares two values according to what we wish to sort; returns a Boolean value
    :param data: (list) is a list of tuples in the format of (word, frequency)

    :return: (list) a sorted list with tuples [(word, frequency)]
    """
    # initializes copied data so we don't manipulate data
    aList = data.copy()
    length = len(aList) # initializes length 
    
    # calls insert for all of aList
    for i in range(length):
        insert(aList, 0, i-1, aList[i], cmp_fun)
        
    return aList

def selection_sort(cmp_fun, data):
    """
    This function is a sorting algorithm; sorts by selection that takes a list of data and a type of sorting to be done

    :param cmp_fun: (func) a function that compares two values according to what we wish to sort; returns a Boolean value
    :param data: (list) is a list of tuples in the format of (word, frequency)
    
    :return: (list) a sorted list with tuples [(word, frequency)]
    """
    # initialize copy of data so as not to modify data
    new_list = data.copy()

    # loop through indices in the class
    for i in range(len(new_list)):
        unsorted_ind = i

        # selects values that make cmp_fun True
        for n in range(i+1, len(new_list)):

            # compares values by calling cmp_fun
            if not cmp_fun(new_list[unsorted_ind], new_list[n]): 
                unsorted_ind = n

        # replaces values
        if i != unsorted_ind: 
            current_val = new_list[i]
            new_list[i] = new_list[unsorted_ind]
            new_list[unsorted_ind] = current_val

    return new_list

# OLD CODE 
#   # copies data so we don't manipulate data 
#     aList = data.copy()
#     newList = [] # initializes a new list
    
#     # initializes length
#     length = len(aList)

#     # sorts if counts go down
#     if cmp_fun == cmp_counts_descend:

#         # iterates through all of aList
#         for item in range(length):

#             # appends largest value
#             largest = max(aList)
#             newList.append(largest)
#             aList.remove(largest)

#     # sorts if words ascend
#     elif cmp_fun == cmp_words_ascend:

#         # iterates through all of aList
#         for item in range(length):

#             # appends smallest value
#             smallest = min(aList)
#             newList.append(smallest)
#             aList.remove(smallest)

#     return newList
    
def merge(cmp_fun, list1, list2): 
    """
    A helper function for merge_sort

    :param cmp_fun: (func) a function that compares two values according to what we wish to sort; returns a Boolean value
    :param list1: (list) half of a list to sort from
    :param list2: (list) the other half of a list to sort from

    :return: (list) a sorted list of form [(word, frequency)]
    """
    # initialize indices 
    index1 = 0
    index2 = 0

    # initialize resultList
    resultList = list1 + list2

    # iterate through the lists
    while index1 < len(list1) and index2 < len(list2): 

        # selects first element of list if cmp_fun is True
        if cmp_fun(list1[index1], list2[index2]):
            resultList[index1+index2] = list1[index1]
            index1 += 1 

        # else, selects first element of other list
        else:
            resultList[index1+index2] = list2[index2]
            index2 += 1
    
    # slices list to deal with smaller case, removes element that was sorted
    if index1 < len(list1): 
        resultList[(index1+index2):]=list1[index1:]

    # does same if first list element not used
    if index2 < len(list2): 
        resultList[(index1+index2):]=list2[index2:]

    return resultList
    
def merge_sort(cmp_fun, data):
    """
    This function is a sorting algorithm; sorts by merging

    :param cmp_fun: (func) a function that compares two values according to what we wish to sort; returns a Boolean value
    :param data: (list) a list of tuples in the form [(word, count)]

    :return: (func call) that returns (list) a call to recursiveMergeSort (see def recursiveMergeSort)
    """
    # copies data do we don't change actual data
    aList = data.copy()

    # helper function to actually do the recursion
    def recursiveMergeSort(aList):
        """
        A helper function for merge_sort

        :param aList: (list) a copy of data (see aList = data.copy() above)

        :return: (func call) that returns (list) a call to merge (see def merge)
        """
        # if list is too small, base case and return. this is the final product of merge_sort
        if len(aList)<2:
            return aList

        # recursive case, call half of each list to merge
        else:
            middle = len(aList) // 2
            list1 = recursiveMergeSort(aList[:middle]) 
            list2 = recursiveMergeSort(aList[middle:]) 
            return merge(cmp_fun, list1, list2)
        
    return recursiveMergeSort(aList)


def time_sort(sorting_algorithm, cmp_fun, data):
    """
    This function calculates the time to sort

    :param sort_algorithm: (function) is the function for the different sorting algorithms implemented in Part 1 and Part 2.
    :param cmp_fun: (function) is the comparison function to be used on our data.
    :param data: (list) is a list of the tuples (e.g., (word, count)) to be sorted

    :return: (float) a rounded to three decimals version of how long it took for the sort to run
    """   
    # start time
    time_start = time.time()

    # calls a specified sort function
    sorting_algorithm(cmp_fun, data)

    # end time
    time_end = time.time()
    
    return round(time_end - time_start, 3)


def plot_word_frequency(sorted_words): 
    """
    creates the information for the plot of the word frequency (but does not actually plot it)

    :param sorted words: (list) the sorted data based on wordcount
    """
    # initializes frequency to be plotted
    frequencies = []

    # appends the count of each word to frequency
    for n in range(len(sorted_words)):
        frequencies.append(sorted_words[n][1])
    
    # creates the axes based on the length of sorted_words
    if len(sorted_words) < 1000:
        x = list(range(len(sorted_words)))
        y = frequencies[:len(sorted_words):]
    else:
        x = list(range(1000))
        y = frequencies[:1000:]

    # actually plots points 
    plt.plot(x, y)
    plt.xlabel("Word Index")
    plt.ylabel("Word Count")
    plt.title("Word Count Distribution")

def main(filename):
    """
    This function: 
        1) Creates a dictionary of words by calling create_dict
        2) Converts the words dictionary to a list of word tuples (word, count) by calling convert_dict_to_list
        3) Sorts the dictionary items and prints out the list of the first 10 words when sorting alphabetically.
        4) Sorts the dictionary items and prints out the highest 10 counts as a list.
        5) Plots the top 1000 words from highest to lowest (based on count) using your plot function.
            â€¢ Note, uses any of our sorting algorithm implementations
        6) Evaluates the running time of your sorting algorithms (sorting the words, not the counts) on sublists of your data.
            â€¢ Runs the sorting algorithms (all three of them) to sort the first 1000, 2000, 3000, . . . 10000 words from the unsorted word list. 
              Then creates a list containing tuples (number_of_words, runtime) for the above runnings.
            â€¢ Prints the results 
    """
    # creates a dictinoary based on filename, converts it to a list
    dictionary = create_dict("starter/" + filename)
    dict_to_list = convert_dict_to_list(dictionary)

    # displays top 10 frequency words using merge_sort
    alphabetical_order = merge_sort(cmp_words_ascend, dict_to_list)
    first_words = [word[0] for word in alphabetical_order[:10]]
    print("First 10 words: " + str(first_words))

    # displays the top ten counts of the words
    frequency_order = merge_sort(cmp_counts_descend, dict_to_list)
    highest_counts = [word[1] for word in frequency_order[:10]]
    print("Top 10 counts: " + str(highest_counts))

    # displays how long it took to sort 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, and 10000 words using insertion_sort
    insertion_stats = [(value, time_sort(insertion_sort, cmp_words_ascend, dict_to_list[:value])) for value in range(1000, 10001, 1000)]
    print("Insertion sort: " + str(insertion_stats))

    # displays how long it took to sort 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, and 10000 words using selection_sort
    selection_stats = [(value, time_sort(selection_sort, cmp_words_ascend, dict_to_list[:value])) for value in range(1000, 10001, 1000)]
    print("Selection sort: " + str(selection_stats))

    # displays how long it took to sort 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, and 10000 words using merge_sort
    merge_stats = [(value, time_sort(merge_sort, cmp_words_ascend, dict_to_list[:value])) for value in range(1000, 10001, 1000)]
    print("Merge sort: " + str(merge_stats))

    # plots the word frequency
    plot_word_frequency(merge_sort(cmp_counts_descend, dict_to_list))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main("t8.shakespeare.txt")
        # plt.show() is called here so that
        # autograder don't need to plot
        plt.show()
