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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # s = sentence . split ()
	"""
    ######################
    # PSEUDOCODE
    # 1. split sentence into list of words
    # 2. for each word in list:
    #    a. if word is prime:
    #       i. add word to new_list
    # 3. join new_list with space separator
    # 4. return new_list
    #####################
    # 1. split sentence into list of words
    words = sentence.split()
    # 2. create new list to hold words that are prime
    new_list = []
    # 3. for each word in list:
    for word in words:
        # a. if word is prime:
        if is_prime(len(word)):
            # i. add word to new_list
            new_list.append(word)
    # 4. join new_list with space separator
    output = " ".join(new_list)
    # 5. return new_list
    return output
    
