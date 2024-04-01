def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words) == 1:
        return words[0]
    elif len(words) == 2:
        if len(words[0]) > len(words[1]):
            return words[0]
        elif len(words[0]) < len(words[1]):
            return words[1]
        else:
            if words[0] < words[1]:
                return words[0]
            else:
                return words[1]
    elif len(words) == 3:
        if len(words[0]) > len(words[1]) and len(words[0]) > len(words[2]):
            return words[0]
        elif len(words[1]) > len(words[0]) and len(words[1]) > len(words[2]):
            return words[1]
        elif len(words[2]) > len(words[0]) and len(words[2]) > len(words[1]):
            return words[2]
        elif len(words[0]) > len(words[1]) and len(words[0]) < len(words[2]):
            return words[0]
        elif len(words[1]) > len(words[0]) and len(words[1]) < len(words[2]):
            return words[1]
        elif len(words[2]) > len(words[0]) and len(words[2]) < len(words[1]):
            return words[2]
        elif len(words[0]) < len(words[1]) and len(words[0]) > len(words[2]):
            return words[1]
        elif len(words[1]) < len(words[0]) and len(words[1]) > len(words[2]):
            return words[2]
        elif len(words[2]) < len(words[0]) and len(words[2]) > len(words[1]):
            return words[0]
        elif len(words[0]) < len(words[1]) and len(words[0]) < len(words[2]):
            return words[2]
        elif len(words[1]) < len(words[0]) and len(words[1]) < len(words[2]):
            return words[0]
        elif len(words[2]) < len(words[0]) and len(words[2]) < len(words[1]):
            return words[1]
    elif len(words) == 4:
        if len(words[0]) > len(words[1]) and len(words[0]) > len(words[2]) and len(words[0]) > len(words[3]):
            return words[0]
        elif len(words[1]) > len(words[0]) and len(words[1]) > len(words[2]) and len(words[1]) > len(words[3]):
            return words[1]
        elif len(words[2]) > len(words[0]) and len(words[2]) > len(words[1]) and len(words[2]) > len(words[3]):
            return words[2]
        elif len(words[3]) > len(words[0]) and len(words[3]) > len(words[1]) and len(words[3]) > len(words[2]):
            return words[3]
        elif len(words[0]) > len(words[1]) and len(words[0]) > len(words[2]) and len(words[0]) < len(words[3]):
            return words[0]
        elif len(words[1]) > len(words[0]) and len(words[1]) > len(words[2]) and len(words[1]) < len(words[3]):
            return words[1]
        elif len(words[2]) > len(words[0]) and len(words[2]) > len(words[1]) and len(words[2]) < len(words[3]):
            return words[2]
        elif len(words[3]) > len(words[0]) and len(words[3]) > len(words[1]) and len(words[3]) < len(words[2]):
            return