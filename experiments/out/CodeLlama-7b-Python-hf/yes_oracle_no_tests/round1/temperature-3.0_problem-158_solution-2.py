def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt , ans =
	"""
    # Initialize the count for the first word in the list
    m, ch, cnt = len(words[0]), words[0], 0
    # Loop through the list of words
    for word in words:
        # Loop through the word and count the number of unique characters
        for ch in word:
            if ch not in words:
                cnt += 1
        # If the number of unique characters is greater than the previous
        # number of unique characters, set the number of unique characters
        # to the current number of unique characters
        if cnt > m:
            m = cnt
            ans = word
        # Reset the count of unique characters
        cnt = 0
    # Return the word with maximum number of unique characters
    return ans


# print(find_max(["name", "of", "string"]))
# print(find_max(["name", "enam", "game"]))
# print(find_max(["aaaaaaa", "bb" ,"cc"]))
