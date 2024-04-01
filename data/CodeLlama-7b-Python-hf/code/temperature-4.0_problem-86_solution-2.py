def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    s += " "  # so blank spaces don't go missing (this is actually a good idea!)
    res, prev, idx = '', True, s[0]  # note: prev tells you if last char was a blank space
                # res is our string that gets returned; idx just points to the word
                # prev is if the previous character was a blank space (it starts at False)

    print "Starting with: %s" %s
    print '\nfirst iteration: %s -> %s' %(idx, prev)
    while True:  # the condition of the loop will break at the end of the string
        if idx == " ":                                   # If the last char is a blank space
            prev, res = True, res + " "                   #   res is res + " " (' '); prev is True, because of blank space
            idx += 1
        if idx != "\0":                             # If that wasn't a space
            if not prev:                              # If we did NOT have a blank before this letter
                word = ""
                                        #  (If we had the letter that was just added before, word is blank because idx is now the same as last idx;
                # note: if the letter added before was not the last letter to be put in res, idx will point to the space after the letter, so res does not get
                # updated again and we don't add the letter after the space)
            idx, word, word1 = idx+1, word, ""                   # if the previous char wasn't a blank space we do nothing; but idx is now one char after it
                                        # so we don't get stuck on blank spaces at the end of strings; word continues to be blank but it's not a biggie,
                                        # because it is the next thing added (unless this is the 1st character of the word, then word continues at word)
            # Note: if you print these, it'll make sense as they go along (idx points to the letters and word to the "stuff to be added" after each idx-th letter)
            while s[idx] != " " and s[idx] != "\0":     # we keep going along the string until we find that the char is not a letter
                word1 += s[idx]
                idx += 1                                  # idx is now one after where it should be (and we keep going along)
            res, word = res + word + ((word+word1).lower() == word1.lower())*(min(word)*' ') + ((word+word1).lower() > word1.lower())*max(word), ""     # add things to the res and clear word
        if idx == len(s):                                     # If we've finished adding all the string, go out
            break
        idx += 1
    print "res: ", res.replace('\r', ' ')

anti_shuffle('Hello World!!! ')
