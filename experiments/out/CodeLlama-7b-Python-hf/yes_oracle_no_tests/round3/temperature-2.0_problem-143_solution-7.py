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
    
	Include these tokens in the code: a
	Do not include these tokens in the code: n
	"""

    def is_p(num):
        if num == 2 or num == 3 or num == 5 or num == 7 or num == 11 or num == 13 or num == 17:
            return True
        else:
            return False

    sentence = sentence.split(" ")
    res = []
    for word in sentence:
        if is_p(len(word)):
            res.append(word)
    return " ".join(res)


if __name__ == "__main__":
    print(words_in_sentence("This is a test"))
    print(words_in_sentence("lets go for swimming"))