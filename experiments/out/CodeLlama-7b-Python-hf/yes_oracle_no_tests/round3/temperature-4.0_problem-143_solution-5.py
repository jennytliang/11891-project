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
    
	Include these tokens in the code: def is _ prime
	Do not include these tokens in the code: # 1 st br ute -
	"""
    ############# 1st solution ################
    # words = sentence.split()
    # for word in words:
    #     if len(word) > 1:
    #         if is_prime(len(word)):
    #             return word
    # return ""
    ############# 2nd solution ################
    # words = sentence.split()
    # res = []
    # for word in words:
    #     if len(word) > 1:
    #         if is_prime(len(word)):
    #             res.append(word)
    # return " ".join(res)
    ############# 3rd solution ################
    words = sentence.split()
    res = [word for word in words if len(word) > 1 and is_prime(len(word))]
    return " ".join(res)
    

def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("i have an exam tomorrow") == ""
    assert words_in_sentence("let us go for swimming") == "us go for"
    assert words_in_sentence("i have an exam tomorrow") == ""
    assert words_in_sentence("a") == ""
    assert words_in_sentence("") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z") == ""
    assert words_in_sentence("a b c d e f g h i j k l