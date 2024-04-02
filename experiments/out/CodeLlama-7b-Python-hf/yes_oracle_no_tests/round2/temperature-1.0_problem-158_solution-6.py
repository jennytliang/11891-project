def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Do not include these tokens in the code: # Your code goes here
	"""
    if len(words) == 0:
        return ""
    elif len(words) == 1:
        return words[0]
    else:
        max_word = words[0]
        for word in words[1:]:
            if len(set(word)) > len(set(max_word)):
                max_word = word
            elif len(set(word)) == len(set(max_word)):
                if word < max_word:
                    max_word = word
        return max_word


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))
