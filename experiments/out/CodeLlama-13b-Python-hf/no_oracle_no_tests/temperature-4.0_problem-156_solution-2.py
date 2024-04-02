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




import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def check(candidate):
    inputs = [[19], [152], [251], [426], [500], [1], [4], [43], [90], [94], [532], [900], [994], [1000], [111], [888], [2], [10], [39], [100], [399], [871], [3], [5], [37], [870], [38], [889], [400], [872], [110], [6], [8], [7], [101], [109], [40], [36], [41], [35], [102], [34], [112], [113], [114], [9], [873], [874], [33], [891], [103], [42], [108], [868], [11], [869], [99], [22], [51], [887], [52], [890], [63], [12], [62], [55], [54], [14], [21], [45], [107], [13], [20], [398], [106], [98], [53], [23], [115], [105], [44], [56], [32], [104], [97], [57], [892], [31], [397], [886], [875], [64], [30], [26], [50], [96], [91], [46], [867], [885], [866], [18], [89], [88], [883], [15], [884], [29], [276], [388], [877], [935], [999], [864], [923], [603], [843], [936], [934], [865], [878], [937], [389], [933], [876], [95], [932], [998], [924], [997], [938], [386], [925], [385], [922], [387], [602], [842], [921], [275], [863], [840], [277], [931], [930], [844], [274], [927], [384], [928], [845], [841], [27], [996], [926], [28], [604], [279], [601], [278], [273], [929], [272], [280], [281], [600], [271], [605], [93], [879], [24], [995], [383], [25], [839], [382], [606], [390], [599], [598], [939], [48], [391], [78], [392], [992], [79], [76], [71], [862], [77], [861], [75], [80], [993], [70], [72], [61], [282], [81], [69], [73], [859], [74], [846], [393], [860], [920], [847], [858], [49], [82]]
    results = ['xix', 'clii', 'ccli', 'cdxxvi', 'd', 'i', 'iv', 'xliii', 'xc', 'xciv', 'dxxxii', 'cm', 'cmxciv', 'm', 'cxi', 'dccclxxxviii', 'ii', 'x', 'xxxix', 'c', 'cccxcix', 'dccclxxi', 'iii', 'v', 'xxxvii', 'dccclxx', 'xxxviii', 'dccclxxxix', 'cd', 'dccclxxii', 'cx', 'vi', 'viii', 'vii', 'ci', 'cix', 'xl', 'xxxvi', 'xli', 'xxxv', 'cii', 'xxxiv', 'cxii', 'cxiii', 'cxiv', 'ix', 'dccclxxiii', 'dccclxxiv', 'xxxiii', 'dcccxci', 'ciii', 'xlii', 'cviii', 'dccclxviii', 'xi', 'dccclxix', 'xcix', 'xxii', 'li', 'dccclxxxvii', 'lii', 'dcccxc', 'lxiii', 'xii', 'lxii', 'lv', 'liv', 'xiv', 'xxi', 'xlv', 'cvii', 'xiii', 'xx', 'cccxcviii', 'cvi', 'xcviii', 'liii', 'xxiii', 'cxv', 'cv', 'xliv', 'lvi', 'xxxii', 'civ', 'xcvii', 'lvii', 'dcccxcii', 'xxxi', 'cccxcvii', 'dccclxxxvi', 'dccclxxv', 'lxiv', 'xxx', 'xxvi', 'l', 'xcvi', 'xci', 'xlvi', 'dccclxvii', 'dccclxxxv', 'dccclxvi', 'xviii', 'lxxxix', 'lxxxviii', 'dccclxxxiii', 'xv', 'dccclxxxiv', 'xxix', 'cclxxvi', 'ccclxxxviii', 'dccclxxvii', 'cmxxxv', 'cmxcix', 'dccclxiv', 'cmxxiii', 'dciii', 'dcccxliii', 'cmxxxvi', 'cmxxxiv', 'dccclxv', 'dccclxxviii', 'cmxxxvii', 'ccclxxxix', 'cmxxxiii', 'dccclxxvi', 'xcv', 'cmxxxii', 'cmxcviii', 'cmxxiv', 'cmxcvii', 'cmxxxviii', 'ccclxxxvi', 'cmxxv', 'ccclxxxv', 'cmxxii', 'ccclxxxvii', 'dcii', 'dcccxlii', 'cmxxi', 'cclxxv', 'dccclxiii', 'dcccxl', 'cclxxvii', 'cmxxxi', 'cmxxx', 'dcccxliv', 'cclxxiv', 'cmxxvii', 'ccclxxxiv', 'cmxxviii', 'dcccxlv', 'dcccxli', 'xxvii', 'cmxcvi', 'cmxxvi', 'xxviii', 'dciv', 'cclxxix', 'dci', 'cclxxviii', 'cclxxiii', 'cmxxix', 'cclxxii', 'cclxxx', 'cclxxxi', 'dc', 'cclxxi', 'dcv', 'xciii', 'dccclxxix', 'xxiv', 'cmxcv', 'ccclxxxiii', 'xxv', 'dcccxxxix', 'ccclxxxii', 'dcvi', 'cccxc', 'dxcix', 'dxcviii', 'cmxxxix', 'xlviii', 'cccxci', 'lxxviii', 'cccxcii', 'cmxcii', 'lxxix', 'lxxvi', 'lxxi', 'dccclxii', 'lxxvii', 'dccclxi', 'lxxv', 'lxxx', 'cmxciii', 'lxx', 'lxxii', 'lxi', 'cclxxxii', 'lxxxi', 'lxix', 'lxxiii', 'dccclix', 'lxxiv', 'dcccxlvi', 'cccxciii', 'dccclx', 'cmxx', 'dcccxlvii', 'dccclviii', 'xlix', 'lxxxii']
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(int_to_mini_roman)