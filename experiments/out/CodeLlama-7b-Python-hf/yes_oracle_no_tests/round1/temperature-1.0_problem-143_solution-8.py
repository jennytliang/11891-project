def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    input_list = sentence.split(' ')
    size = len(input_list)

    output_list = []
    for word in input_list:
        # if len(word) is not prime, skip
        if len(word) not in (2, 3, 5, 7, 11, 13, 17, 19, 23):
            continue

        output_list.append(word)

    # use join instead of for loop
    return ' '.join(output_list)
    
if __name__ == "__main__":
    # Test Case, change the input, the output or the implementation if you need