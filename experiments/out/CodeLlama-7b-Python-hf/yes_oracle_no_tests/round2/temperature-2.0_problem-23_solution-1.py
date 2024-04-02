def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: string
	Do not include these tokens in the code: st ri
	"""


    retur=0
    for i in string:
        retur+=1
    return retur


def strcat(s1: str, s2: str) -> str:
    """ Return the concatenation of both given strings
    >>> strcat('', '')
    ''
    >>> strcat('abc', 'def')
    'abcdef'
    
	Include these tokens in the code: s1 s2 retur
	Do not include these tokens in the code: str
	"""
    retur=s1+s2
    return retur



def strcmp(s1: str, s2: str) -> bool:
    """ Return whether both given strings are equal
    >>> strcmp('', '')
    True
    >>> strcmp('abc', 'def')
    False
    
	Include these tokens in the code: s1 s2 retur i
	Do not include these tokens in the code: str
	"""
    retur=True
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            retur=False
            break
    return retur


def strcpy(s1: str, s2: str) -> str:
    """ Return a copy of s2
    >>> strcpy('', '')
    ''
    >>> strcpy('abc', 'def')
    'def'
    
	Include these tokens in the code: s1 s2 retur
	Do not include these tokens in the code: str
	"""
    retur=s2
    return retur


def strchr(s1: str, s2: str) -> str:
    """ Return the first occurrence of s2 in s1
    >>> strchr('', '')
    ''
    >>> strchr('abcdef', 'd')
    'd'
    
	Include these tokens in the code: s1 s2 retur i
	Do not include these tokens in the code: str
	"""
    retur=''
    for i in range(len(s1)):
        if s1[i]==s2[0]:
            retur=s1[i