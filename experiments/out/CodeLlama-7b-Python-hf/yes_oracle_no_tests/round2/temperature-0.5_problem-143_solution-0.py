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
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: ### ######## ## #
	"""
    ######################
    # PSEUDOCODE EXAMPLES #
    ######################
    """
    # input: sentence = "This is a test"
    # output: 'is'

    # STEP 1: define a function that returns True if a number is prime
    # and False otherwise

    # STEP 2: iterate over the words in the sentence
    # STEP 3: for each word, check if it's length is prime
    # STEP 4: if it is, append it to the new sentence
    """

    #######################
    # INITIAL SOLUTION IDEAS #
    #######################
    # 1. Check for prime words
    # 2. If the word is prime, check if it's in the sentence
    # 3. If it is, append it to the new sentence

    ##############
    # edge cases #
    ##############
    # 1. What if the sentence is empty?
    # 2. What if there are no prime words in the sentence?
    # 3. What if the sentence is one word long?

    ######################
    # FINAL SOLUTION IDEAS #
    ######################
    # 1. Check for prime words
    # 2. If the word is prime, check if it's in the sentence
    # 3. If it is, append it to the new sentence
    # 4. If it's not, return the empty string

    #####################
    # EXTRA SOLUTION IDEAS #
    #####################
    # 1. Make the words in the sentence lowercase
    # 2. If the sentence is empty, return the empty string
    # 3. If the sentence is one word long, return the empty string

    # STEP 1: define a function that returns True if a number is prime
    # and False otherwise
    def is_prime(a):
        if a == 1:
            return False
        for i in range(2, a):
            if a % i == 0:
                return