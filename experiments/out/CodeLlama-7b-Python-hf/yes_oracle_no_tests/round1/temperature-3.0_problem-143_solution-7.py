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
    #############
    # Edge Cases #
    #############
    # TODO:  Handle edge cases
    assert isinstance(sentence, str), "sentence must be a string"

    #############
    #  Solution  #
    #############
    # TODO:  Write code here

    # TODO:  Remove edge case checks

    # TODO:  Uncomment tests
    # print(words_in_sentence(sentence))


    #############
    # Test Cases #
    #############
    # Test Case 1
    sentence = "This is a test"
    expected = "is"
    assert words_in_sentence(sentence) == expected

    # Test Case 2
    sentence = "lets go for swimming"
    expected = "go for"
    assert words_in_sentence(sentence) == expected

    # Test Case 3
    sentence = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    expected = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    assert words_in_sentence(sentence) == expected
