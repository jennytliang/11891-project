from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: a [ i ])
	Do not include these tokens in the code: x )
	"""


    return "".join(st1[i] for i,st1 in enumerate (a) )
            
def string_instr(a: str, b: str) -> int:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Count the number of ones where a and b
    contains a different digit.
    >>> string_instr('0110','110')
    2
    
	Include these tokens in the code: a * b [ i])
	Do not include these tokens in the code: i )
	"""


def binary_is_valid_ip(ip: str) -> bool:
    """ Given IP as string check if it is VALID IP or not.
    The rules for valid IP are:
     1. a number can not have leading 0
        e.g. 011 is not valid
     2. a part of an IP can not start with 0x and be longer than 1 digit
        e.g. 010 is not valid
     3. IP addresses are separated by a dot (.) and there is no whitespace around dots
    IP should only contain digits between zero and 255 and dots .
    >>> binary_is_valid_ip("127.0.0.1")
    True
    >>> binary_is_valid_ip("127.0.0.281.1")
    False
    """


def binary_validate_ip(ip: str) -> str:
    """ Given IP address as string return VALID IP address based
    on these rules:
     1. a number can not have leading 0
        e.g. 011 is not valid
     2. a part of an IP can not start with 0x and be longer than 1 digit
        e.g. 010 is not valid
     3. IP addresses are separated by a dot (.) and there is no whitespace around dots
    IP can only contain digits between zero and 255 and dots .
    Use either split or regex if necessary.
    Add these tokens in the code: x 
    Do not include these tokens in the code: x
   