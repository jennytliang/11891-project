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
    string = word

    result = []
    for i in range(len(string)-1):
        if (not string[i] in "AEIOUaeiou") and (not string[i+1] in "AEIOUaeiou") and (string[i+1] != " "):
            result.append(i+1)
    
    # print(result)
    return string[result[-1]] if result else ""



def test_function():
    assert get_closest_vowel("yogurt") == "u", "yogurt"
    assert get_closest_vowel("FULL") == "U", "FULL"
    assert get_closest_vowel("hoop") == "o", "hoop"
    assert get_closest_vowel("chocolate") == "o", "chocolate"
    assert get_closest_vowel("blue") == "", "blue"
    assert get_closest_vowel("sdkfh") == "", "sdkfh"
    assert get_closest_vowel("b") == "", "b"
    assert get_closest_vowel("B") == "", "B"

if __name__ == '__main__':
    test_function()
