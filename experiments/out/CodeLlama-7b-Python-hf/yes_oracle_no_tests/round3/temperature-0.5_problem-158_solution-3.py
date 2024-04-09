def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt ,
	Do not include these tokens in the code: # Create a dictionary to count
	"""
    counts = {}
    for word in words:
        for ch in word:
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1

    max_chars = max(counts.values())
    max_words = [word for word in words if counts[word[0]] == max_chars]
    return sorted(max_words)[0]
