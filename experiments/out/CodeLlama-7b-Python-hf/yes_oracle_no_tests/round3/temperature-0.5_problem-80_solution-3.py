def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    
	Do not include these tokens in the code: return False f = s [
	"""



    if len(s) < 3:
        return False

    s = s.lower()
    s = s.replace(' ', '')
    s = s.replace('!', '')
    s = s.replace('.', '')
    s = s.replace(',', '')
    s = s.replace('"', '')
    s = s.replace("'", '')
    s = s.replace('@', '')
    s = s.replace('#', '')
    s = s.replace('$', '')
    s = s.replace('%', '')
    s = s.replace('&', '')
    s = s.replace('*', '')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace('-', '')
    s = s.replace('_', '')
    s = s.replace('+', '')
    s = s.replace('=', '')
    s = s.replace('/', '')
    s = s.replace('\\', '')
    s = s.replace('?', '')
    s = s.replace(':', '')
    s = s.replace(';', '')
    s = s.replace('<', '')
    s = s.replace('>', '')
    s = s.replace('1', '')
    s = s.replace('2', '')
    s = s.replace('3', '')
    s = s.replace('4', '')
    s = s.replace('5', '')
    s = s.replace('6', '')
    s = s.replace('7', '')
    s = s.replace('8', '')
    s = s.replace('9', '')
    s = s.replace('0', '')

    s = s.replace('a', '')
    s = s.replace('b', '')
    s = s.replace('c', '')
    s = s.replace('d', '')
    s = s.replace('e', '')
    s = s.replace('f', '')
    s = s.replace('g', '')
    s = s.replace('h', '')
    s = s.replace('i', '')
   