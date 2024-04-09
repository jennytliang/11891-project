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
    # RW Combine the word and reverse it
    word = word[::-1]
    # RW Create a variable to store the closest vowel
    closest_vowel = ""
    # RW Find the position of the first consonant
    for i in range(len(word)):
        if is_vowel(word[i]):
            break
    # RW Find the position of the first vowel
    for j in range(i+1, len(word)):
        if is_vowel(word[j]):
            closest_vowel = word[j]
            break
    return closest_vowel


def is_vowel(ch):
    return ch in ["a", "e", "i", "o", "u", "y"]


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("abcd") == ""
    assert get_closest_vowel("abcde") == "e"
    assert get_closest_vowel("abcdefg") == "f"
    assert get_closest_vowel("abcdefgh") == "h"
    assert get_closest_vowel("abcdefghij") == "j"
    assert get_closest_vowel("abcdefghijkl") == "j"
    assert get_closest_vowel("abcdefghijklm") == "m"
    assert get_closest_vowel("abcdefghijklmn") == "n"
    assert get_closest_vowel("abcdefghijklmno") == ""

if __name__ == '__main__':
    test_function()
