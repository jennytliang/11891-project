def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: ( s
	"""

    wo = s.replace(" ","").split(",")
    wo2 = []
    for w in wo:
        wo2.append(w)
    return wo2


def sum_list(l):
    """
    You will be given a list of integers. You have to return the sum of the integers.
    
    For example:
    sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    sum_list([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    sum_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    
    The length of the list will always be at least 1.
    """
    sum = 0
    for n in l:
        sum += n
    return sum


def sum_list2(l):
    """
    You will be given a list of integers. You have to return the sum of the integers.
    
    For example:
    sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    sum_list([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    sum_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    
    The length of the list will always be at least 1.
    """
    sum = 0
    for n in l:
        sum += n
    return sum


def is_prime(n):
    """
    You will be given a number n. For this task, you should return if the number is a prime number or not.
   