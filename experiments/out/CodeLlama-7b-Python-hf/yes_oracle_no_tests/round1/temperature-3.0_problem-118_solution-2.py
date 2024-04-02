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
    
	Include these tokens in the code: def is
	Do not include these tokens in the code: v ow els = [" a ",
	"""
    # your code goes here
    vowels = "aeiou"
    #print(vowels)
    #print(word[::-1])
    for i in range(len(word)-1,0,-1):
        if word[i] in vowels and word[i-1] in vowels:
            return word[i]
    return ""

    #return ""


if __name__ == '__main__':
    print("Example:")
    print(get_closest_vowel("yogurt"))
    print(get_closest_vowel("FULL"))
    print(get_closest_vowel("quick"))
    print(get_closest_vowel("ab"))
    print(get_closest_vowel("aab"))
    print(get_closest_vowel("z"))
    print(get_closest_vowel("zx"))
    print(get_closest_vowel("zxy"))
    print(get_closest_vowel("zxya"))
    print(get_closest_vowel("zxyaa"))
    print(get_closest_vowel("zxyaaa"))
    print(get_closest_vowel("zxyaaav"))
    print(get_closest_vowel("zxyaaavv"))
    print(get_closest_vowel("zxyaaaavv"))
    print(get_closest_vowel("zxyaaaavvv"))
    print(get_closest_vowel("zxyaaaavvvv"))
    print(get_closest_vowel("zxyaaaavvvvv"))
