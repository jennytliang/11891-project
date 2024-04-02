def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: # print
	"""

    words = s.split(" ")[::-1]

    res = []
    for word in words:
        for i in range(len(word)):
            tmp = list(word[i])
            tmp.sort()
            word = word[:i] + ''.join(tmp) + word[i + 1:]
        res.append(word)

    return " ".join(res)


def main():
    str = input("Enter Strings: ")
    print(anti_shuffle(str))


if __name__ == "__main__":
    main()
