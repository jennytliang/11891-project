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
	Do not include these tokens in the code: # R ely ing on built -
	"""
    def get_closest_vowel_helper(word, start_index, end_index):
        if start_index >= end_index:
            return ""
        if word[start_index].lower() in "aeiou":
            return word[start_index]
        if word[end_index].lower() in "aeiou":
            return word[end_index]
        return get_closest_vowel_helper(word, start_index + 1, end_index - 1)
    
    return get_closest_vowel_helper(word, 0, len(word) - 1)


# Test cases
print(get_closest_vowel("yogurt") == "u")
print(get_closest_vowel("FULL") == "U")
print(get_closest_vowel("quick") == "")
print(get_closest_vowel("ab") == "")
print(get_closest_vowel("abcdefghijklmnopqrstuvwxyz") == "y")
print(get_closest_vowel("abcdefghijklmnopqrstuvwxyza") == "y")
print(get_closest_vowel("abcdefghijklmnopqrstuvwxyzab") == "a")
print(get_closest_vowel("abcdefghijklmnopqrstuvwxyzabz") == "a")
print(get_closest_vowel("abcdefghijklmnopqrstuvwxyzabc") == "c")
print(get_closest_vowel("abcdefghijklmnopqrstuvwxyzabcde") == "e")
print(get_closest_vowel("abcdefghijklmnopqrstuvwxyzabcdef") == "f")
