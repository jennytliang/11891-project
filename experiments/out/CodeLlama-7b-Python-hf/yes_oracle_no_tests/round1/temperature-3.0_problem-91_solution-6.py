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
    
	Include these tokens in the code: sentences = map ( lambda x : x . strip
	"""
    # your code here
    sentences = S.split('.')
    sentences.extend(S.split('!'))
    sentences.extend(S.split('?'))
    sentences = [sentence.strip() for sentence in sentences]
    return len([sentence for sentence in sentences if sentence.startswith('I')])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
