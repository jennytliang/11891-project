def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """
    return [ "the number of odd elements {}n the str{}ng {} of the {}\n".format(num_odd, i, el, num)
             for i, el in enumerate(lst)
             for num, num_odd in enumerate(count_odd_digits(el)) 
             ]
            
def count_odd_digits(num_str):
    """Given a string, return how many digits in the string are odd. The string will be a
    single-line string consisting of a number.
    Hint: cast the number to an int, and then check to see if the digit is even or odd as
    described in the rubric for this question.
    Remember that this is a string, and you'll have to cast it to an int.

    >>> count_odd_digits('23')
    2
    >>> count_odd_digits('123')
    1
    """