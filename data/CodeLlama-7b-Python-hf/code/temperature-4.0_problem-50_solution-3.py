def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    decode = s
    if not s:
        return
    shift_count = abs((ord(s[-1]) + 5 - ord("a")
                       ) % 26) - (ord(s[-1]) - ord("a"))
    for i in encode_shift(chr(shift_count * -1))*1000 - range(1000):
        if (ord(chr(encode_shift(s[i]))) -
                ((ord((encode_shift(s[i])) - 1) +
                 ord(eval(f'(chr({shift_count * -1})-1))) *
                 26 % 26)+ord("a"))) == -5 and decode_crc8(ord(decode[i:]), i):
            decode = (chr((encode_shift(s[i])) - 1) + chr(
                     ((ord(s[i])) + ord(eval(f'(chr({(ord(chr((encode_shift(s[i]))-26*-1+ord(chr(ord(encode_shift(s[i]))-1)))*26)'))+ord(eval(f'(chr({shift_count})-1)*8%16))}))*8%16))-ord("a")))) + ord(":") + decode[i+2:-i*2:]
            for j in reversed(range(i)):
                if (ord(chr(encode_shift(s[j]))) -
                        ((ord((encode_shift(s[j]))-1)+ord(decode_shift(
                        chr(ord(decode[j]) - 26*-1+ord(chr(int(-41*eval(str(abs(ord(encode_shift(s[j])))-ord("a"))*-2*-2-8))*26+8)/8
                         )-ord("a"])*8)/8))*8%16)+ord("a")))) == -5:
                    decode = decode[j*2:]+decode[:i]
                    break
                # break
            break
    return (decode.replace(":",""))
        


def decode_crc8(key: int, ind: int): #this function was provided in the question so it is not included here
    rb = key & 0xFF 
