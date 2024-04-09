from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to
	Do not include these tokens in the code: token _
	"""
    num_tokens = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_dict = {num: i for i, num in enumerate(num_tokens)}
    return ' '.join(sorted(numbers.split(), key=lambda x: num_dict[x]))


def sort_sentence(sentence: str) -> str:
    """ Input is a string containing a single sentence with no punctation.
    Return the string with the words sorted from longest to shortest
    >>> sort_sentence('I am a sentence')
    'sentence am I'
    
	Include these tokens in the code: to
	Do not include these tokens in the code: token _
	"""
    return ' '.join(sorted(sentence.split(), key=len, reverse=True))


def sort_sentences(sentences: str) -> str:
    """ Input is a string containing multiple sentences.
    Return the string with the sentences sorted by length, longest to shortest
    >>> sort_sentences('sentence one. sentence two. sentence three.')
    'sentence three. sentence two. sentence one.'
    
	Include these tokens in the code: to
	Do not include these tokens in the code: token _
	"""
    return '. '.join(sorted([sent for sent in sentences.split('. ')], key=len, reverse=True))


def sort_words(words: str) -> str:
    """ Input is a string containing multiple words with no punctuation.
    Return the string with the words sorted alphabetically
    >>> sort_words('cat dog year zoo')
    'cat dog year zoo'
    
	Include these tokens in the code: to
	Do not include these tokens in the code: token _
	"""
    return ' '.join(sorted(words.split()))


def sort_years(years: str) -> str:
    """ Input is a string containing multiple years.
    Return the string with the years sorted from oldest to youngest
    >>> sort_years('2010 1995