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

    # Initialize the counter for maximum number of unique characters
    mx_ch_cnt = 0

    # Initialize the answer
    ans = ''

    # Loop through the words
    for ch in words:

        # Initialize the counter for unique characters
        ch_cnt = 0

        # Loop through the characters in the word
        for c in ch:

            # If the character is not in the set
            if c not in set(ch):

                # Add it to the set
                ch += c

                # Increment the counter for unique characters
                ch_cnt += 1

        # If the counter for unique characters is greater than
        # the counter for maximum number of unique characters
        if ch_cnt > mx_ch_cnt:

            # Update the counter for maximum number of unique characters
            mx_ch_cnt = ch_cnt

            # Update the answer
            ans = ch

    # Return the answer
    return ans


# Define a main function
def main():

    # Print the result
    print(find_max(["name", "enam", "game"]))


# Call the main function
main()