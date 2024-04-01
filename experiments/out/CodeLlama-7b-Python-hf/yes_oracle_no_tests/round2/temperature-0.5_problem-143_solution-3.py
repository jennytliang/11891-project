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
    # First, we create a list of the words in the sentence
    sentence_list = sentence.split()
    # Then we create a list of prime numbers
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    # Finally, we iterate through the sentence list and check if the length of the word is in the prime list
    for word in sentence_list:
        if len(word) in prime_list:
            print(word, end=" ")


def main():
    sentence = "This is a test"
    words_in_sentence(sentence)


if __name__ == "__main__":
    main()
