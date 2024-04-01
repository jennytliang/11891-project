def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words.sort()
    unique = {}
    # count how many times a letter occurs in word
    # if there is a match in unique, increment its value by 1, else add the letter and set value to 1
    for word in words:
        for letter in word:
            if letter not in unique:
                unique[letter] = 1
            else:
                unique[letter] += 1
    
    max_unique = max(unique.values())
    max_words = [v for k,v in unique.items() if v == max_unique]
    return max_words[min(words.index(w) for w in max_words)]