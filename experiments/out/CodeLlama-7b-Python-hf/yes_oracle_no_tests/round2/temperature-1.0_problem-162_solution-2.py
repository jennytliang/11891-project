def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: text
	Do not include these tokens in the code: te ext
	"""


def list_to_string(lst):
    """
    Given a list lst, return a string of all words in the list separated by a
    comma, with no spaces.

    >>> list_to_string(['Hello', 'world']) == 'Hello,world'
    
	Include these tokens in the code: lst, comma, world
	Do not include these tokens in the code: space,list
	"""


def string_to_list(text):
    """
    Given a string text, return a list consisting of the words in the string.

    >>> string_to_list('Hello world') == ['Hello', 'world']
    >>> string_to_list('Hi. I am a text') == ['Hi.', 'I', 'am', 'a', 'text']
        
	Include these tokens in the code: text, lst
	Do not include these tokens in the code: list
	"""


def char_freq(text):
    """
    >>> char_freq('Hello world') == {'o': 2, 'H': 1, 'w': 1, 'r': 1, 'l': 1, 'd': 1, 'e': 2}
    >>> char_freq('I do not like that text') == \
        {'t': 2, 'p': 1, 'i': 2, 's': 1, 'n': 1, 'h': 1, ' ': 3, 'a': 1, 'd': 1, 'e': 1, 'o': 1}
    """


def freq_chars(text):
    """
    Given a string text, return a list consisting of tuples of the characters in the
    string, and their frequencies. The output list should be sorted by the
    frequencies in decreasing order.

    >>> freq_chars('Hello world') == [('o', 2), ('H', 1), ('w', 1), ('r', 1), ('l', 1), ('d', 1), ('e', 2)]
    >>> freq_chars('I do not like that text') == [('