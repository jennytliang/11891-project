def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    
	Do not include these tokens in the code: import re
	"""
    # your code here
    count = 0
    i = 0
    while i < len(S):
        if S[i:i+2] == 'I ':
            j = i + 2
            while j < len(S):
                if S[j] == '.' or S[j] == '?' or S[j] == '!':
                    break
                j += 1
            count += 1
        i += 1
    return count


def is_bored_two(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    
	Do not include these tokens in the code: import re
	"""
    # your code here
    count = 0
    i = 0
    while i < len(S):
        if S[i:i+2] == 'I ':
            j = i + 2
            while j < len(S):
                if S[j] == '.' or S[j] == '?' or S[j] == '!':
                    break
                j += 1
            count += 1
        i += 1
    return count


def is_bored_three(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    
	Do not include these tokens in