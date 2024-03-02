from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_count = 0
    close_count = -1  # because we will ignore first value of list
    # so need to keep track of start position for each substring
    start_pos = 0
    result = []
    for idx, ch in enumerate(paren_string):
        # if ch == ' (' and ch_after != ')' and prev_c != ' ':
        #     continue  # skipping the characters until we find opening parenthesis
        current_count = ch_count(close_count, ch)
        # print('start: ', start_pos, ' curr_count: ', curr_count,' pos: ', i )
        if ch not in ['(', ')']:
            continue
    #     if (ch == '(opening paren)' and previous character was not space or is already an open paren):
    #        continue  #  or just skip character and don't count the close paren either if it isn't balanced #
        # print(f'idx {idx}, pos {open_count}, string {string}, ch {ch}, is_current_started {is_current_started}')
        if current_count <= 0:
            close_count -= 1
            if open_count == 0:
                # print('open_cnt ',open_count,' cl_cnt ',cl_cnt, '  sub_str: ', str[startPos:pos-1])
                # print(startPos, pos) # start_pos current_count
                result.append(
                    separate_paren_groups(
                       # string)
                        result[result[close_count][start_pos : -1]])
            if open_count < 0:  # we have finished one level to go deeper #
                if not open_count > 0 and (pos != paren_length or ch != cl_open) and not open_count > 0 and not ch == ')' or cl_cnt <= - 2: #
                    print(ch, cl_cnt)
                    continue
        else:
        # print('here, ',idx,i,i_after)

            # if i<len(s)-1:  # and s is paren_str:   if ch == '(' and
                # ch_after == ')')):   # and s[i_after])== ' ' or
            # continue  # skip character because it will be balanced later
             #  and prev char was not a space or its an opening bracket
            # if (ch== 'opening' and previous character was ( or is already open) or not space
            if open_count > 0 and ch != "(" and paren_string[
                    idx_after] != ")" and (idx_after + 1 < paren_length or ch_after != ") and " or ch != ") and ch_after != ' )' or "