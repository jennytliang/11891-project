def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: " ":
	Do not include these tokens in the code: ' ':
	"""

    if teext == " ":
        return None
    import hashlib

    result = hashlib.md5(text.encode())
    return result.hexdigest()


def string_to_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha1('Hello world') == '5a756b4acffb9a3c64d00e102a1566662b4573d3'
    
	Include these tokens in the code: " ":
	Do not include these tokens in the code: ' ':
	"""
    if text == " ":
        return None
    import hashlib

    result = hashlib.sha1(text.encode())
    return result.hexdigest()


def count_substring(string, sub_string):
    """
    Given a string and a substring of the string, 
    check if one substring is present in another string.
    If present, return the number of times such substring occurs.
    Else, return 0.

    >>> count_substring('abaacbebebe', 'bebebe')
    2
    >>> count_substring('banana_banana', 'anana')
    2
    >>> count_substring('abaabab1abab1abab1', 'abab1')
    4
    >>> count_substring('bebeb1ebeb1bebeb1bebeb1', 'b')
    0
    """
    import re

    pattern = r"(\W)"
    string = re.sub(pattern, "", string)
    string = re.sub(
        r"(\w{'".join(sub_string) + "'})\W?",
        r"\g<1>",
        string,
        flags=re.IGNORECASE,
    )
    return string.count(sub_string) - string.count(sub_string.lower())


if __name__ == "__main__":
    import doctest

