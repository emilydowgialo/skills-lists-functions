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
    for item in my_list:
        print item


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    only_odd = []
    for num in number_list:
        if num % 2 != 0:
            only_odd.append(num)

    return only_odd


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    only_even = []
    for num in number_list:
        if num % 2 == 0:
            only_even.append(num)

    return only_even


def every_other_item(my_list):
    """Return a list that contains every other item in my_list starting
       with the first item.

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["you", "friend", "are", "very", "good", " ", "at", " ", "coding"])
       ['you', 'are', 'good', 'at', 'coding']

    """
    for item in my_list:
        return my_list[::2]


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
    for i, item in enumerate(my_list, 0):
        print i, item


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    longer_than_4 = []

    for word in word_list:
        if len(word) > 4:
            longer_than_4.append(word)

    return longer_than_4


def n_long_words(word_list, n):
    """Return all words in input list that are longer than n characters.

    >>> n_long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"], 3)
    ['hello', 'spam', 'spam', 'bacon', 'bacon']

    >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
    ['apples', 'bananas']

    """
    longer_than_n = []

    for word in word_list:
        if len(word) > n:
            longer_than_n.append(word)

    return longer_than_n


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
    if len(number_list) == 0:
        return None

    else:
        smallest = number_list[0]

        for num in number_list:
            if num < smallest:
                smallest = num

        return smallest


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
    if len(number_list) == 0:
        return None

    else:
        largest = number_list[0]

        for num in number_list:
            if num > largest:
                largest = num

        return largest


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    halves = []

    for num in number_list:
        num_halfed = num/2.0
        halves.append(num_halfed)

    return halves


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    lengths = []

    for word in word_list:
        lengths.append(len(word))

    return lengths


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
    total = 0

    for num in number_list:
        total += num

    return total


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
    product = 1

    for num in number_list:
        product *= num

    return product


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
    joined = ""

    for word in word_list:
        joined += word

    return joined


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.

    """
    avg = 0

    for num in number_list:
        avg += num

    return avg/float(len(number_list))


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """
    with_comma = ", "

    return with_comma.join(list_of_words)


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
    common_foods = []

    for food in foods1:
        if food in foods2:
            common_foods.append(food)

    return set(common_foods)


def reverse_list(my_list):
    """Return the inputted list, reversed.

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

    Do not use the python methed reverse()/reversed().

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    """
    reversed_list = []

    for item in my_list:
        reversed_list.insert(0, item)

    return reversed_list


def reverse_list_in_place(my_list):
    """Return the inputted list reversed--WITHOUT creating a new list.
       This will involve moving the items in my_list to different positions
       in the same list.

       Do not use the python methed reverse()/reversed()

        >>> reverse_list_in_place([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list_in_place(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

        >>> reverse_list_in_place(["kitties", "are", "the", "coolest"])
        ['coolest', 'the', 'are', 'kitties']


    """
    for idx, item in enumerate(my_list):
        if idx == (len(my_list)/2):
            break

        my_list[idx], my_list[len(my_list) - (idx + 1)] = my_list[len(my_list) - (idx + 1)], my_list[idx]

    return my_list


def duplicates(my_list):
    """Return a list of words which are duplicated in the input list. The returned
    list should be in ascending order.

    >>> duplicates(["apple", "apple", "banana", "cherry", "banana", "apple"])
    ['apple', 'banana']

    >>> duplicates([1, 2, 2, 4, 4, 4, 7])
    [2, 4]


    """
    dupes = []

    for item in my_list:
        if my_list.count(item) > 1:
            dupes.append(item)

    return sorted(set(dupes))


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
    letter_indices = []

    for index, word in enumerate(list_of_words):
        if letter in word:
            letter_indices.append(index)
        else:
            letter_indices.append(None)

    return letter_indices


def largest_n_items(input_list, n):
    """Given a list of integers along with an integer n, return a
    list of the largest n numbers in the input list in ascending order.

    You can assume that n will be less than the length of the list.

    For example:

    >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
    [59, 700, 6006]

    """
    largest_sorted = sorted(input_list)

    return largest_sorted[-n::]


##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
