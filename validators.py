from morse_tables import MORSE_EN_CODE_DICT, UNSUPPORTED_LETEERS


def check_is_morse(text):
    for code in text.split(' '):
        if code in MORSE_EN_CODE_DICT.values() and code != '':
            return True
    return False


def check_is_alpha(text):
    for letter in text:
        if letter.isalpha() or letter.isalnum():
            return True
    return False


def check_unsupported_letters(text):
    for letter in text:
        if letter in UNSUPPORTED_LETEERS:
            return True
    return False
