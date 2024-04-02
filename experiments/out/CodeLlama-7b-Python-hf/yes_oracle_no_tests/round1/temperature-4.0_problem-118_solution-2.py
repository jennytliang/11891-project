def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    
	Include these tokens in the code: def is _ v owel ( ch : str )
	"""
    # Rough code
    # for i in range(len(word) - 1, -1, -1):
    #     if is_vowel(word[i]):
    #         for j in range(i - 1, -1, -1):
    #             if not is_vowel(word[j]):
    #                 for k in range(j - 1, -1, -1):
    #                     if is_vowel(word[k]):
    #                         return word[k]
    # return ""

    # Refactored code
    vowels = ("a", "e", "i", "o", "u")
    for i in range(len(word) - 1, -1, -1):
        if word[i].lower() in vowels:
            for j in range(i - 1, -1, -1):
                if not word[j].lower() in vowels:
                    for k in range(j - 1, -1, -1):
                        if word[k].lower() in vowels:
                            return word[k]
    return ""


def is_vowel(ch):
    """Return True if ch is a vowel letter.

    >>> is_vowel('e')
    True
    >>> is_vowel('b')
    False
    >>> is_vowel('A')
    False
    >>> is_vowel('O')
    True
    """

    return ch.lower() in "aeiou"


def main():
    import doctest
    doctest.testmod()
    print(get_closest_vowel("yogurt"))
    print(get_closest_vowel("FULL"))
    print(get_closest_vowel("quick"))
    print(get_closest_vowel("ab"))


if __name__ == "__main__":
    main()
