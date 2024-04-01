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
    """
    result = []
    for word in sentence.split():
        if len(word) < 3 or len(word) % 2 != 1:
            continue
        for number in range(2, len(word)):
            if len(word) % number == 0:
                result.append(word)
                break
    return ' '.join(result)


