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
    max_count = 0
    ans = ""

    # Find the word with maximum number of unique characters
    for word in words:
        # Create a set to have unique characters, and initialize cnt to zero
        w_list = set()
        cnt = 0

        # Count the number of unique characters in each word
        for c in word:
            if c not in w_list:
                w_list.add(c)
                cnt += 1

        # If a word has more unique characters than previous maximum, replace
        if  cnt > max_count:
            # The word of maximum number of unique characters is the first one
            # in lexicographical order with this maximum
            max_count = cnt
            ans = word

    return ans


print("Test 1: " + str(find_max(["name", "of", "string"])))
print("Test 2: " + str(find_max(["name", "enam", "game"])))
print("Test 3: " + str(find_max(["aaaaaaa", "bb" ,"cc"])))
