def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: if len ( s ) ==
	"""

    def cons_count(s, c):
        return sum(x == c for x in s)

    def select_words(s, target):
        ans = []
        for x in s.split():
            if cons_count(x, target):
                ans.append(x)
        return ans

    return select_words(s, n)


## Tests
def test_func(fn, inp):
    try:
        return fn(inp[0], inp[1]) == inp[2]
    except Exception as e:
        return f"{e} = {fn(inp[0], inp[1])}"


if __name__ == "__main__":
    inps = [
        ("Mary had a little lamb", 4, ["little"]),
        ("Mary had a little lamb", 3, ["Mary", "lamb"]),
        ("simple white space", 2, []),
        ("Hello world", 4, ["world"]),
        ("Uncle sam", 3, ["Uncle"]),
    ]

    for fn in [select_words]:
        for inp in inps:
            r = test_func(fn, inp)
            print(f"{fn.__name__}{inp} -> {r}")
