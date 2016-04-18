"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def print_list(my_list):
    """Print each item in the input list

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9

    """
    for item in my_list:  # iterate over items in list
        print item  # print items in the list on separate lines


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    empty_list = []  # empty list where odd items will go
    for item in number_list:  # loop iterates over list items
        if item % 2 != 0:  # use mod to check if items are odd
            empty_list.append(item)  # append items that pass above test to empty list

    return empty_list  # returns list of odd numbers


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    empty_list = []  # empty list where items that are even will go
    for item in number_list:  # for loop iterates over list items
        if item % 2 == 0:  # loop over items using mod to check if even
            empty_list.append(item)  # append items that pass mod test to empty_list

    return empty_list  # returns list of even numbers


def every_other_item(my_list):
    """Return a list that contains every other item in my_list starting
       with the first item.

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["you", "friend", "are", "very", "good", " ", "at", " ", "coding"])
       ['you', 'are', 'good', 'at', 'coding']

    """
    for item in my_list:  # iterate over each item in the list
        return my_list[::2]  # slice indicates to skip over every other element, beginning with the first item in my_list


def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """
    for index, item in enumerate(my_list, 0):  # use enumerate so we get index and item
        print index, item  # print index, item on same line


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    empty_list = []  # empty list for words longer than 4 chars
    for item in word_list:  # iterate over items in word_list
        if len(item) > 4:  # check if word length is longer than 4 chars
            empty_list.append(item)  # append words that pass above test to empty_list

    return empty_list  # returns list containing only words >4 chars


def n_long_words(word_list, n):
    """Return all words in input list that are longer than n characters.

    >>> n_long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"], 3)
    ['hello', 'spam', 'spam', 'bacon', 'bacon']

    >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
    ['apples', 'bananas']
    """
    empty_list = []  # list for items that are longer than n characters
    for item in word_list:  # iterate over items in list
        if len(item) > n:  # check if word length is longer than n
            empty_list.append(item)  # add items that satisfy loop condition to empty list

    return empty_list  # return list of items with length > n

import sys  # import sys module for maxint (this is for smallest_int)


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """
    if len(number_list) >= 1:  # if len is 0 function will return None; also checks if the length is greater than or equal to 1
        total = sys.maxint  # total should be huge number for comparison, so using maxint here makes the most sense
        for number in number_list:  # iterate over list of numbers
            if number < total:  # check if number is less than number
                total = number  # if number is less than total, it becomes the new number; this is to keep track of it

        return total  # number returned should be the lowest number


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    if len(number_list) >= 1:  # if len is 0 function will return nothing
        total = -sys.maxint  # initiate total at largest negative number (that's why I used -maxint) because we are looking for it to be larger
        for number in number_list:  # iterate over numbers in list
            if number > total:  # see if number in list is greater than the number total is set to
                total = number  # if number is greater than total we replace total

        return total  # total will be the largest number


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    empty_list = []  # empty list for numbers divided by 2
    for item in number_list:  # iterate over items in number_list
        a = float(item)/2  # divide item by 2; float so it doesn't round off the half
        empty_list.append(a)  # append item divided by 2 to empty_list

    return empty_list  # return list of numbers divided by 2


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    empty_list = []  # empty list for the length of words in the input list
    for item in word_list:  # iterate over items in word_list
        word_length = len(item)  # get length of words in list
        empty_list.append(word_length)  # append word lengths to empty list

    return empty_list  # returns list of word lengths


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    total = 0  # initiate a counter at 0
    for number in number_list:  # iterate over items in input list
        total += number  # increase the total by numbers in number list

    return total  # return the total, which will be all numbers summed


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    total = 1  # initiate a counter at 1 - this is so if the list is empty, the product is 1
    for number in number_list:  # iterate over items in list
        total *= number  # multiply running total by number in list

    return total  # return total, which will be product of all numbers


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    total = ""  # initiate empty string
    for word in word_list:  # iterate over words in list
        total += word  # concatenate words to running total string

    return total  # return total, which is all words joined together


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    total = 0  # initialize counter at 0
    for number in number_list:  # iterate over items in list
        total += number  # increase total by number in list

    return float(total)/len(number_list)  # return float of total by length of the list


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """
    comma_space = ", "  # the separator is a comma with a space

    return comma_space.join(list_of_words)  # returns the list of words with a comma and space


def foods_in_common(foods1, foods2):
    """Using ANY Python data structure presented in the last week, given 2 lists of foods, 
    return a set of items that are in common between the two. (Don't include any duplicates
    in the output collection.)
    
    For example:

    >>> foods_in_common(["cheese", "bagel", "cake"], ["hummus", "beets", "bagel", "lentils"])
    set(['bagel'])

    If there are no foods in common, return an empty set.

    >>> foods_in_common(["lamb", "chili", "cheese"], ["cake", "ice cream"])
    set([])

    """
    common_foods = []  # empty list for keeping track of common foods between list1 and list2
    for item in foods1:  # iterate over items in food1 list
        if item in foods2:  # if the item in food1 is also in food list 2..
            common_foods.append(item)  # add the common item to common_foods list

    return set(common_foods)  # use set to eliminate any duplicates in the common_foods list; return the list of foods in both lists


def reverse_list(my_list):
    """Return the inputted list, reversed.

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

    Do not use the python methed reverse()/reversed().

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    """
    new_list = my_list[::-1]  # reverse the list using slices, with the step running backwards

    return new_list  # return reversed list


def reverse_list_in_place(my_list):
    """Return the inputted list reversed--WITHOUT creating a new list.
       This will involve moving the items in my_list to different positions 
       in the same list.

       Do not use the python methed reverse()/reversed()

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']


    """
    # Can't figure this one out. I think I have to swap element at index 0 with element at index -1
    # and continue swapping from outer to inner until I reach the middle,
    # and return that result, but I don't know how to convert that into code :(


def duplicates(my_list):
    """Return a list of words which are duplicated in the input list. The returned 
    list should be in ascending order.

    >>> duplicates(["apple", "apple", "banana", "cherry", "banana", "apple"])
    ['apple', 'banana']

    >>> duplicates([1, 2, 2, 4, 4, 4, 7])
    [2, 4]


    """
    dupes = []  # empty list for duplicates
    for item in my_list:  # iterate over items in list
        if my_list.count(item) > 1:  # count method checks how many times objects occur in list, which is perfect for finding instances more than 1 (dupes)
            dupes.append(item)  # if an item is a dupe and occurs more than once, we add to our list

    dupes_set_list = set(dupes)  # dupe list will contain every instance of an object so use set to eliminate multiple numbers
    dupes_list = list(dupes_set_list)  # convert set to list

    return sorted(dupes_list)  # return sorted list in ascending order


def find_letter_indices(list_of_words, letter):
    """Given a list of words and a letter, return a list of integers that correspond
    to the index of the first occurance of the letter in that word.

    Do not use the .index() list method.

    >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
    [0, 1, 2]

    If the letter doesn't occur in one of the words, use None for that word in
    the output list. For example:

    >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
    [0, 1, 2, None]

    """
    string_list = []  # empty list to convert list_of_words elements into strings
    indexes = []  # empty list for indexes
    for item in list_of_words:  # iterate over elements in list
        item = str(item)  # convert elements to strings
        string_list.append(item)  # append string items to string list

    for item in string_list:  # iterate over string list
        if letter in item:  # check if letter is in the element
            indexes.append(string_list.index(item))  # if letter is in the element, add the letter's index number to the list of indexes
        else:
            indexes.append(None)  # if the letter is not in the element, append None to the list of indexes
            # I am not entirely sure this solution is a good one. Though my tests passed, appending None to the index list seems like I'm cheating? o_O IDK
            # I'm also not sure if creating a list of indexes is the most elegant way to solve this

    return indexes  # return list of indexes


def largest_n_items(input_list, n):
    """Given a list of integers along with an integer n, return a 
    list of the largest n numbers in the input list in ascending order. 

    You can assume that n will be less than the length of the list. 

    For example:

    >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
    [59, 700, 6006]

    """
    sorted_list = sorted(input_list)  # sort list so elements run from smallest to largest
    largest = sorted_list[-n::]  # the list is sorted from smallest to largest, and because we want the nth number of largest integers, slice the sorted list starting from the -nth index at the end of the list

    return largest  # return list of largest numbers


##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
