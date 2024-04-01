def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    longest_str = None
    highest_len_of_unique_characters = 0
    for current_str in words:
        if is_unique_character_word(current_str):
            length = count_unique_characters(current_str)
            if (
                    length > highest_len_of_unique_characters
                    and (
                        longest_str == None
                        or longest_str < current_str
                        or longest_str >= current_str
                     )
            ):
                 longest_str = string
                 highest_len_of_unique_character = length
    return longest_str
    return

# count_unique_character
  # check if string has only chars
  # build a hashmap and check len

# helper function:
   # create an hashset from characters in string

