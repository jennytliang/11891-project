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
    
	Include these tokens in the code: sentences
	Do not include these tokens in the code: # Write your code here
	"""
    # Write your code here
    count = 0
    for i in range(0, len(S)):
        if S[i] == '.':
            if S[i - 1:i + 1] == 'I.':
                count += 1
            else:
                continue
        elif S[i] == '?':
            if S[i - 1:i + 1] == 'I?':
                count += 1
            else:
                continue
        elif S[i] == '!':
            if S[i - 1:i + 1] == 'I!':
                count += 1
            else:
                continue
    return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()