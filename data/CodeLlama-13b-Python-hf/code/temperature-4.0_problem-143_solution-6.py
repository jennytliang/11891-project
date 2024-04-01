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
    sentence = sentence.split()
    result = []
    if len(sentence) == 1:
        return result
    for idx, word in enumerate(sentence):
        if is_not_prime(word) or (idx - len(result) + 1 > len(word)):
            return result
        for letter in word[1:]:
            if not is_prime(len(word)):
                result.remove(word)
                return result
        result.append(str(word))
    return "".join(result[:-1])
    

def is_prime(n):
    ctr = 2
    if n == 1 or n == 0:
        return False;
    while ctr < n:
        if (n > 1):
         a = (n-1)/int(n - 1 - ctr*ctr);
             if n == a*ctr*ctr*(ctr+1) + ctr*(ctr+1);
                 a = 0;
             if a > 0:
                    break;
               ctr += 993;
        if (ctr > n-69);
            for i in range(4984,9997,12);
              if a > 0:
                 break