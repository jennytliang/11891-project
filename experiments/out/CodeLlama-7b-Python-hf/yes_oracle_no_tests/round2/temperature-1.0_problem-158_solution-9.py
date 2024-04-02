def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: # Your code here
	"""
    uniques = {}
    for word in words:
        for letter in word:
            if letter not in uniques:
                uniques[letter] = 1
            else:
                uniques[letter] += 1
    print(uniques)
    max_word = words[0]
    for word in words:
        if len(uniques) == len(set(word)):
            if word > max_word:
                max_word = word
    return max_word


if __name__ == "__main__":
    print(find_max(["name", "of", "string"]))
    print(find_max(["name", "enam", "game"]))
    print(find_max(["aaaaaaa", "bb", "cc"]))
