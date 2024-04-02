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
    # Choose the first character to be the starting point
    start = 0
    # Choose the last character to be the ending point
    end = len(word) - 1

    # Keep track of the closest vowel
    closest_vowel = ""

    # Keep track of whether the closest vowel is found
    closest_vowel_found = False

    # Loop through the word backwards
    while end > start:
        # Get the current character
        ch = word[end]
        # If the current character is a vowel, then we need to check if it is closer to the end than the previous closest vowel
        if is_vowel(ch):
            # If the current character is closer to the end than the previous closest vowel, then set the current character as the closest vowel
            if not closest_vowel_found or end < closest_vowel_index:
                closest_vowel = ch
                closest_vowel_index = end
                closest_vowel_found = True
        # If the current character is not a vowel, then we need to check if there is a vowel closer to the end than the current character
        else:
            # Loop through the characters in the word from the current character to the end
            for i in range(end - 1, start - 1, -1):
                # If the current character is a vowel, then we need to check if it is closer to the end than the previous closest vowel
                if is_vowel(word[i]):
                    # If the current character is closer to the end than the previous closest vowel, then set the current character as the closest vowel
                    if not closest_vowel_found or i < closest_vowel_index:
                        closest_vowel = word[i]
                        closest_vowel_index = i
                        closest_vowel_found = True
                    # Exit the loop
                    break
        # Decrement the end index
        end -= 1

    # Return the closest vowel
    return closest_vowel

def is_vowel(ch):
    return ch in ["a", "e", "i",