# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".


def hello_world():  # define the function with no arguments
    '''return the phrase "Hello World"'''

    print "Hello World"  # the function's action is to print this phrase

hello_world()  # testing the function


# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.


def name_function(input_name):  # define a function with one argument
    '''take a name as a string and print "Hi" plus the input name'''

    print "Hi {}".format(input_name)  # print a string with a formatter for the name argument

name_function("Emily")  # testing

# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.


def multiply_nums(x, y):  # define a function that takes two parameters, the numbers to be multiplied
    '''takes two integers and multiplies them together'''

    multiplied_nums = x * y  # the function will multiply the number arguments
    print multiplied_nums  # print the result of the function

multiply_nums(7, 2)  # testing


# 4. Write a function that takes a string and an integer and
#    prints the string that many times


def stringteger(string_input, integer_input):  # function takes two arguments, string and integer
    '''takes in a string and an integer and prints the string as many times as the number'''

    multi_string = string_input * integer_input  # this tells the function to multiply the string and the integer arguments
    print multi_string  # print the result of the above multiplication

stringteger("hello", 4)  # testing


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".


def higher_or_lower(x):  # function takes in one argument, an integer x
    '''takes in an integer and prints statements describing if it is higher
    or lower than 0, or prints "Zero" if it is zero'''

    if x > 0:  # test if x is higher than 0
        print "Higher than 0"  # prints statement if condition is met
    elif x < 0:  # tests if x is less than 0
        print "Lower than 0"  # prints statement if elif statement is met
    else:
        print "Zero"  # prints statement if above 2 conditions are not met

higher_or_lower(6)  # testing
higher_or_lower(0)  # testing


# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.


def divisible_by_3(x):  # define function that takes integer argument
    '''takes an integer and returned boolean statement depending on if the integer
    if divisible by 3'''

    if x % 3 == 0:  # check if integer is odd
        return True  # return True if integer is odd
    else:
        return False  # return False if integer is not odd (even)

divisible_by_3(9)  # testing


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.


def number_of_spaces(sentence):  # define function that takes sentence string argument
    '''takes a sentence as one string and returns the number of spaces in the sentence'''

    space_count = sentence.count(" ")  # use .count method to count number of spaces, bind to variable
    return space_count  # return number of spaces variable

number_of_spaces("Hi there")  # testing


# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.


def meal_total(meal_price, tip_percentage=0.15):  # define a function with two arguments, one being optional
    '''takes a meal price and tip percentage and returns the total amount paid,
    which is the meal price plus the tip. Passing in tip is optional, and the
    function will assume 0.15 if tip percentage is not given'''

    total_price = float(meal_price) + (meal_price * tip_percentage)  # total price equation
    return total_price  # return the total price to exit function

print meal_total(20, 0.2)  # testing


# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.


def what_is_it(x):  # function takes one argument, an integer
    '''takes an integer and returns info on whether it is positive or negative,
    even or odd'''

    string_list = []  # empty list for our string info
    if x > 0:  # conditional statement testing if integer is pos or neg
        item = "Positive"  # binding item to name "positive" if it passes this condition
        string_list.append(item)  # append item to empty list
    else:
        item = "Negative"  # binds item to "negative" if doesn't pass condition
        string_list.append(item)  # add item to empty list

    if x % 2 == 0:  # check if integer is even using mod
        item2 = "Even"  # bind item2 to "even" if it passes condition
        string_list.append(item2)  # add item2 to our empty list
    else:
        item2 = "Odd"  # binds item2 to "odd"
        string_list.append(item2)  # add item2 to our empty list

    return string_list  # return the list, which will contain two strings

#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.


my_list = what_is_it(5)  # call the function, bind to variable
sign, parity = my_list  # unpack the list

print sign, parity  # print sign and parity on one line


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.


def tax_function(item_cost, state, default_tax=0.05):  # define func that takes optional argument "tax"
    '''takes cost of an item, state, and tax percentage, and returns the total cost
    of the item considering all of the arguments'''

    if state == "CA":  # conditional for if state is CA
        total = (0.07 * item_cost) + item_cost  # return total cost of item with tax included
    else:
        total = (default_tax * item_cost) + item_cost  # if state is not CA, return this total

    return total  # return total cost of item

print tax_function(30, "TX")  # testing


# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.


def name_job(name, title="Engineer"):  # define function that takes a name and optional title which defaults to "Engineer"
    '''returns statement given name and title arguments'''

    return title + " " + name  # the function will return the person's title and name


# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.


def email(receiver, sender_name, sender_title):  # define function that takes 3 arguments
    '''returns string with receiver, sender name, and sender title info'''

    receiver = name_job("Jane Doe")  # call name_job function and bind to receiver variable
    print "Dear {}, I think you are amazing! Sincerely, {} {}".format(receiver, sender_name, sender_title)  # print the statement with formatters

email("Jane Doe", "John Snow", "Developer")  # testing


# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.


numbers = [1, 2]  # numbers list


def num_list(num):  # function takes one argument, an integer
    '''adds number argument into numbers list'''

    numbers.append(num)  # add number to list numbers
    return numbers  # breaks out of the function

print num_list(3)
