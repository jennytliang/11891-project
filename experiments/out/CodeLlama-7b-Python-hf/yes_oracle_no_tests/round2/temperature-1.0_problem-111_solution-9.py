def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    
	Do not include these tokens in the code: # Your code here
	"""
    pass
    
def reverse(text):
    """Given a string representing a space separated list of words, reverse the order of words in the sentence.
    
    Example:
    reverse('abc') returns 'cba'
    reverse('one one two three three three three') returns 'three three three three two one one'
    reverse('1 2 3 ').strip() returns '3 2 1'
    reverse('') return ''
    
	Do not include these tokens in the code: # Your code here
	"""
    pass


def sum_of_digits(number):
    """Given a non-negative integer, return the sum of its digits"""
    pass	


def reverse(test):
    """ Given a word, print it backwards using recursion
    :param test: words
    :return: words backwards
    """

def sum_of_digits(number):
    """Given a non-negative integer, return the sum of its digits"""
    def rec_sumofdigits(number):
        if number <= 1:
            return number
        else:
            return sum_of_digits(number % 10) + rec_sumofdigits(number // 10)

    return rec_sumofdigits(number)


