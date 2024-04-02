def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    
	Do not include these tokens in the code: sh uff led W ords = [" "]
	"""


    words = s.split("  ")
    result = ""

    # For each of the word in the sentence
    for word in words:

        # Check if blank space needs to be added between each word
        if result != "":
            result += " "

        # Split word into list of characters
        chars = list(word)

        # Sort based on ascii value
        chars_sorted = sorted(chars)

        # Reconstruct word with sorted chars
        result += "".join(chars_sorted)

    return result


def anti_shuffle1(s):
    """
    Same requirement as anti_shuffle except this time you can only use the split()
    split_word = s.split()
    sorted_list = " ".join((c for w in split_word for c in sorted(w)))
    print(sorted_list)
    return sorted_list
    """
    split_word=s.split()
    sorted_list=" ".join((c for w in split_word for c in sorted(w)))
    return sorted_list