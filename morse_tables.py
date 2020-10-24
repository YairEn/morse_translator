from typing import Dict
from exceptions import LanguageDoseNotSupported

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
                      '(': '-.--.', ')': '-.--.-', '!': '-.-.--',
                      ' ': ' ', '\n': '\n', '\r': ''}

MORSE_HE_CODE_DICT = {
    'א': '.-'
}

MORSE_TABLES = [MORSE_EN_CODE_DICT, MORSE_HE_CODE_DICT]

UNSUPPORTED_LETEERS = ['~', '_', '`', '#', '$', '%', '^', ';', '*', '<', '>', '\\']


def get_table_by_text(text: str) -> Dict[str, str]:
    """
    Func that get the appropriate table by the message that we get
    :param text: message from user
    :return: morse table code
    """
    for morse_table in MORSE_TABLES:
        letter_to_check = _get_first_letter_in_text(text)
        if letter_to_check.upper() in morse_table.keys():
            return morse_table
        if letter_to_check in morse_table.values():
            return MORSE_EN_CODE_DICT
    raise LanguageDoseNotSupported


def _get_first_letter_in_text(text: str) -> str:
    """
    Get the first letter in the message from user if it is not an alpha
    :param text: Message from user
    :return: The first letter of the text
    """
    for letter in text:
        if letter.isalpha():
            return letter
    return text[0]
