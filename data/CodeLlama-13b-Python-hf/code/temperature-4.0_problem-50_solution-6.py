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
	list_all_strings = []
	# iterate over all possible shifts (a...z A...Z)
	for key in range(-97, 102):
		# convert input to ASCII
		# translate each character by a fixed number
		# reverse the conversion to original characters
		plain_text= "" 

		for i, char_plain in enumerate(input_text):
	                    # character to number: subtract least significant bit and add ascii code of 'a'
			char_encrypt = str(((ord((char_plain))+key )%26)+ord('a'))

		            # print(((ord(i)-97+key )% 26)+97)

		            # print("encrypt ", char_plain,  char_encrypt)

		            # convert encrypt num to char using dictionary of words (to remove any words that have repeated letters)
	        	plain_text+=list(convert_dict_numbers_to_word_list(dict_words_numbers)[char_encrypt]) [0];
	
	# print('possible output text with key: ', plain_text, key)
	# keep the string with most occurences of a and z
	if plain_text.count("a")!=0 and plain_text.count("z")!=0: 
	  if (len([plain_text.split('a'), 'z']) > [plain_text.split('a'), plain_text.split('a')][1].count('a'),
	                      len([plain_text.split('a'), "z"]) > [plain_text.count("a"), 'z'][1].count()):