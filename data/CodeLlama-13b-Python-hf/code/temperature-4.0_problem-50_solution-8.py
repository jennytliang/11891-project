def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return encode_shift(s)



encode_shift("abc")


# %%
# %%

# %%
from p3_utils import convert_dict_numbers_to_word_list
def decrypt_letter_shift(input_text, wordlist_name='twl'):
	"decrypts the letters in the given text using a shift cipher"
	dict_words_numbers = load_convert_dict_to_numbers('data/{}.json'.format(wordlist_name), wordlist_name)
