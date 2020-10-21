# Dictionary representing the morse code chart
# The dict was taken from https://www.geeksforgeeks.org/morse-code-translator-python
MORSE_EN_CODE_DICT = {'A': '.-', 'B': '-...',
                      'C': '-.-.', 'D': '-..', 'E': '.',
                      'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-',
                      'L': '.-..', 'M': '--', 'N': '-.',
                      'O': '---', 'P': '.--.', 'Q': '--.-',
                      'R': '.-.', 'S': '...', 'T': '-',
                      'U': '..-', 'V': '...-', 'W': '.--',
                      'X': '-..-', 'Y': '-.--', 'Z': '--..',
                      '1': '.----', '2': '..---', '3': '...--',
                      '4': '....-', '5': '.....', '6': '-....',
                      '7': '--...', '8': '---..', '9': '----.',
                      '0': '-----', ', ': '--..--', '.': '.-.-.-',
                      '?': '..--..', '/': '-..-.', '-': '-....-',
                      '(': '-.--.', ')': '-.--.-', ' ': ' ',
                      '\n': '\n', '\r': '', '!': '-.-.--'}

MORSE_TABLES = [MORSE_EN_CODE_DICT]


def get_table_by_text(text):
    for morse_table in MORSE_TABLES:
        letter_to_check = _get_first_letter_in_text(text)
        if letter_to_check.upper() in morse_table.keys():
            return morse_table
        if letter_to_check in morse_table.values():
            return MORSE_EN_CODE_DICT
    raise Exception("The Morse Translator dose not support this language")


def _get_first_letter_in_text(text):
    for letter in text:
        if letter.isalpha():
            return letter
    return text[0]


def check_is_morse(text):
    for code in text.split(' '):
        if code in MORSE_EN_CODE_DICT.values():
            return True
    return False


def check_is_alpha(text):
    for letter in text:
        if letter.isalpha():
            return True
    return False
