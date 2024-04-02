def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.replace(", ", " ").split()


def count_substring(string, sub_string):
    """
    You will be given two strings. Count the number of times the first string appears as a substring within the second string.

    For example:
    count_substring("Hi", "HiHiHi") == 2
    count_substring("dragon", "Dragon") == 1
    count_substring("banana", "Banana") == 3
    count_substring("distance", "distance") == 1
    count_substring("a", "a") == 1
    count_substring("", "") == 0
    """
    return string.count(sub_string)


def is_prime(number):
    """
    You will be given a number. You should determine if it is a prime number or not.
    For example:
    is_prime(1) == False
    is_prime(2) == True
    is_prime(11) == True
    is_prime(4) == False
    is_prime(101) == True
    is_prime(2021) == False
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def is_leap_year(year):
    """
    You will be given a year. Determine whether or not it is a leap year. If the year can be divided by 4, it is a leap year, unless it is divisible by 100 and not by 400.
    For example:
    is_leap_year(1990) == False
    is_leap_year(2000) == True
    is_leap_year(2019) == False
    is_leap_year(2020) == True
    """
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 100 == 0 and year % 40