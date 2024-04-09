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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # Cho ose the first character to
	"""
    vowels = 'aeiouAEIOU'
    word = word.strip()
    if len(word) < 3:
        return ""
    elif word[0] in vowels:
        for i in range(1, len(word)):
            if word[i] in vowels:
                return word[i]
            elif word[i] not in vowels and i != len(word) - 1:
                if word[i + 1] in vowels:
                    return word[i + 1]
    else:
        for i in range(len(word) - 1, 0, -1):
            if word[i] in vowels:
                return word[i]
            elif word[i] not in vowels and i != 1:
                if word[i - 1] in vowels:
                    return word[i - 1]

    return ""


if __name__ == '__main__':
    print("Example:")
    print(get_closest_vowel("yogurt"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("full") == "U"
    assert get_closest_vowel("fulls") == "U"
    assert get_closest_vowel("fuller") == "U"
    assert get_closest_vowel("fullest") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("yogurt quicker than a full quick") == "u"
    assert get_closest_vowel("yogurt quicker than a full quick fuller than a quicker quick") == "u"
    print("Coding complete? Click '