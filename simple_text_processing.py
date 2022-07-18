"""

    Author: Tadius Frank


    The goal of this assignment is to familiarize you with processing strings,
    sequences and files, through exercises on looping over contents in string,
    reading and writing files, etc.
"""

from string import *

def every_fourth_char(s):
    """
    Create new string with every fourth character of a string 

    :param s: (int) string input
    :return: (str) every fourth character of s

    """

    new_string = ""
    
    # loops through range of string length and adds character to new string if string index divisible by 4
    # then returns new string of qualified indexes
    for index in range(len(s)):
        if index % 4 == 0:
            new_string += s[index]
    
    return new_string


def copy_parts_of_file(old_filename, new_filename):
    """
    Copies every fourth character in old_filename for each line to new_filename

    :param old_filename: (str) the file we are reading from
    :param new_filename: (str) the file we are copying to

    """

    # opens both old file for reading and new file for writing
    old_file = open(old_filename, "r", encoding = "latin-1")
    new_file = open(new_filename, "w")

    # for loop goes through each line of old file and write every fourth char of each line in new file
    for line in old_file:
        new_file.write(every_fourth_char(line.rstrip("\n")))
        new_file.write("\n")
    
    # closes both files
    old_file.close()
    new_file.close()


def num_characters(s):
    """
    Counts the number of non whitespace characters in a string

    :param s: (str) string input
    :return: (int) number of non whitespace characters

    """

    count = 0

    # loops through each character in string input
    # if character not whitespace adds 1 to count then returns total non whitespace characters
    for characters in s:
        if characters not in whitespace:
            count += 1
    return count


def count_characters(filename):
    """
    Counts all the characters in filename (excluding whitespaces)
    
    :param filename: (file) the file we are counting characters in
    :return: (int) the total number of characters

    """

    # opens file in parameter for reading
    file_name = open(filename, "r", encoding = "latin-1")

    character_count = 0

    # for loop goes through each line in the file and counts the total number of characters by adding the amount on each line
    for line in file_name:
        character_count += num_characters(line)
    
    # closes the file and returns the total number of characters
    file_name.close()
    
    return character_count


def count_char(s, char):
    """
    Counts the number of either uppercase or lowercase form of a character in a string

    :param s: (str) string input
    :param char: (str) character to check for
    :return: (int) number of times char in s
    """

    count = 0

    # loops through each character in string which is converted to all lowercase
    # if characters is the lowercase character parameter count increases by 1, then returns total char in string
    for characters in s.lower():
        if characters == char.lower():
                count += 1
    
    return count


def num_words(s):
    """
    Counts the number of words separated by whitespace
    
    :param s: (str) the string we are measuring the number of words for
    :return: (int) number of words

    """

    word_count = 0
    status = False

    # loops through each character in the string 
    # if character is whitespace and the next character is not whitespace then increases word count by one
    for words in s:
        if (words not in whitespace) and (status == False):
            word_count += 1
            status = True
        elif words in whitespace:
            status = False
    
    # returns the total number of words
    return word_count


def main():
    
    # asks user for character input
    char = input("single letter to count: ")
    
    # continues to ask for single letter while user character input is not a single letter
    while char not in ("abcdefghijklmnopqrstuvwxyz" or "ABCDEFGHIJKLMNOPQRSTUVWXYZ") or not len(char) == 1:
        print("you must enter a single letter!")
        char = input("single letter to count: ")

    # asks user for how they want to run their results -- in file or interactive
    file_or_interactive = input("enter 1 for file or 0 for interactive\n")

    # user selects interactive mode
    if file_or_interactive == "0":
        line_input = 0
        s = ""
        count_lines = 0
        
        # user is asked to enter lines of their string to get results for and will be asked until they input -1
        # each time character inputs a line, variable count_lines increases by 1
        while line_input != "-1":
            line_input = input("input line or -1 to stop: ") 
            if line_input != "-1":
                s += line_input + "\n"
                count_lines += 1

        # total number of lines
        print(str(count_lines) + " lines")

        # total number of words
        print(str(num_words(s)) + " words")
        
        # total number of non whitespace characters
        print(str(num_characters(s)) + " non-whitespace characters")
        
        # number of times char appears
        print(str(count_char(s, char)) + " " + str(char) + "'s")
        
        # average length of a word number of characters divded by number of words
        print("average word length is: " + str(num_characters(s) / num_words(s)))
        
        # percentage of char is number of char divided by number of characters multiplied by 100
        print("percentage " + str(char) + "'s is: " + str(count_char(s, char) / num_characters(s) * 100))


    # user selects file mode
    # asks user for filename and then opens that file
    if file_or_interactive == "1":
        file_name = input("filename?: ")
        filename = open(file_name, "r", encoding = "latin-1")
        
        num_lines = 0
        words = 0
        total_c = 0
        total_words = 0
        
        # loops through each line and adds number of lines, words, and characters
        for line in filename:
            num_lines += 1
            total_words += num_words(line)
            total_c += count_char(line, char)
        
        # total number of lines in file
        print(str(num_lines) + " lines")

        # total number of words in file
        print(str(total_words) + " words")

        # total number of non whitespace characters
        print(str(count_characters(file_name)) + " non-whitespace characters")

        # total number of times c appears in the file
        print(str(total_c) + " " + str(char) + "'s")

        # average length of a word number of characters divded by number of words
        print("average word length is: " + str(count_characters(file_name)/total_words))

        # percentage of char is number of char divided by number of characters multiplied by 100
        print("percentage " + str(char) + "'s is: " + str(total_c / count_characters(file_name) * 100))


if __name__ == '__main__':
    main()
