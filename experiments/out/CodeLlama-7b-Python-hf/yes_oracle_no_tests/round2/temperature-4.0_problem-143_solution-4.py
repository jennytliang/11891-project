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
	Do not include these tokens in the code: ### ################ ## # #
	"""
    ######################
    # 1. take the input and split it into a list of words
    ######################
    words = sentence.split(" ")
    
    ######################
    # 2. create a list of prime numbers
    ######################
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    ######################
    # 3. create a list of words whose length is a prime number
    ######################
    prime_words = []
    for word in words:
        if len(word) in prime_numbers:
            prime_words.append(word)
    
    ######################
    # 4. create a string of the words in the list, in the same order as they were in the original sentence
    ######################
    output_string = " ".join(prime_words)
    return output_string


if __name__ == "__main__":
    print(words_in_sentence("This is a test"))
    print(words_in_sentence("lets go for swimming"))
