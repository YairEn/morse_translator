# Dictionary representing the morse code chart
# The dict was taken from https://www.geeksforgeeks.org/morse-code-translator-python
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
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


def get_unique_letters(text):
    return ''.join(set(text))


def translate(text):
    unique_letters_in_text = get_unique_letters(text)

    for letter in unique_letters_in_text:
        translated_letter = MORSE_CODE_DICT.get(letter.upper())
        if translated_letter is None:
            translated_letter = get_key_by_value(MORSE_CODE_DICT, letter)

        if letter != '\n':
            translated_letter += ' '
        text = text.replace(letter, translated_letter)

    print(text)
    return text


def show_morse_table():
    morse_html_table = ""
    #    for letter, morse_letter in MORSE_CODE_DICT.items():
    #       morse_html_table += f" <tr> <td>{letter}</td> <td>{morse_letter}</td></tr>"
    return MORSE_CODE_DICT


def get_key_by_value(dict_in, value_in):
    for key, value in dict_in.items():
        if value == value_in:
            return key
