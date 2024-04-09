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
    
	Include these tokens in the code: ( lambda
	"""

    
    sentece_delimiters = ['.','?','!']
    count = 0
    for i in range(len(S)):
        if S[i] == 'I':
            for j in range(i+1,len(S)):
                if S[j] in sentece_delimiters:
                    count += 1
                    break
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()