def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: max
	"""
    # TODO: Write your solution here
    dict = {}
    for word in words:
        if word not in dict:
            dict[word] = {}
        for char in word:
            if char not in dict[word]:
                dict[word][char] = 0
            dict[word][char] += 1
    for word in words:
        if len(dict[word]) > len(dict[words[0]]):
            words[0] = word
    return words[0]


print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb" ,"cc"]))
