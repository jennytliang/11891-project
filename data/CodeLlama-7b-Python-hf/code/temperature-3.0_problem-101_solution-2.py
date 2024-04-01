def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    return [item.strip() for item in s.split(',')]


def sum_positive(arr):
    """
    Given an array of integers. You need to find the sum of all the positive integers.
    
    sum_positive([1, 2, 3, -4, 5]) == 1 + 2 + 3 + 5 = 11
    sum_positive([1, -2, 3, -4, 5]) == 1 + 3 + 5 = 9
    """

    return sum(x for x in arr if x > 0)


def largest_odd_times(arr):
    """
    You will be given an array of integers. You need to return the element that is 
    appeared more than half the time in the array. If more than one element appeared
    more than (n / 2) times, return the element that appeared in odd number of times.
    
    largest_odd_times([2, 1, 2, 3, 2, 5, 4, 2, 2, 2]) == 2 as 2 appeared 5 times which is more than 5/2 i.e 2.5. 
    largest_odd_times([2, 2, 3, 5, 2, 3, 2, 2, 2, 3, 2, 2, 5, 2, 3]) == 3 as 3 appeared 5 times which is more than 5/2 i.e 2.5. 
    largest_odd_times([0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7]) == 5 as 5 appeared 5 times which is more than 5/2 i.e 2.5. 
    """
    
    counter = {}
    for x in arr:
        if x not in counter:
            counter[x] = 1
        else:
            counter[x] += 1

    max_value = 0
    max_value_count = 0
    max_odd_count = 0
    for k, v in counter.items():
        if v > max_value_count:
            max_value = k
            max_value_count = v
        if (v % 2 != 0 and v > max_odd_count):
            max_odd_count = v

    if max_value_count > len(arr) // 2:
        return max_value
    return None

