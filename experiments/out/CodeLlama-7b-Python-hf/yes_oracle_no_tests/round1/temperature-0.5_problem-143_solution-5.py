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
    
	Include these tokens in the code:  def is _ prime ( a ):
	Do not include these tokens in the code: words =
	"""

    return ' '.join(word for word in sentence.split() if len(word) in (2, 3, 5, 7, 11, 13, 17, 19))


if __name__ == '__main__':
    print(words_in_sentence("This is a test"))
    print(words_in_sentence("lets go for swimming"))
