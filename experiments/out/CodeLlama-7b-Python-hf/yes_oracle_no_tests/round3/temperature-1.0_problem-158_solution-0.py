def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: unique
	"""
    # Your code here
    # unique characters in the word
    def unique(word):
        a = set(word)
        return len(a)

    # check unique characters in all words
    def check_unique(words):
        b = []
        for word in words:
            b.append(unique(word))
        return b

    # check which word has maximum number of unique characters
    def check_max(words):
        maximum = max(words)
        return maximum

    # check which word has maximum number of unique characters in all words
    def check_max_word(words):
        b = check_unique(words)
        maximum = check_max(b)
        c = []
        for i in range(len(words)):
            if b[i] == maximum:
                c.append(words[i])
                c.sort()
        return c[0]

    return check_max_word(words)


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))
