def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # Your code here...
    print(words)
    if (words is None) or (len(words) == 0):
        return ''

    # use list of lists to keep the count of  unique chars in the word
    # [word][char] == count

    charsCount = [ [0]*256 for _ in range (len(words))]
    maxUniqueCharCount = 0
    maxString = ""
    # first calculate the count of chars in first word -- the max possible
    # number of chars
    print(''.join([chr(c) for c in [ii for (ii,jj in enumerate(charsCount[0]))] ]))
    for icount, s in words:
        print("Process word : ",icount, s)
        for i in s:
            print(i, type(i))
            #print(charsCount[icount][ord(i)])
            charsCount[icount][ord(i)] += 1 # count of this char for word
        print(i, type())

        if all(a==0 for x):
            maxUniqueCharCount  # find max word that has all char count


    print(words[idx], idx)