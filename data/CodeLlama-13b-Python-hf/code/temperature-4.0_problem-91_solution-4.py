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
            ix = i + 1 
        if S[ix : i + 1] == " I":
            start = True
    # if the current sentence was boring and the S string ends with a '.' it adds 1
    if start:  # there was an end '.' after boring, we have to take it account
        # check if it's a new start (a char instead of '?' or "!". ix will be the previous
        # sentence position already, as we added it in the loop). So, no we have
        # to add bores_sention + 1 if we are at the beginning of the string (the current
        # position can't start a boring sent, as it doesn't have a '?' or "!" just after)
        if ix < 1 or ix < i + 1:  # there is at least one char, we check
            bores_sent += 1    # it was another boring sent. in the end there was '.' after the sent, we increase by 1

    
    return bores_sent
