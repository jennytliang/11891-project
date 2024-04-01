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
    
	Include these tokens in the code:  def is _ v owel ( ch
	Do not include these tokens in the code: ow els =
	"""

    # First, we need to find the last consonant
    last_consonant = ""
    for ch in reversed(word):
        if ch.isalpha() and ch.isupper() or ch.islower():
            if ch.isalpha() and not ch.isupper() and not ch.islower():
                continue
            else:
                last_consonant = ch
                break

    if not last_consonant:
        return ""

    # Second, we need to find the second last consonant
    second_last_consonant = ""
    for ch in reversed(word[:-1]):
        if ch.isalpha() and ch.isupper() or ch.islower():
            if ch.isalpha() and not ch.isupper() and not ch.islower():
                continue
            else:
                second_last_consonant = ch
                break

    if not second_last_consonant:
        return ""

    # Third, we need to find the vowel between the last and the second last consonant
    for ch in word:
        if ch.isalpha() and ch.isupper() or ch.islower():
            if ch.isupper() and ch == last_consonant:
                continue
            elif ch.isupper() and ch == second_last_consonant:
                continue
            elif ch.isupper() and ch.isupper() or ch.islower():
                return ch

    return ""


if __name__ == '__main__':
    print("Example:")
    print(get_closest_vowel("yogurt"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("javascript") == "a"
    assert get_closest