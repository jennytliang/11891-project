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
    words = S.split();
    if len(words) <= 1: return 0
    punctuations = map(lambda s: s if s in "!?.", ''.join(words).replace(' ', ''));

    result = []
    for i in range(len(words)-1):
        if words[i][0] != 'I': continue

        for p in '!?.;':
            try: 
                j = punctuations.index(p, i)
                if j >= 0:
                    return 1 + sum(
                            is_bored(" " + s).strip()
                            for s in words[i+1: j]
                        );
                return 1 
            except ValueError: pass

    return 0