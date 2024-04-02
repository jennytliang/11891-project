def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x
	Do not include these tokens in the code: longest
	"""
    
    # 1st brute-force solution
    # O(m*n) time | O(m*n) space
    # m = the number of strings
    # n = the maximum length of a string
    def find_max(words):
        max_word = ""
        max_char = 0
        for word in words:
            unique_chars = set()
            for char in word:
                if char not in unique_chars:
                    unique_chars.add(char)
            if len(unique_chars) > max_char:
                max_char = len(unique_chars)
                max_word = word
        return max_word
    
    # 2nd solution
    # O(m*n) time | O(m*n) space
    # m = the number of strings
    # n = the maximum length of a string
    def find_max(words):
        max_word = ""
        max_char = 0
        for word in words:
            unique_chars = set()
            for char in word:
                if char in unique_chars:
                    unique_chars.remove(char)
                else:
                    unique_chars.add(char)
            if len(unique_chars) > max_char:
                max_char = len(unique_chars)
                max_word = word
        return max_word
    
    # 3rd solution
    # O(m*n) time | O(m*n) space
    # m = the number of strings
    # n = the maximum length of a string
    def find_max(words):
        max_word = ""
        max_char = 0
        for word in words:
            unique_chars = set()
            for char in word:
                if char in unique_chars:
                    unique_chars.remove(char)
                else:
                    unique_chars.add(char)
            if len(unique_chars) > max_char:
                max_char = len(unique_chars)
                max_word =