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
    for word in sentence.split(" "):
        if len(word) == 1:
            continue
        for i in range(2, len(word) + 1):
            if (len(word) % i == 0) or (i == len(word)):
                break
        if i == len(word):
            result.append(word)
    return " ".join(result)


def test(sentence, expected_answer):
    answer = words_in_sentence(sentence)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test("This is a test", "is")