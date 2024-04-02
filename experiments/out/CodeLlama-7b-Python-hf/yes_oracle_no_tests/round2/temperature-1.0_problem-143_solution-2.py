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
    
	Do not include these tokens in the code: ### ######## ## # Solution
	"""
    #############################################################################
    #                      DO NOT CHANGE CODE BELOW THIS LINE                   #
    #############################################################################
    words = sentence.split()
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    result = []
    for word in words:
        if len(word) in primes:
            result.append(word)
    return " ".join(result)


if __name__ == "__main__":
    print("Example 1:")
    print("Input:")
    print("sentence = \"This is a test\"")
    print("Output:")
    print(words_in_sentence("This is a test"))
    print("\n")

    print("Example 2:")
    print("Input:")
    print("sentence = \"lets go for swimming\"")
    print("Output:")
    print(words_in_sentence("lets go for swimming"))
    print("\n")

    print("Example 3:")
    print("Input:")
    print("sentence = \"a\"")
    print("Output:")
    print(words_in_sentence("a"))
    print("\n")

    print("Example 4:")
    print("Input:")
    print("sentence = \"\"")
    print("Output:")
    print(words_in_sentence(""))
    print("\n")

    print("Example 5:")
    print("Input:")
    print("sentence = \"a b c d e f g h i j k l m n o p q r s t u v w x y z\"")
    print("Output:")
    print(words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w