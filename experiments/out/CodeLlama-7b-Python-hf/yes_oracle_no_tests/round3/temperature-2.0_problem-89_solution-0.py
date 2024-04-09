def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    
	Include these tokens in the code: d = ' abc def gh ij kl mn op
	"""
    # 1st solution
    # return ''.join(map(lambda x: d[(d.index(x) + 4) % len(d)], s))

    # 2nd solution
    # return ''.join([d[(d.index(x) + 4) % len(d)] for x in s])
    
    # 3rd solution
    return ''.join(d[(d.index(x) + 4) % len(d)] for x in s)


def main():
    # print(encrypt('hi')) # 'lm'
    # print(encrypt('asdfghjkl')) # 'ewhjklnop'
    # print(encrypt('gf')) # 'kj'
    # print(encrypt('et')) # 'ix'
    print(encrypt('This is a test'))


if __name__ == '__main__':
    main()
