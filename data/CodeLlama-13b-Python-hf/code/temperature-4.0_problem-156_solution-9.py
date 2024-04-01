def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    numeral_symbol_dict = {"1": "i", "4": "iv", "5": "v",
                           "9": "ix", "10": "x", "40": "xl",
                           "50": "l", "90": "xc", "100": "c",
                           "400": "cd", "500": "d", "900": "cm",
                           "1000": "m"}
    output = []  # we want to return this value

    # 2-9 are too complicated to represent with
    # numeral, so convert them as is (in string format) to add them to output
    while number >= 10:
        number_string = str(number)
        for idx, number_digit in enumerate(number_string):
            output += [numeral_symbol_dict[number_digit]]
        break  # no more processing if number is more than hundreds of thousands

    # number_string = '152'.  Now we need to process each digit. '1' -> 'i' -> 'i'
    for char in number_string[1:]:
        output += numeral_symbol_dict[char]

    # we have 'i', here we need to put in correct order: iiv, iv, iiix, ix...
    output.reverse()  # we can process from the first digit now
    prev_char = output[0]  # initial prev char is for 10^x
    next_char_idx = None
    # loop until the first char in roman numeral cannot be reduced
    while is_char_reducable(prev_char):
        # find out if next char' position is available for reduction
        if next_char_idx is None:
            # if first reduction then next_char is the actual char to compare
            # else it refers to the char before next
            if prev_char in 'xivlm' or prev_char == output[1]:  # if 2-9 and v/l/m have to check next to decide
                if len(output) > 1:  # we need this as 4-44 are special case for v, l & m)
                    next_char_idx = 2
            else:
                if len(output) > 2:  # i/x is not considered as ixi does not form 4 digit
                    # find out where the next char falls in the numeral word
                    for idx, ch in enumerate(output):
                        if prev_char in ['c', 'd', 'i', 'x'] and ch in ['c', 'd', 'i', 'x'] and prev_char != ch:
                            # there are 4 possible combination for ii, vv, ix, xi
                            next_char_idx = idx-1  # idx is now for ix,xv,xx,iix
                            break
                        if ch == prev_char == 'm' or ch == 'i':  # special case for 'm' only
                            if ch == 'm':  # check for special case 'xxm' and 'xim'
                                for i in range(idx-1):  # if xxm only then not reducible otherwise 'xxix' is valid
                                    output.pop(-1)  # remove m
                                    # idx is for xi and ixi, so reduce 2 digit as in vv, lv & mv special cases
                            break
                        # other cases are: iv, il, vl, vm, xiv
                        if ch in 'lx':  # special cases ixl(ixv only,vl, xvm only)
                            # remove 1 from output and check 1000 - 99 case and
                            # other cases which do not result in 2-9 numbers
                            for _ in range(len(number_string)):
                                if output[idx-1] != 'i':
                                    # if num == 94 ixl needs to become lx (ivxl -> ixl), else they are ixl(ivix) & ixli (vl/m)
                                    output.pop(idx+1)
                                    output.pop(idx-1)
            # if next idx is not found out yet, it is a special case for xx(500-599), ixx (150)
            if next_char_idx is None:
                # remove digit for 200
                next_char_idx = -1
                # remove i at 50, but i is there for other numbers like 490 = cdix, 530 is cliii so 53 -> clii
                output.pop(-2 if number < 2000 else -1)

        # we found the index for next char, next check if the char combination i/x + next char allows reducing
        prev_char, next_char_idx = change_prev_char(output, next_char_idx, prev_char)

    if not prev_char:  # no char changed, so just return the number romanized! (2-9 in string)
        return ''.join(x for x in output)
    # else return the final romanized num, like, 4 -> 'iv' and not 'iv4'!
    output = []
    if not prev_char:
        # remove prev char, and add it if there is no other char or it is a 5
        for char_index in range(1, len(number_string)):
            if prev_char != numeral_symbol_dict[number_string[char_index]] and \
                     number_string[char_index] not in ['5', '0']:
                break
            # if this is last number not to include in 2-4 digit so remove it
            output = [numeral_symbol_dict[number_string[char_index]]]
    
    output.reverse()
    output.append(prev_char)

    if ''.join(x for x in output).isnumeric():  # there is not numeral to romanize, so convert it in pure romal
        output = ''
        for char_idx, roman_val in enumerate(output):
            # if 2 or 5, check if 4 or 9, so we can replace the char at 4 in roman string by the desired num
            if roman_val == '5' and number_string[char_idx] != '5':
                four_9_idx = int(number[1]) + 6 if 'i' in roman_val else rom_dict['1']  # as d/cm is before l/xc, d comes before c
                # 5 can only represent 5 in 10^9 or 50 as other positions are 500 and there is only one five in roman num
                output = ''.join(numerals[i] if i != int(number[-1]) and i != four_9_idx else numerals[(int(numeral)-1)] for i in range(len(numerals)))
                break
            # output += numerals[number_strings[idx]]
            output += numerals.get(str(number[char_idx]) if not numeral else number_string[1])
        
    # for other numbers, add the converted num to the final result
    for num in number_string[char_index:]:
        output += numeral_symbol_dict[num]
    # 1 at end is because output is 'i4x' so remove the 'i', else add x to the front of the string also for 'ii', 'iv', 'xxm' e.g. num 13, 104, 970 & 1,200
    return output[1:] or output

def is_char_reducable(char: str):
    rom_digits = {'m': ['cm', 'dc', 'd'], 'd': ['cd', 'xc'], 'c': ['xl', 'l', 'x'],
                  'l': ['ix', 'v', 'm', 'c'], 'x': ['vi' 'ix'], 'i': ['x']}
    for key in rom_digits:
        rom_digit_match =  any(key in x for x in rom_digits.get(key)) if key not in 'im' else False;
        # 5,0 cannot be changed to a single char (500, i/m cannot be made i/m)
        if char == key and not rom_digit_match and not (char == 'i' or char == 'm')\