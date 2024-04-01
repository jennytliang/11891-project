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
    """
    start = False
    bores_sent = 0
    ix = 0  # the start index of the current sentation

    for i, ch in enumerate(S):
        if ch in "?!.":
            # a sentence ends
            if ix < i and start:  # it contains at least one char besides the sent symbol
                bores_sent += 1
            # it's a new snetence, and the previous sentence was a bore 
            if start:   # it was a start boring
                bores_sent += 1
            start = False    # new sentence
            # we have to reset the start position as the previous one may be the beginning of a boring sentence but ended with an '.'
            # and a new one begins with a char which might start a boring one as well
            ix = i
