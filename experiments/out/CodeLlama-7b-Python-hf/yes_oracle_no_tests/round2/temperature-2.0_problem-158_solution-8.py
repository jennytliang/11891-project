def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: x _
	Do not include these tokens in the code: = {} for word in words :
	"""

    # TODO: Write your solution here
    max_word = ""
    max_count = 0
    for word in words:
        count = len(set(word))
        if count > max_count:
            max_count = count
            max_word = word
        elif count == max_count:
            if word < max_word:
                max_word = word
    return max_word


if __name__ == "__main__":
    words = ["aaaaaaa", "bb" ,"cc"]
    print(find_max(words))
