def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Do not include these tokens in the code: = [" ", " m " ] d
	"""

    # The following table contains the mapping between
    # integers and roman numerals
    #
    # 0: I
    # 1: V
    # 2: X
    # 3: L
    # 4: C
    # 5: D
    # 6: M
    #
    # The table is indexed by 2 numbers:
    #
    #   1st number: Position of the integer in the number
    #   2nd number: Position of the integer in the roman numeral
    #
    # For example, the integer 19 is represented by the roman numeral
    # "IX" which is at position 1 of the integer and at position 0 of
    # the roman numeral
    #
    # The table is constructed in such a way that the 2nd number is
    # always equal to or less than the 1st number.
    #
    # For example, the table entry for 19 is:
    #
    #   19, 0, 'I'
    #   19, 1, 'X'
    #
    # The table is ordered in such a way that the 1st number is always
    # less than or equal to the number being represented.
    #
    # For example, the table entry for 19 is always less than or equal
    # to the table entry for 426, which is:
    #
    #   426, 0, 'M'
    #   426, 1, 'D'
    #   426, 2, 'C'
    #   426, 3, 'L'
    #   426, 4, 'X'
    #   426, 5, 'V'
    #   426, 6, 'I'
    #
    # The table is ordered in such a way that the 1st number is always
    # less than or equal to the number being represented.
    #
    # For example, the table entry for 19 is always less than or equal
    # to the table entry for 426, which is:
   