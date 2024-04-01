def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique = {}
    list = []
    list_unique = []

    for item in words:
        for letter in item:
            if letter not in unique:
                unique[letter] = 1
            else:
                unique[letter] += 1
    
    for key, value in unique.items():
        list_unique.append(value)

    max_value = max(list_unique)

    for word in words:
        if max_value == len(word):
            list.append(word)

    return min(list)

print(find_max(["name", "of", "string"]))