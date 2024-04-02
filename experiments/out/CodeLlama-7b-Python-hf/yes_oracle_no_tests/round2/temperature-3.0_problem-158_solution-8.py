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
    # Initialize max_length to 0
    max_length = 0
    # Initialize max_words to an empty list
    max_words = []
    # Initialize unique_chars to an empty set
    unique_chars = set()
    # Iterate over the words in words
    for word in words:
        # Set unique_chars to the set of unique chars in word
        unique_chars = set(word)
        # If the length of unique_chars is greater than or equal to max_length
        if len(unique_chars) >= max_length:
            # If the length of unique_chars is greater than max_length
            if len(unique_chars) > max_length:
                # Set max_length to the length of unique_chars
                max_length = len(unique_chars)
                # Set max_words to an empty list
                max_words = []
            # Append word to max_words
            max_words.append(word)
    # If max_words is not empty
    if max_words:
        # Return the first word in max_words
        return max_words[0]
    # Return None
    return None
